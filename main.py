import streamlit as st
from dataBase import *
import sqlite3
import pandas as pd
from quizCode import *
from supportCode import *
from textForDataFacts import *
import datetime
from eventCode import *
from announceCode import *


# Initiaing the databases
initDB()
initAnnouncementDb()
initDiscussionDB()

# Overall UI Formatting 
st.set_page_config( layout= "wide")
st.title('Data Governance at Aflac')
from PIL import Image
st.image(image= Image.open("uiImage.png"))
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(['About us', "Data Governance Role", "DQ and MDM","Quizzes/Games", "Resources", "Calendar", "Announcements","Discussion Board","Support"])

with tab1:
    col1,col2 = st.columns(2)
    with col1:
        st.header("About Us")
        st.image(image= Image.open('datagovImage.png'))



with tab2:
    st.header("Data Governance Team")
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("What is Data Governance?")
        whatDataGov()
    with col2:
        st.subheader("Roles and Responsibilites")
        dataGovRR()

with tab3:
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Practices for Ensuring Data Quality(DQ)")
        dataGovDQ()
    with col2:
        st.subheader("Master Data Management(MDM)")
        dataGovMDM()

with tab4:
    col1,col2 = st.columns(2)
    with col1:
        st.header("Our Quizzes")
        displayQuizzes()

    with col2:
        st.header("Our Game")
        st.button("Game Name")
    
with tab5:
    st.header("Links to Resources")
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Softwares we use")
        st.link_button("Collibra University", "https://university.collibra.com/learn")
        st.link_button("Talebau", "https://www.tableau.com/resources/reference-materials")
    with col2:
        st.subheader("Practice/Learn")
        st.link_button("Aflac History","https://www.aflac.com/about-aflac/our-company/our-history.aspx")
        if st.button("About Aflac"):
            st.image(image= Image.open("aflacChartImage.jpg"))
        st.link_button("Pluralsight", "https://app.pluralsight.com/library/")
        
with tab6:
    col1, col2 = st.columns([1.5, 1])
    with col1:
      st.header("Calendar Event Planner")
      addEvent()
    with col2:
      controlEvent()

with tab7:
    col1, col2 = st.columns([1.5,1])
    with col1:
      addAnnounce()
    with col2:
      listAnnounce()

with tab8:
    st.header("Discussion Board")
    col1,col2 = st.columns(2)
    with col1:
        with st.form("new_post_form"):
            user = st.text_input("Your Name (Optional)", max_chars=50, placeholder="Leave blank for Anonymous")
            role = st.text_input("Your Role (Optional)", max_chars=50, placeholder="Leave blank for General User")
            content = st.text_area("Write your message here...")
            submit = st.form_submit_button("Post")

            if submit:
                if content.strip():  
                    addPost(user, role, content)
                    st.success("Message posted!")
                    st.rerun()
                else:
                    st.warning("Message cannot be empty.")



    with col2:
        st.image(image= Image.open("logo.jpeg"))
        st.subheader(" Recent Posts")
        searchQuery = st.text_input("🔍 Search messages", placeholder="Enter keyword...")
        postsDF = getPosts(searchQuery)

        if not postsDF.empty:
            for _, row in postsDF.iterrows():
                with st.container():
                    st.markdown(f"**{row['user']}** ({row['role']}) 🕒 {row['timestamp']}")
                    st.write(row["content"])
                    if st.button(f" Delete", key=row['id']):
                        deletePost(row['id'])
                        st.warning("Message deleted!")
                        st.rerun()
                    st.markdown("---")
        else:
            st.write("No messages found.")     

with tab9:
    st.header("Support")
    col1,col2 = st.columns([1,5])
    with col1:
        from PIL import Image
        st.image(image= Image.open('supportDuckImage.png'))
    with col2:
        st.subheader("Questions")
        dropdownAnswers()
   