import streamlit as st
from dataBase import *

# Add an announcement for users to see
def addAnnounce():
    st.header("Add Announcements")
    userA = st.text_input("Your Name (Not REQ )", max_chars=50, placeholder= "Leave blank for Anonymous")
    positionA = st.text_input("Your Role (Not REQ)", max_chars=50, placeholder="Leave blank for General User")
    with st.expander("Add Announcement"):
        new_announcement = st.text_area("Enter your announcement")
        if st.button("Add Announcement") and userA and positionA and new_announcement:
            announcementSaveDb(new_announcement, userA, positionA)
            st.success("Announcement added successfully")
            
# List all announcements in the system
def listAnnounce():
    st.subheader("Announcements")
    announcements = announcementLoadDb()
    for ann in announcements:
        ann_id, announcement, userA, positionA = ann
        st.write(f"{announcement}- by {userA} ({positionA})")
        st.text("------")
        if st.button(f"Delete { announcement}"):
            announcementDeleteDb(ann_id)