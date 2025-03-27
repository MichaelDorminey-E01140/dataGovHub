import streamlit as st
from dataBase import *
from quizCode import *
from supportCode import *
from textForDataFacts import *
from eventCode import *
from announceCode import *
from discussionCode import *
from PIL import Image
from gameCode import *
st.set_page_config( layout= "wide")


# Initiaing the databases
initDB()
initAnnouncementDb()
initDiscussionDB()
initGameDB()
initQuizDB()
# Overall UI Formatting 
st.title('DataGov Hub')
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
        st.write("Basic example showing simple few lines of data")
        st.write("Using the dropdowns the objective of the game is to face challenges with data cleaning. You will use the dropdowns to fill blank data with unknown, deleting rows that contain errors, and deleting duplicate rows in order to have the best data possible. ")
        st.write("There is a leaderboard which will show the highest scores in the quickest time")
        st.write("-Missing Values")
        st.write("-Inconsistent Data")
        st.write("-Errors")
        st.write("This sample data will provide a realistic scenario of what data cleaning and analysis looks like. It will also help practice data cleaning techniques which are useful when identifiying data")
        startingGame()
        
# Tab which has links for resources     
with tab5:
    st.header("Links to Resources")
    col1,col2 = st.columns(2)

    with col1:
        st.subheader("Softwares we use")
        st.link_button("Tableau", "https://www.tableau.com/resources/reference-materials")
        st.link_button("Collibra", "https://aflac.collibra.com/apps/")


    with col2:
        st.subheader("Practice/Learn")
        st.link_button("Pluralsight", "https://app.pluralsight.com/library/")
        st.link_button("Aflac History","https://www.aflac.com/about-aflac/our-company/our-history.aspx")
        st.link_button("Collibra University", "https://university.collibra.com/learn")

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
   