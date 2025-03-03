"""
2. Sentiment Analysis of User Input
Create a Streamlit app where a user enters text, and the app analyzes its sentiment (positive, negative, or neutral).
Use Gemini API to classify the sentiment and display the result with a confidence score.

"""
import streamlit as st
st.title("Sentiment Analyzer")
text = st.text_area("Enter the text: ")
import google.generativeai as genai


genai.configure(api_key="AIzaSyBW0FGG-5hw41OV-XFniCfkscT3lqIcJ0w")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-1.5-flash") # Load Model

if st.button("Click here"):
  prompt = f'''   
    Analyze the sentiment of the following text and classify it as positive, negative, or neutral.
    Provide a confidence score between 0 and 1.
    Explain the reasoning behind your sentiment classification.

    Text: {text}

    Output format:
    Sentiment: [Sentiment]
    Confidence Score: [Confidence Score]
    Reason: [Reason for the sentiment and Confidence Score]
'''

  response = model.generate_content(prompt)
  # Extract sentiment and confidence score
  sentiment = None
  confidence_score = None
  reason  = None
  response_text =response.text
  lines = response_text.split('\n')
  for line in lines:
        if "Sentiment:" in line:
          sentiment = line.split("Sentiment:")[1].strip()
        if "Confidence Score:" in line:
          try:
            confidence_score = float(line.split("Confidence Score:")[1].strip())
          except ValueError:
            confidence_score = None
        if "Reason:" in line:
             reason = line.split("Reason:")[1].strip()

  st.subheader("Sentiment: ")
  st.write(sentiment)
  st.subheader("Reason:")
  st.write("Reason:",reason)

  st.subheader("Confidence Score:")
  st.write(confidence_score)
   
  st.progress(confidence_score)
  #st.slider("Confidence", 0.0, 1.0, confidence_score, disabled=True)
  
  #st.metric(label="Confidence", value=f"{confidence_score:.2f}")
#I just received the best news ever! I got the job offer I've been waiting for. I'm so excited!"\
#My flight was canceled, and I lost my luggage. This has been a terrible travel experience
#The meeting will be held on Tuesday at 10 AM in the conference room

#The food was delicious, but the service was incredibly slow and rude