import streamlit as st
import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="AIzaSyAz7BUszo_CseQbJDqcm50eMaVCo8mrFIo")
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("AI-Powered Interview Preparation Chatbot")

options = ["Python", "Machine Learning", "Data Science"]
topic = st.selectbox("Select a topic:", options)

if "question" not in st.session_state:
    st.session_state.question = None
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None

def generate_question(topic):
    prompt = f"Generate an interview question about {topic}. Only return the question."
    response = model.generate_content(prompt)
    return response.text

def evaluate_answer(question, user_answer):
    prompt = f"""
    Evaluate the following answer to the interview question: "{question}".

    User's answer: "{user_answer}"

    Provide a score out of 10, feedback on the correctness and completeness of the answer, and areas for improvement.
    Format the output with clear headers like "Score:", "Feedback:", and "Areas for Improvement:".
    """
    response = model.generate_content(prompt)
    return response.text

if st.button("Get Question"):
    st.session_state.question = generate_question(topic)
    st.session_state.user_answer = None  # Reset user answer for new question

if st.session_state.question:
    st.subheader("Question:")
    st.write(st.session_state.question)

    st.subheader("Your Answer:")
    user_answer = st.text_area("Enter your answer here:", value=st.session_state.user_answer or "")
    st.session_state.user_answer = user_answer

    if st.button("Submit Answer"):
        if st.session_state.user_answer:
            evaluation = evaluate_answer(st.session_state.question, st.session_state.user_answer)
            st.subheader("Evaluation:")
            st.write(evaluation)
        else:
            st.warning("Please enter your answer before submitting.")
