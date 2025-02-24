import streamlit as st
import datetime
from dataBase import *
from calendarCode import generate_calendar
import sqlite3
import calendar
import pandas as pd
from quizCode import *
from dropdownCodeForSupport import *


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
        st.write("")
        st.write("Data governance is the systematic management of an organization's data assets to ensure data quality, security, privacy, compliance, and usability while aligning with business objectives.")
        st.write("It has become increasingly important as organizations handle large volumes of data from various sources such as databases and policies")
        st.write("Key Components include: ")
        st.write("""
    - Data Quality:
        - Ensure accuracy, consistency, and reliability of data
        - Prevent poor outcomes from bad data

    - Security and Privacy:
        - Implement access controls to protect data
        - Use encryption 
        - Apply data masking (e.g., showing only the last four digits of credit card numbers)
        - Follow proper data disposal procedures

    - Compliance:
        - Ensure data handling adheres to relevant regulations
        - Reduce legal and regulatory risks

    - Usability:
        - Maintain data catalogs to document data availability and ownership
        - Use data dictionaries to define tables, columns, and measures
        - Track data lineage to trace the source of data
        - Implement metadata management tools for better data organization
    """)
    with col2:
        st.subheader("Roles and Responsibilites")
        st.write("""**Roles and Responsibilities in Data Governance:**
                
- **Data Governance Committee**:
  - Plans, implements, and manages the data governance program.
  - Develops policies and sets the strategic direction for data governance.
  - Advocates and communicates data governance initiatives across the organization.
  - Allocates resources (human and monetary) and monitors progress.
  - Manages change and risk related to data governance.
  - Composed of:
    - Data Governance Director (leader)
    - Data Stewards
    - Department Representatives (e.g., IT, Legal)
    - Data Governance Coordinator
    - Data Governance Analyst/Architect

- **Data Stewards**:
  - Responsible for applying data governance within different business units (e.g., sales, HR, finance).
  - Manage data domains (e.g., orders, leads, customers) and ensure proper data handling and policy application.

- **Data Owners**:
  - Own specific datasets and are responsible for supervising policies, approving security changes, and making decisions for their datasets.
  - Collaborate with the data governance committee to ensure policies are followed.

- **Other Roles Impacted by Data Governance**:
  - **IT Personnel**: Handle general security, storage, and data retention.
  - **Database Administrators**: Implement database-specific security measures such as encryption and masking policies.
  - **Business Knowledge Workers**: Interact with data regularly, ensuring its secure handling and providing feedback on data governance policies.""")

with tab3:
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Practices for Ensuring Data Quality(DQ)")
        st.write("""
                 -- **Data Profiling**: 
  - Analyzes data to identify characteristics, patterns, and anomalies (e.g., duplication, inconsistencies).
  - Helps understand data and ensures alignment with expectations for improvement.

- **Data Validation**: 
  - Ensures data accuracy and completeness at the entry point (manual or automated).
  - Prevents errors from entering the system early.

- **Data Cleansing**: 
  - Corrects errors and removes duplicates.
  - Involves merging records or updating outdated information.

- **Data Completeness**: 
  - Addresses missing data by eliminating, annotating, or seeking additional information to maintain accuracy.

- **Data Documentation**: 
  - Includes data dictionaries, metadata, and lineage tracking.
  - Ensures clarity and helps resolve issues related to data origin and transformation.

- **Data Quality Monitoring**: 
  - Continuously evaluates data for accuracy, completeness, and consistency.
  - Uses automated tools to track anomalies and trends over time.
- **Data Governance**: 
  - Defines ownership, access permissions, and data management standards.
  - Ensures compliance, integrity, and security, especially in sensitive fields like healthcare.

**Impact of Poor Data Quality**:

- **Financial Losses**: 
  - Examples: 2008 financial crisis, a 2015 bank loss of $2.8 billion, a USA airline losing $1 billion due to overbooking.

- **Reputation Damage**: 
  - Inaccurate data can lead to bad decision-making, lost revenue, and damaged customer relationships.

- **Global Loss**: 
  - Poor data quality costs businesses an average of $15 million per year, impacting morale and opportunities.""")
    with col2:
        st.subheader("Master Data Management(MDM)")
        st.write("""

- **Best Practices**:
  - **Data Integration**: Combines data from different sources to ensure consistency.
  - **Data Stewardship**: Assigns responsibility for maintaining data quality and compliance.
  - **Data Quality Control**: Uses validation, cleansing, and monitoring to ensure accurate data.
  - **Data Governance**: Sets policies and rules for data management and access control.
  - **Master Data Modeling**: Standardizes key business data to align processes and systems.
  - **Data Security and Compliance**: Protects sensitive data and ensures regulatory compliance.

- **Impact of Poor MDM**:
  - **Operational Inefficiency**: Causes delays and redundant work.
  - **Increased Costs**: Leads to higher operational costs and resources spent fixing errors.
  - **Poor Customer Experience**: Affects service quality and customer retention.
  - **Regulatory Risks**: Non-compliance can result in legal consequences.
  - **Damaged Reputation**: Inconsistent data harms brand trust and customer loyalty.""")

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
                            if st.button(f"Delete Event for {user} on {date}", key=f"delete_{date}_{user}_{role}_{e}"):
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
            if st.button(f"Delete {"Above"}"):
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
   