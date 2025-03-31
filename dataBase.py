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
    eventSaveDb(str(date), user or " ", role or "User", event)


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

# Save event data to database
def eventSaveDb(date, user, role, event):
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("INSERT INTO events (date, user, role, event) VALUES (?, ?, ?, ?)", (date, user, role, event))
    conn.commit()
    conn.close()

#Delete event data from database
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

# Delete announcements from database
def announcementDeleteDb(id):
    conn = sqlite3.connect("announcements.db")
    c = conn.cursor()
    c.execute("DELETE FROM announcements WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    st.rerun()


# Initialize Discussion Database
def initDiscussionDB():
    conn = sqlite3.connect("discussion.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user TEXT DEFAULT '',
                    role TEXT DEFAULT 'User',
                    content TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    likes INTEGER DEFAULT 0,
                    dislikes INTEGER DEFAULT 0
                )''')

#Second database used for undo function by tracking last action performed
    c.execute(''' CREATE TABLE IF NOT EXISTS lastAction(
                    postID INTEGER PRIMARY KEY,
                    action TEXT CHECK(action IN ('likes', 'dislikes')),
                    FOREIGN KEY (postId) REFERENCES posts(id) ON DELETE CASCADE
                    )''')
    conn.commit()
    conn.close()

# Add Posts to Discussion
def addPost(user, role, content):
    conn = sqlite3.connect("discussion.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (user, role, content, likes, dislikes) VALUES (?, ?, ?, ?, ?)", 
                   (user or "", role or "User", content, 0, 0))
    conn.commit()
    conn.close()

# Retrieve posts (with optional search)
def getPosts(searchQuery=""):
    conn = sqlite3.connect("discussion.db")
    if searchQuery:
        query = "SELECT id, user, role, content, timestamp, likes, dislikes FROM posts WHERE content LIKE ? ORDER BY timestamp DESC"
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

# Update Like/Dislike Count
def updateReaction(postID, like=False, dislike=False, undo=False):
    conn = sqlite3.connect("discussion.db")
    cursor = conn.cursor()
    if undo:
        cursor.execute("SELECT action FROM lastAction WHERE postID = ?",(postID,))
        lastAction = cursor.fetchone()
        if lastAction:
            lastAction = lastAction[0]
            if lastAction == "like":
                cursor.execute("UPDATE posts SET likes = likes - 1 WHERE id = ? AND likes > 0",(postID,))
            elif lastAction == "dislike":
                cursor.execute("UPDATE posts SET dislikes = dislikes - 1 WHERE id = ? AND dislikes > 0",(postID,)) 
            cursor.execute("DELETE FROM lastAction WHERE postID = ?",(postID,)) 
    else:
        cursor.execute("SELECT action FROM lastAction WHERE postID = ?", (postID,))
        existingAction = cursor.fetchone()
        if not existingAction:
            if like:
                cursor.execute("UPDATE posts SET likes = likes + 1 WHERE id = ?", (postID,))
                cursor.execute("INSERT INTO lastAction(postID, action) VALUES(?, ?)", (postID, "like"))
            if dislike:
                cursor.execute("UPDATE posts SET dislikes = dislikes + 1 WHERE id = ?", (postID,))
                cursor.execute("INSERT INTO lastAction(postID, action) VALUES(?, ?)", (postID, "dislike"))

    conn.commit()
    conn.close()


# Initialize Database for Data Cleaning Game
def initGameDB(): 
    conn = sqlite3.connect("game.db")
    c = conn.cursor()
    c.execute('''Create TABLE IF NOT EXISTS players(
                    name TEXT NOT NULL,
                    score INTEGER DEFAULT 0)
                   ''')
    conn.commit()
    conn.close()
# Updating player data based on game performance
def updateGamePlayerData(name, score):
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO players (name, score) VALUES (?,?,?)", (name,score))
    conn.commit()
    conn.close()
# Pulling player data     
def getGameLeaderboard():
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute ('''SELECT name, score 
                        FROM players 
                        ORDER BY score DESC
                        LIMIT 10''')
    gameLeaderboard = cursor.fetchall()
    conn.close()
    return gameLeaderboard

# Initialize Database for Quizzes
def initQuizDB(): 
    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    c.execute('''Create TABLE IF NOT EXISTS quizTakers (
                    playerName TEXT NOT NULL,
                    score INTEGER DEFAULT 0,
                    timeTaken REAL)
                   ''')
    conn.commit()
    conn.close()    
# Update player data based on game performance
def updateQuizPlayerData(playerName, score, timeTaken):
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO quizTakers (playerName, score, timeTaken) VALUES (?,?,?)", (playerName,score,timeTaken))
    conn.commit() 
    conn.close()
# Pulling quiz data 
def getQuizLeaderboard():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute ('''SELECT playerName, score, timeTaken 
                        FROM quizTakers 
                        ORDER BY score DESC, timeTaken ASC 
                        LIMIT 10''')
    quizLeaderboard = cursor.fetchall()
    conn.close()
    return quizLeaderboard

def clearGameDB():
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM players;")
    conn.commit()
    conn.close()
    st.write("Database cleared")

def clearQuizDB():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM quizTakers;")
    conn.commit()
    conn.close()
    st.write("Database cleared")





