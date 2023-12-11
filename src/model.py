import streamlit as st
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Тут будет встраиваться модель
@st.cache_resource
def loadmodel():
  tokenizer = T5Tokenizer.from_pretrained("cointegrated/rut5-base-multitask")
  model_rut5 = T5ForConditionalGeneration.from_pretrained("cointegrated/rut5-base-multitask")
  return tokenizer, model_rut5


# Тут будет распологаться процессинг
def process(criteria: str, tokenizer, model_rut5):
  inputs = tokenizer(criteria, return_tensors='pt')
  with torch.no_grad():
    hypotheses = model_rut5.generate(**inputs, num_beams=5, max_length=300, length_penalty=2.5, no_repeat_ngram_size=3)
  return tokenizer.decode(hypotheses[0], skip_special_tokens=True)
