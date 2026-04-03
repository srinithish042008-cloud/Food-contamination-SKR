import streamlit as st

# Page config
st.set_page_config(page_title="Food Contamination Virtual Lab", layout="wide")

# Sidebar navigation
st.sidebar.title("🧪 Virtual Lab Sections")
section = st.sidebar.radio("Go to:", ["Aim & Theory", "Experiment", "Quiz", "Feedback"])

# ---------------- AIM & THEORY ----------------
if section == "Aim & Theory":
    st.title("📘 Aim & Theory")

    st.subheader("🎯 Aim")
    st.write("""
    To study the effect of storage conditions and hygiene on food contamination levels.
    """)

    st.subheader("📖 Theory")
    st.write("""
    Food contamination occurs when harmful microorganisms such as bacteria grow in food.
    
    Factors affecting contamination:
    - Temperature (Cold slows growth, Warm increases growth)
    - Hygiene (Clean reduces contamination, Dirty increases it)
    - Food type (Milk spoils faster than dry foods)
    
    Proper storage and hygiene can minimize microbial growth.
    """)

# ---------------- EXPERIMENT ----------------
elif section == "Experiment":
    st.title("🧫 Food Contamination Virtual Lab")

    food = st.selectbox("Select Food Sample", ["Milk", "Meat", "Vegetables"])
    storage = st.selectbox("Storage Condition", ["Cold", "Room Temperature", "Hot"])
    hygiene = st.selectbox("Hygiene Level", ["Clean", "Moderate", "Poor"])

    if st.button("Run Experiment"):
        contamination = "Low"
        microbial = "Minimal growth"

        if storage == "Room Temperature" or hygiene == "Moderate":
            contamination = "Medium"
            microbial = "Moderate growth"

        if storage == "Hot" or hygiene == "Poor":
            contamination = "High"
            microbial = "Rapid growth"

        st.subheader("🔬 Results")
        st.write(f"**Contamination Level:** {contamination}")
        st.write(f"**Microbial Presence:** {microbial}")

# ---------------- QUIZ ----------------
elif section == "Quiz":
    st.title("📝 Quiz")

    q1 = st.radio(
        "1. Which condition increases contamination?",
        ["Cold storage", "Clean hygiene", "Hot temperature"]
    )

    if st.button("Submit Quiz"):
        score = 0

        if q1 == "Hot temperature":
            score += 1

        st.success(f"Your Score: {score}/1")

# ---------------- FEEDBACK ----------------
elif section == "Feedback":
    st.title("💬 Feedback")

    name = st.text_input("Your Name")
    feedback = st.text_area("Your Feedback")

    if st.button("Submit"):
        st.success("Thank you for your feedback!")
