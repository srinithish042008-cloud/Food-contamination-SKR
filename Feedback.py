import streamlit as st

st.title("💬 Feedback")

name = st.text_input("Name")
feedback = st.text_area("Feedback")

if st.button("Submit"):
    st.success("Thanks for your feedback!")
