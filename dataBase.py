import sqlite3
import streamlit as st
import pandas as pd

# Database to save details of added events for the calendar
def initDB():
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS events (
                    date TEXT,
                    user TEXT,
                    role TEXT,
                    event TEXT)''')
    conn.commit()
    conn.close()

# Add event data to database
def eventAddDb(date, user, role, event):
    eventSaveDb(str(date), user or "Anonymous", role or "General User", event)


# Load event data from database
def eventLoadDb():
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("SELECT date, user, role, event FROM events")
    rows = c.fetchall()
    events = {}
    for date, user, role, event in rows:
        if date not in events:
            events[date] = {}
        if user not in events[date]:
            events[date][user] = {}
        if role not in events[date][user]:
            events[date][user][role] = []
        events[date][user][role].append(event)
    conn.close()
    return events

# Save data to database
def eventSaveDb(date, user, role, event):
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("INSERT INTO events (date, user, role, event) VALUES (?, ?, ?, ?)", (date, user, role, event))
    conn.commit()
    conn.close()

#Delete data from database
def eventDeleteDb(date, user, role, event):
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("DELETE FROM events WHERE date = ? AND user = ? AND role = ? AND event = ?", (date, user, role, event))
    conn.commit()
    conn.close()

# Database to add and remove announcements
def initAnnouncementDb():
    conn = sqlite3.connect("announcements.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS announcements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    announcement TEXT,
                    user TEXT,
                    position TEXT)''')
    conn.commit()
    conn.close()

# Save Announcements to database
def announcementSaveDb(announcement, user, position):
    conn = sqlite3.connect("announcements.db")
    c = conn.cursor()
    c.execute("INSERT INTO announcements (announcement, user, position) VALUES (?, ?, ?)", 
              (announcement, user, position))
    conn.commit()
    conn.close()
# Load Announcements from database
def announcementLoadDb():
    conn = sqlite3.connect("announcements.db")
    c = conn.cursor()
    c.execute("SELECT id, announcement, user, position FROM announcements")
    rows = c.fetchall()
    conn.close()
    return rows

#Delete announcements from database
def announcementDeleteDb(id):
    conn = sqlite3.connect("announcements.db")
    c = conn.cursor()
    c.execute("DELETE FROM announcements WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    st.rerun()

def initDiscussionDB():
    conn = sqlite3.connect("discussion.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user TEXT DEFAULT 'Anonymous',
                    role TEXT DEFAULT 'General User',
                    content TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
                ''')
    conn.commit()
    conn.close()

def addPost(user, role, content):
    conn = sqlite3.connect("discussion.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (user, role, content) VALUES (?, ?, ?)", 
                   (user or "Anonymous", role or "General User", content))
    conn.commit()
    conn.close()

# Retrieve posts (with optional search)
def getPosts(searchQuery=""):
    conn = sqlite3.connect("discussion.db")
    if searchQuery:
        query = "SELECT * FROM posts WHERE content LIKE ? ORDER BY timestamp DESC"
        df = pd.read_sql_query(query, conn, params=('%' + searchQuery + '%',))
    else:
        df = pd.read_sql_query("SELECT * FROM posts ORDER BY timestamp DESC", conn)
    conn.close()
    return df

# Delete a post
def deletePost(postID):
    conn = sqlite3.connect("discussion.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM posts WHERE id = ?", (postID,))
    conn.commit()
    conn.close()