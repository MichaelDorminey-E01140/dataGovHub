import streamlit as st
from dataBase import *
import sqlite3
import pandas as pd
import numpy as np
import random
import time
from quizCode import *
from supportCode import *
from textForDataFacts import *
import datetime
from eventCode import *
from announceCode import *
from discussionCode import *
from PIL import Image
st.set_page_config( layout= "wide")



# Initiaing the databases
initDB()
initAnnouncementDb()
initDiscussionDB()
initGameDB()

# Overall UI Formatting 
st.title('Data Governance at Aflac')
st.image(image= Image.open("uiImage.png"))
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(['About us', "Data Governance Roles", "DQ and MDM","Quizzes/Games", "Resources", "Calendar", "Announcements","Discussion Board","Support"])

# About Us Tab covering Data Governance introduction
with tab1:
    col1,col2 = st.columns([1,2])
    with col1:
        st.header("About Us")
        st.write("The Data Enablement Center (DEC) is the single source of truth of all our data governance and stewardship activities. This platform will be used to manage business terms, metrics, and reports along with a maintained data catalog. The DEC will support our data stewards in their day-to-day activities. Data Enablement is a vital step toward achieving our vision of consistent, trusted and high-quality data throughout the enterprise.")

    with col2:
        st.image(image= Image.open('datagovImage.png'))

# Tab covering what Data Governance does
with tab2:
    st.header("Data Governance Team")
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("What is Data Governance?")
        whatDataGov()
    with col2:
        st.subheader("Roles and Responsibilites")
        dataGovRR()

# Tab covering the two main ideas
with tab3:
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Practices for Ensuring Data Quality(DQ)")
        dataGovDQ()
    with col2:
        st.subheader("Master Data Management(MDM)")
        dataGovMDM()

# Tab with quizzes and a game
with tab4:
    col1,col2 = st.columns(2)
    with col1:
        st.header("Our Quizzes")
        displayQuizzes()

    with col2:
        st.header("Our Game")
        st.write('''This game will cover some things Data Governance typically deals with on a day-to-day basis such as: ''')
        st.write("-Missing Values")
        st.write("-Inconsistent Data")
        st.write("-Errors")
        st.write("This sample data will provide a realistic scenario of what data cleaning and analysis looks like. It will also help practice data cleaning techniques which are useful when identifiying data")
        st.button("Data Cleaning Game")
        playerName = st.text_input("Enter your name: ","")
        if playerName: 
            addPlayer(playerName)
            st.write(f"Welcome, {playerName}! Today you will be helping me with cleaning messy data of cafe sales.")
            st.write("Bob the owner of the store wants an update of what is selling the best. This will help him calculate of what the future of his cafe shop is and which products he should remove.")
            st.write("-You have options to play timed or untimed.")
            st.write("-Score will be kept based on each correct solution and points will be deducted for wrong choices.")
            st.write("-This Data is provided free by Kaggle.")
            filePath = "cafeSales.csv"
            st.write("Randomly selected Raw Data")
            subsetSize = 50
            fullDF = pd.read_csv(filePath)

            df = fullDF.sample (n = subsetSize, random_state = random.randint(1,1000))
            st.dataframe(df)
            missingValues = df.isnull().sum().sum()
            duplicateRows = df.duplicated().sum()
            incorrectTypes = 0
                
    
            
            if "Price" in df.columns:
                incorrrectTypes = df['Item'].apply(lambda x: isinstance(x,str) and not x.isdigit()).sum()
            if "Item" in df.columns:
                df["Item"] = df["Item"].fillna("Unknown").astype(str)
            st.write("Data Issues detected")
            st.write(f"Missing Values: {missingValues}")
            st.write(f'Duplicate Rowsz: {duplicateRows}')
            if st.button("Get a Hint"):
                hints = [
                    "Consider filling missing values with 'Unknown'",
                    "Try removing duplicate rows to avoid redundancy",
                    "For the 'Price', 'Quantity', 'Total Spent', and 'Transaction Date' ensure it is only numerics"
                ]
                st.write(f"Hint: {random.choice(hints)}")
            if st.button("Remove Duplicates"):
                df = df.drop_duplicates()
                st.success("Duplicates Removed!")
            if st.button("Fill Missing Values with 'Unknown'"):
                df = df.fillna("Unknown")
                st.success("Missing values filled!")
            st.write("Cleaned Data")
            st.dataframe(df)
            startTime = time.time()
            score = 100 - (missingValues + duplicateRows + incorrectTypes)
            score = max(score,0)
            timeTaken = round(time.time() - startTime, 2)
            updatePlayerData(playerName,score,timeTaken)
            st.write(f"Your Score: {score}")
            st.write(f"Time Taken **{timeTaken} seconds")
            st.write("Leaderboard")
            if playerLeaderboard(playerName,score, timeTaken):
                st.table(pd.DataFrame(playerLeaderboard, columns = ["Player", "Score", "Time Taken"]))
            else:
                st.write("No Scores Yet. Be the first player!")



# Tab which has links for resources     
with tab5:
    st.header("Links to Resources")
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Softwares we use")
        st.link_button("Collibra University", "https://university.collibra.com/learn")
        st.link_button("Tableau", "https://www.tableau.com/resources/reference-materials")
    with col2:
        st.subheader("Practice/Learn")
        st.link_button("Pluralsight", "https://app.pluralsight.com/library/")
        st.link_button("Aflac History","https://www.aflac.com/about-aflac/our-company/our-history.aspx")
        if st.button("About Aflac"):
            st.image(image= Image.open("chartImage.jpg"))

# Tab used to plan events between team members         
with tab6:
    col1, col2 = st.columns([1.5, 1])
    with col1:
      st.header("Calendar Event Planner")
      addEvent()
    with col2:
      controlEvent()

#Tab used for announcments between team members
with tab7:
    col1, col2 = st.columns([1.5,1])
    with col1:
      addAnnounce()
    with col2:
      listAnnounce()

# Tab used for discussion between team members 
with tab8:
    st.header("Discussion Board")
    col1,col2 = st.columns(2)
    with col1:
        createDiscussionPost()
    with col2:
        managingDiscussionPost()     

# Tab used for support on common questions
with tab9:
    st.header("Support")
    col1,col2 = st.columns([1,5])
    with col1:
        st.image(image= Image.open('supportDuckImage.png'))
    with col2:
        st.subheader("Questions")
        dropdownAnswers()
   