from app import session, components, constants
import model


def main():
  # Инициализация состояния приложения
  session.init()

  # Рисуем шапку + описание
  components.header(
    constants.LANG_PACK.get("title"),
    constants.LANG_PACK.get("subtitle"),
    constants.LANG_PACK.get("description"),
  )

  # Подгружаем и кешируем модельку
  with components.spinner(constants.LANG_PACK.get("loading_model_text")):
    tokenizer, model_rut5 = model.loadmodel()

  # Получаем состояние приложения
  state = session.get_state()

  # Рисуем основные компоненты приложения, используя состояние, то есть если мы ввели текст,
  # то сетим в состояние ключ file_uploader_disabled: True, и далее поле загрузки файлом которое
  # следит за этим полем в состоянии - отключается,
  # и так же в обратном порядке для text_area с ключем text_area_disabled
  text_area_data = components.text_area(
    constants.LANG_PACK.get("text_area_label"),
    state.text_area_disabled,
    constants.STATE_KEY_TEXT_AREA
  )
  file_data = components.file_uploader(
    constants.LANG_PACK.get("file_uploader_label"),
    state.file_uploader_disabled,
    constants.STATE_KEY_FILE_UPLOADER
  )
  btn = components.button(constants.LANG_PACK.get("btn_start_label"))
  
  # Получаем критерии (пропсы) для нашей модели, в нашем случае это просто текст
  criteria = text_area_data or file_data

  # Если все ок, то передаем в функцию процессинга, если нет, то пишем что не так
  if bool(criteria) and btn:
    with components.spinner(text=constants.LANG_PACK.get("loading_result_text")):
      res = model.process(f'simplify | {criteria}', tokenizer, model_rut5)

    components.results(constants.LANG_PACK.get("result_text"), res)
  elif not bool(criteria) and btn:
    components.info(constants.LANG_PACK.get("empty_input_text"))


if __name__ == "__main__":
    main()