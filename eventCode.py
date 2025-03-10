import streamlit as st
from dataBase import *
import datetime

# Pulling previous events in order to maintain history 
def controlEvent():
    if "events" not in st.session_state:
        st.session_state.events = {}
    events = eventLoadDb()
    for date, users in events.items():
        if date not in st.session_state.events:
            st.session_state.events[date] = {}
        for user, roles in users.items():
            if user not in st.session_state.events[date]:
                st.session_state.events[date][user] = {}
            for role, events_list in roles.items():
                if role not in st.session_state.events[date][user]:
                    st.session_state.events[date][user][role] = events_list

# List of events previously scheduled
    with st.container():
        st.subheader("Scheduled Events")
        for date, users in sorted(events.items()):
            st.write(f"**{date}**")
            for user, roles in users.items():
                for role, event_list in roles.items():
                    for e in event_list:
                        st.write(f"  - **{user}** ({role}): {e}")
                        if st.button(f"Delete Event {e}"):
                            eventDeleteDb(date, user, role, e)
                            st.rerun()
                            st.success(f"Event '{e}' deleted for {user} on {date}")

# Function to add a new event to the system
def addEvent():
    userE = st.text_input("Your Name (Optional)", max_chars=50, placeholder="Enter")
    area = st.text_input("Your Role (Optional)", max_chars=50, placeholder="Enter")
    selected_date = st.date_input("Select a Date", value=datetime.datetime.today())
    event_text = st.text_input("Add Event", placeholder = "Enter Event",)
    if st.button("Add Event"):
        eventAddDb(str(selected_date), userE, area, event_text)
        st.rerun()
        st.success(f"Event added for {selected_date} by {userE, area}")

