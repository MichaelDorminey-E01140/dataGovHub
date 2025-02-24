import streamlit as st
import datetime
from dataBase import *
from calendarCode import generate_calendar
import sqlite3
import calendar
import pandas as pd
from quizCode import *
from dropdownCodeForSupport import *
from textForDataFacts import *


# Initiaing the databases
init_db()
init_announcements_db()

# Pulling data from past uses 
if "events" not in st.session_state:
    st.session_state.events = {}
events = load_events()
for date, users in events.items():
    if date not in st.session_state.events:
        st.session_state.events[date] = {}
    for user, roles in users.items():
        if user not in st.session_state.events[date]:
            st.session_state.events[date][user] = {}
        for role, events_list in roles.items():
            if role not in st.session_state.events[date][user]:
                st.session_state.events[date][user][role] = events_list

# UI Formatting Begins
st.title('Data Governance at Aflac')
from PIL import Image
st.image(image= Image.open("favicon-128.png"))
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(['About us', "Data Governance Role", "DQ and MDM","Quizzes/Games", "Resources", "Calendar", "Announcements","Discussion Board","Support"])
with tab1:
    st.header("Our Company")
    st.image(image= Image.open('chart.jpg'))
with tab2:
    st.header("Data Governance Team")
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("What is Data Governance?")
        whatDataGov()
    with col2:
        st.subheader("Roles and Responsibilites")
        DataGovRR()
with tab3:
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Practices for Ensuring Data Quality(DQ)")
        DataGovDQ()
    with col2:
        st.subheader("Master Data Management(MDM)")
        DataGovMDM()
with tab4:
    col1,col2 = st.columns(2)
    with col1:
        st.header("Our Quizzes")
        display_quizzes()

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
        st.link_button("Pluralsight", "https://app.pluralsight.com/library/")
        
with tab6:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("Calendar")
        with st.sidebar:
            st.header("Calendar Settings for Tab 5")
            year = st.number_input("Select Year", min_value=1900, max_value=2100, value=datetime.datetime.today().year)
            month = st.selectbox("Select Month", list(calendar.month_name[1:]))
            month_num = list(calendar.month_name).index(month)
        
# Calendar for viewing purpose is pulled from class and it moves on the the user entering data to add to the schedule 
    with col1:
        st.subheader(f"{month} {year}")
        st.dataframe(generate_calendar(year, month_num,events).set_index(pd.Index([""] * len(generate_calendar(year,month_num,events)))), height=250, width=395)
        user = st.text_input("Enter your name")
        area = st.text_input("Enter the area you work in")
        selected_date = st.date_input("Select a Date", value=datetime.datetime.today())
        event_text = st.text_input("Add Event")
        if st.button("Save Event") and user:
            add_event(str(selected_date), user, area, event_text)
            st.rerun()
            st.success(f"Event added for {selected_date} by {user, area}")
    with col2:
        with st.container():
            st.subheader("Scheduled Events")
            for date, users in sorted(events.items()):
                st.write(f"**{date}**")
                for user, roles in users.items():
                    for role, event_list in roles.items():
                        for e in event_list:
                            st.write(f"  - **{user}** ({role}): {e}")
                            if st.button(f"Delete Event {e}"):
                                delete_event(date, user, role, e)
                                st.success(f"Event '{e}' deleted for {user} on {date} Reload to See Updates")

with tab7:
    col1, col2 = st.columns([2,1])
    with col1:
        st.header("Add Announcements")
        userA = st.text_input("Enter your Name")
        positionA = st.text_input("Enter your Position")
        with st.expander("Add Announcement"):
            new_announcement = st.text_area("Enter your announcement")
            if st.button("Add Announcement") and userA and positionA and new_announcement:
                save_announcement(new_announcement, userA, positionA)
                st.success("Announcement added successfully")
    with col2:
        st.subheader("Announcements")
        announcements = load_announcements()
        for ann in announcements:
            ann_id, announcement, userA, positionA = ann
            st.write(f"{announcement}- by {userA} ({positionA})")
            st.text("------")
            if st.button(f"Delete { announcement}"):
                delete_announcement(ann_id)
    
with tab8:
    st.header("Discussion Board")     
with tab9:
    st.header("Support")
    col1,col2 = st.columns([1,5])

    with col1:
        from PIL import Image
        st.image(image= Image.open('duck.png'))
    with col2:
        st.subheader("Questions")
        dropdownAnswers()
   