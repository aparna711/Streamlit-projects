
"""
4. Automated Code Debugging Helper
Create a Streamlit app where users can input Python code.
The app uses Gemini API to identify and suggest fixes for errors.
Show the corrected code alongside the original input.
"""

import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDynu56ScEkqjTytgKKPwTi4eV-lNeJIUs")
model = genai.GenerativeModel("gemini-1.5-flash")
st.title("Automated Code Debugging Helper")
code = st.text_area("Enter the code to be debugged:")

if st.button("Click here"):
  prompt = f'''Analyze the code {code} entered by user to identify and suggest fixes for errors.
    Show the corrected code alongside the original input
    '''
  response = model.generate_content(prompt)
  st.write(response.text)
