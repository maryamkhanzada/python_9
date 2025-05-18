import streamlit as st

class Payment:
    @staticmethod
    def process(user):
        st.info("Redirecting to payment gateway (mock)...")
        return True  # Replace with real Stripe logic later
