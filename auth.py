import streamlit as st
from models.user import User, FreeUser

class Authenticator:
    def login(self):
        st.sidebar.title("🔐 Login or Sign Up")
        choice = st.sidebar.radio("Choose an option:", ["Login", "Sign Up"])

        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button(choice):
            if choice == "Login":
                user = User.get_user(username, password)
                if user:
                    return user
                else:
                    st.sidebar.error("Invalid credentials.")
            elif choice == "Sign Up":
                return FreeUser.register(username, password)
