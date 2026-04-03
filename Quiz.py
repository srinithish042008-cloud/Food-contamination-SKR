import streamlit as st

st.title("📝 Quiz")

q1 = st.radio(
    "Which condition increases contamination?",
    ["Cold", "Clean", "Hot"]
)

if st.button("Submit"):
    if q1 == "Hot":
        st.success("Correct!")
    else:
        st.error("Wrong answer")
