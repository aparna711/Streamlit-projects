"""
1.AI-Powered Resume Generator
Build a Streamlit app that takes user input (name, skills, experience, and education) and generates a well-structured resume using the Gemini API.

"""

#AI-Powered Resume Generator

import streamlit as st
st.title("AI-Powered Resume Generator")



import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key=st.secrets['GOOGLE_API_KEY']['GOOGLE_API_KEY']) # Replace with your actual API key 
model = genai.GenerativeModel("gemini-1.5-flash") # Load Model

# Get user input
name = st.text_input("Enter your Full name : ")
skills = st.text_area("Enter your skills (comma-separated)  : ")
education = st.text_area("Enter your education : (Degree_name    College name   CGPA|Passed Out Year. , write one degree per line)")
projects = st.text_area("Enter details of project: (Project name, Technology used and its Features or Your Role) ")
experience = st.text_area("Enter the experience : ")
achievements =st.text_area("Give achievements : ")

if st.button("Generate your Resume"):
  # Construct the prompt for Gemini
  prompt = f"""
  Create a AI-Powered Resume Generator using the following details written in the resume accepted from user:

    Full Name: {name},
    Skills: {skills},
    Projects :{projects}
    Experience:{experience},
    Education:  {education},
    Achievements : {achievements},
    Make the resume in a proper structure with spacing and headers.
  """

  # Generate vacation plan using Gemini
  response = model.generate_content(prompt)

  # Print the generated plan
  print(response.text)
  st.write(response.text)

