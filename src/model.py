import streamlit as st  # Импорт streamlit
import torch  # Импорт torch для работы модели
from transformers import (
    T5ForConditionalGeneration,
    T5Tokenizer,
)
from transformers import (
    FSMTForConditionalGeneration,
    FSMTTokenizer
)# Импорт трансформеров для работы модели


# Загружаем модель и кэшируем ее через декоратор
@st.cache_resource
def loadmodel():
    tokenizer = T5Tokenizer.from_pretrained("cointegrated/rut5-base-multitask")
    model_rut5 = T5ForConditionalGeneration.from_pretrained(
        "cointegrated/rut5-base-multitask"
    )
    return tokenizer, model_rut5


@st.cache_resource
def loadmodel_translation_ru_en():
    tokenizer = FSMTTokenizer.from_pretrained("facebook/wmt19-ru-en")
    model = FSMTForConditionalGeneration.from_pretrained("facebook/wmt19-ru-en")
    return tokenizer, model


@st.cache_resource
def loadmodel_translation_en_ru():
    tokenizer = FSMTTokenizer.from_pretrained("facebook/wmt19-en-ru")
    model = FSMTForConditionalGeneration.from_pretrained("facebook/wmt19-en-ru")
    return tokenizer, model


# Процессинг. Передаем входной текст в модель и получаем результат обработки.
def process(criteria: str, tokenizer, model_rut5):
    inputs = tokenizer(criteria, return_tensors="pt")
    with torch.no_grad():
        hypotheses = model_rut5.generate(
            **inputs,
            num_beams=5,
            min_length=200,
            max_length=500,
            no_repeat_ngram_size=3
        )
    return tokenizer.decode(hypotheses[0], skip_special_tokens=True)


def interpreter(text: str, tokenizer, model):
    input_ids = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded


