import streamlit as st
from auth import Authenticator
from models.course import Course
from models.payment import Payment
from db import init_db

init_db()
auth = Authenticator()

st.set_page_config(page_title="SkillNest", layout="centered")
st.title("🐣 SkillNest – Learn. Build. Grow.")

if "user" not in st.session_state:
    user = auth.login()
    if user:
        st.session_state.user = user
    else:
        st.stop()

user = st.session_state.user
st.success(f"Welcome back, {user.username}!")

course = Course.load_sample()
course.display()

if not user.is_premium:
    if st.button("🔓 Unlock Premium Content"):
        if Payment.process(user):
            user.upgrade()
            st.success("🎉 You've been upgraded to Premium!")
        else:
            st.error("❌ Payment Failed. Try again.")

if user.is_premium:
    st.subheader("📈 Your Learning Progress")
    user.show_progress()
