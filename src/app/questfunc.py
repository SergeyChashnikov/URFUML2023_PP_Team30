import re
import model


# Подготавливаем шаблон для разбиения текста на предложения
pattern = re.compile(
    r'([А-ЯA-Z]((т.п.|т.д.|пр.|г.|т. е.|)|[^?!.\(]|\([^\)]*\))*[.?!])'
)


# Разбиваем текст на предложения
def splitting_the_text(input_text: str):
    res = list()
    for sent in pattern.findall(input_text):
        res.append(sent[0])
    text_len = len(res)
    return text_len, res


#
def combine_and_generate(
    tokenizer,
    model_rut5,
    numb_of_quest,  # Число вопросов
    max_length,  # Максимальная длина вопроса
        res):  # Список исходных предложений

    # Список вопросов
    list_quest = list()
    # Буферный блок текста - основа для вопроса
    log_text_block = str()
    # Расчитываем промежуточные переменные
    text_len = len(res)
    min_log_text_block_size = text_len // numb_of_quest
    remains_sentence = text_len % numb_of_quest

    # Определяем размер первого блока - основы для первого вопроса
    if (remains_sentence == 0):
        num_of_iter = min_log_text_block_size
    else:
        remains_sentence -= 1
        num_of_iter = min_log_text_block_size + 1

    # Начинаем объединять блоки
    for step in range(0, text_len):
        # Если мы подошли к концу блока генерируем вопрос
        # и добавляем в список вопросов
        if ((step == (num_of_iter-1)) and (step < (text_len - 1))):
            log_text_block = log_text_block + res[step]
            list_quest.append(
                model.generate_quest(
                    f"ask | {log_text_block}",
                    tokenizer,
                    model_rut5,
                    max_length
                )
            )
        # Сбрасываем блок
            log_text_block = ""
        # Определяем размер нового блока
            if (remains_sentence > 0):
                remains_sentence -= 1
                num_of_iter = num_of_iter + min_log_text_block_size + 1
            else:
                num_of_iter = num_of_iter + min_log_text_block_size
        # Если мы подошли к концу текста генерируем последний вопрос
        # и добавляем в список вопросов
        elif (step == (text_len - 1)):
            log_text_block = log_text_block + res[step]
            list_quest.append(
                model.generate_quest(
                    f"ask | {log_text_block}",
                    tokenizer,
                    model_rut5,
                    max_length
                )
            )
        # В противном случае продолжаем формировать блок
        else:
            log_text_block = log_text_block + res[step]
    return list_quest


# Генерируем вопросы
def generate_questions(
    tokenizer,
    model_rut5,
    criteria,
    res,
    numb_of_quest,
        max_length):
    # Итоговый список вопросов
    result_list_quest = list()
    # Если нужен один вопрос - генерируем его на основе всего текста
    if (numb_of_quest == 1):
        result_list_quest.append(
            model.generate_quest(
                f"ask | {criteria}",
                tokenizer,
                model_rut5,
                max_length
            )
        )
    # Если вопроса два - бьём текст примерно пополам
    elif (numb_of_quest == 2):
        result_list_quest = combine_and_generate(
            tokenizer,
            model_rut5,
            numb_of_quest,
            max_length,
            res)
    # Если вопросов больше - делаем вопрос ко всему тексту и отдельно к блокам
    else:
        first_quest_list = list()
        first_quest_list.append(
            model.generate_quest(
                f"ask | {criteria}",
                tokenizer,
                model_rut5,
                max_length
            )
        )
        result_list_quest = first_quest_list + combine_and_generate(
            tokenizer,
            model_rut5,
            numb_of_quest - 1,
            max_length,
            res)
    return result_list_quest
