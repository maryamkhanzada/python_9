import sqlite3
import streamlit as st

class User:
    def __init__(self, username, is_premium=False):
        self.username = username
        self.is_premium = is_premium

    @staticmethod
    def get_user(username, password):
        conn = sqlite3.connect("skillnest.db")
        c = conn.cursor()
        c.execute("SELECT username, is_premium FROM users WHERE username=? AND password=?", (username, password))
        row = c.fetchone()
        conn.close()
        if row:
            return PremiumUser(username) if row[1] else FreeUser(username)
        return None

    def show_progress(self):
        st.info("Progress tracking coming soon.")

    def upgrade(self):
        conn = sqlite3.connect("skillnest.db")
        c = conn.cursor()
        c.execute("UPDATE users SET is_premium=1 WHERE username=?", (self.username,))
        conn.commit()
        conn.close()
        self.is_premium = True

class FreeUser(User):
    def __init__(self, username):
        super().__init__(username, is_premium=False)

    @staticmethod
    def register(username, password):
        conn = sqlite3.connect("skillnest.db")
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password, is_premium) VALUES (?, ?, 0)", (username, password))
            conn.commit()
            st.sidebar.success("User created! Please login.")
        except sqlite3.IntegrityError:
            st.sidebar.error("Username already exists.")
        finally:
            conn.close()
        return None

class PremiumUser(User):
    def __init__(self, username):
        super().__init__(username, is_premium=True)
