import streamlit as st
import sklearn
import helper
import pickle
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

st.title("Sentiment Analysis App Using ML")

text = st.text_input("Please enter your review")
state = st.button("predict")

token = helper.preprocessing_step(text)

vectorized_data = vectorizer.transform([token])

prediction = model.predict(vectorized_data)


if state : 
  st.text(prediction)