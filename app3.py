'''
3. AI-Based Travel Itinerary Generator
Develop a Streamlit app where users input their travel destination and duration.
Use Gemini API to generate a complete travel itinerary (places to visit, food recommendations, and activities).
Display the results in a structured format.

'''
#AI-Based Travel Itinerary Generator

import streamlit as st
import google.generativeai as genai
genai.configure(api_key ="AIzaSyBW0FGG-5hw41OV-XFniCfkscT3lqIcJ0w")
model = genai.GenerativeModel("gemini-1.5-flash")
st.title(" AI-Based Travel Itinerary Generator ")
destination = st.text_input("Enter the destination")
duration = st.text_input("Duration ")
if st.button("Click here"):
  # prompt =f"""
  #   Generate a complete travel itinerary (places to visit, food recommendations, and activities).
  #   with the details like Destination{destination} and Duration {duration }
  #   Display the results in a structured format
  #   """

  prompt =f"""
     Generate a detailed travel itinerary for a trip to {destination} for {duration}.
        Include:
        - Daily plans with specific places to visit.
        - Food recommendations (local cuisine).
        - Recommended activities.
        - Structure the response in a clear and organized format.
    """

  response= model.generate_content(prompt)
  st.write(response.text)