import streamlit as st

# Function to reset quiz
def restart_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.feedback = None

# Function to display feedback
def feedback_fragment():
    if st.session_state.feedback:
        st.write(st.session_state.feedback)

# Function to display score
def score_fragment():
    st.write(f"Score: {st.session_state.score}/{len(st.session_state.questions)}")

# Function to display the question
def question_fragment():
    q_index = st.session_state.current_question
    if q_index < len(st.session_state.questions):
        question_data = st.session_state.questions[q_index]
        st.subheader(question_data["question"])

        # Use unique key for radio button to prevent persistence issues
        answer = st.radio("Choose your answer:", question_data["options"], key=f"q_{q_index}")

        if st.button("Submit Answer"):
            if answer == question_data["answer"]:
                st.session_state.score += 1
                st.session_state.feedback = " Correct!"
            else:
                st.session_state.feedback = f" Incorrect! The correct answer is {question_data['answer']}."
            
            st.session_state.current_question += 1
            st.rerun()  # Trigger rerun to move to next question

        feedback_fragment()

        if st.session_state.current_question < len(st.session_state.questions):
            st.button("Next Question", on_click=lambda: None)  # Placeholder button to move to the next question
    else:
        st.subheader("🎉 Quiz Finished!")
        st.write(f"Your final score is **{st.session_state.score}/{len(st.session_state.questions)}**.")

# Main logic for selecting quizzes
def display_quizzes():
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = None

    if st.button("Aflac Quiz"):
        st.session_state.quiz_started = "Aflac"
        restart_quiz()  # Reset for the Aflac quiz
        st.session_state.questions = [
            {"question": "What year was Aflac founded?", "options": ["1965", "1954", "1955", "1963"], "answer": "1955"},
            {"question": "What year did Aflac launch its first commercial?", "options": ["2000", "1993", "1955", "1988"], "answer": "2000"},
            {"question": "What Aflac policy was introduced in 1985?", "options": ["Accident Policy", "Cancer Policy", "Life Insurance Policy", "Dental and Vision Policy"], "answer": "Accident Policy"},
            {"question": "Who was named president of Aflac in 2023?", "options": ["Teresa White", "Virgil Miller", "Dan Amos", "Audrey Tillman"], "answer": "Virgil Miller"},
            {"question": "What year did Aflac change its logo to include the Aflac Duck?", "options": ["2002", "2003", "2001", "2005"], "answer": "2005"},
            {"question": "What was the original product line at Aflac?", "options":["Cancer Policies", "Life Insurance Policies", "Dental and Vision Policies", "Accident Policies"], "answer": "Life Insurance Policies"},
            {"question": "Where is Aflac Headquarters located in the United States?", "options":["Georgia", "New York", "California", "Michigan"], "answer": "Georgia"},
            {"question": "What was introduced in 1996 to help revolutionize the policy application process for Aflac?", "options": ["Insurance Cards", "New Website", "SmartApp", "Process Developer"], "answer": "SmartApp"},
        ]
        restart_quiz()  # Restart quiz state

    if st.button("Data Governance Quiz"):
        st.session_state.quiz_started = "Data Governance"
        restart_quiz()  # Reset for the Data Governance quiz
        st.session_state.questions = [
            {"question": "What is Data Governance?", "options": ["Managing data security and compliance", "Creating new databases", "Hacking into secured networks"], "answer": "Managing data security and compliance"},
            {"question": "Which regulation enforces data privacy in Europe?", "options": ["GDPR", "CCPA", "HIPAA"], "answer": "GDPR"},
            {"question": "What is the main goal of Data Governance?", "options": ["To secure data storage", "To define policies for data usage", "To encrypt all files"], "answer": "To define policies for data usage"},
            {"question": "Which role is responsible for enforcing data governance policies?", "options": ["CIO", "Data Steward", "Software Engineer", "CEO"], "answer": "Data Steward"},
        ]
        restart_quiz()  # Restart quiz state

    # Display quiz if started
    if st.session_state.quiz_started:
        question_fragment()  # Display current question