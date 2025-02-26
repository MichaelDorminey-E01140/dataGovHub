import streamlit as st

# Function to reset quiz
def restartQuiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.feedback = None

# Function to display feedback
def feedbackFragment():
    if st.session_state.feedback:
        st.write(st.session_state.feedback)

# Function to display score
def scoreFragment():
    st.write(f"Score: {st.session_state.score}/{len(st.session_state.questions)}")

# Function to display the question
def questionFragment():
    q_index = st.session_state.current_question
    if q_index < len(st.session_state.questions):
        questionData = st.session_state.questions[q_index]
        st.subheader(questionData["question"])
        answer = st.radio("Choose your answer:", questionData["options"], key=f"q_{q_index}")

        if st.button("Submit Answer"):
            if answer == questionData["answer"]:
                st.session_state.score += 1
                st.session_state.feedback = " Correct!"
            else:
                st.session_state.feedback = f" Incorrect! The correct answer is {questionData['answer']}."
            st.session_state.current_question += 1
            st.rerun()  # Trigger rerun to move to next question

        feedbackFragment()
    else:
        st.subheader(" Quiz Finished!")
        st.write(f"Your final score is **{st.session_state.score}/{len(st.session_state.questions)}**.")

# Main logic for selecting quizzes
def displayQuizzes():
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = None

    if st.button("Aflac Quiz"):
        st.session_state.quiz_started = "Aflac"
        restartQuiz()  # Reset for the Aflac quiz
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
        restartQuiz()  # Restart quiz state

    if st.button("Data Governance Quiz"):
        st.session_state.quiz_started = "Data Governance"
        restartQuiz()  # Reset for the Data Governance quiz
        st.session_state.questions = [
            {"question": "What is Data Governance?", "options": ["Managing data security and compliance", "Creating new databases", "Hacking into secured networks", "Developing Data For Companies"], "answer": "Managing data security and compliance"},
            {"question": "What is the main goal of Data Governance?", "options": ["To secure data storage", "To define policies for data usage", "To encrypt all files"], "answer": "To define policies for data usage"},
            {"question": "Which role is responsible for enforcing data governance policies?", "options": ["CIO", "Data Steward", "Software Engineer", "CEO"], "answer": "Data Steward"},
            {"question": "Which of the following is not a component of Data Governance?", "options": ["Data Quality","Data Cleansing","Data Stewartship","Data Guessing"], "answer":"Data Guessing"},
            {"question": "What does the term Data Stewartship refer to in Data Governance ?", "options": ["Collecting Customer Data without Permission","Process of Deleting Outdated Data","Framework for Data Privacy","Responsibility for Managing and Ensuring Data Integrity"], "answer":"Responsibility for Managing and Ensuring Data Integrity"},

        ]
        restartQuiz()  # Restart quiz state
    # Display quiz if started
    if st.session_state.quiz_started:
        questionFragment()  # Display current question