import sqlite3

# Database to save details of added events for the calendar
def init_db():
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS events (
                    date TEXT,
                    user TEXT,
                    role TEXT,
                    event TEXT)''')
    conn.commit()
    conn.close()
def add_event(date, user, role, event):
    save_event(str(date), user, role, event)
    
def load_events():
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

def save_event(date, user, role, event):
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("INSERT INTO events (date, user, role, event) VALUES (?, ?, ?, ?)", (date, user, role, event))
    conn.commit()
    conn.close()

def delete_event(date, user, role, event):
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("DELETE FROM events WHERE date = ? AND user = ? AND role = ? AND event = ?", (date, user, role, event))
    conn.commit()
    conn.close()

#database to add and remove announcements
def init_announcements_db():
    conn = sqlite3.connect("announcements.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS announcements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    announcement TEXT,
                    user TEXT,
                    position TEXT)''')
    conn.commit()
    conn.close()

def save_announcement(announcement, user, position):
    conn = sqlite3.connect("announcements.db")
    c = conn.cursor()
    c.execute("INSERT INTO announcements (announcement, user, position) VALUES (?, ?, ?)", 
              (announcement, user, position))
    conn.commit()
    conn.close()

def load_announcements():
    conn = sqlite3.connect("announcements.db")
    c = conn.cursor()
    c.execute("SELECT id, announcement, user, position FROM announcements")
    rows = c.fetchall()
    conn.close()
    return rows

def delete_announcement(id):
    conn = sqlite3.connect("announcements.db")
    c = conn.cursor()
    c.execute("DELETE FROM announcements WHERE id = ?", (id,))
    conn.commit()
    conn.close()