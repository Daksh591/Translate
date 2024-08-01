from googletrans import Translator
import streamlit as st
import pyttsx3
engine = pyttsx3.init()
st.subheader("Translation")
st.title("Translation")
a = st.text_input("Enter your destination Language: ","Hindi")
b = st.text_input("Enter your Text: ")
c = st.text_input("Enter the source language: ","English")
button = st.button("Know your answer")
if button:
    translate = Translator()
    out = translate.translate(b, a, c)
    result = out.text
    st.text(f"Translate {c} to {a} is {result}")

    engine.say(out.pronunciation)
    engine.runAndWait()

