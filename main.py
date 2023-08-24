
import streamlit as st

def cas_score(responses):
    return sum(responses)

st.title('Coronavirus Anxiety Scale (CAS)')

st.write("""
### Instructions
Please indicate how often you've felt the following ways in the past two weeks.
""")

options = ['Not at all', 'Rarely', 'Sometimes', 'Often', 'Nearly every day']

# Sample questions for CAS (Make sure you have the right and full list)
questions = [
    "I felt dizzy, lightheaded, or faint, when I read or listened to news about the coronavirus.",
    "I felt an increased heart rate or palpitations when I thought about or was exposed to information about the coronavirus.",
    "I had trouble falling asleep or staying asleep because I was thinking about the coronavirus.",
    "I felt paralyzed or frozen when I thought about or was exposed to information about the coronavirus."
]

responses = [st.selectbox(q, options) for q in questions]

# Map the responses to scores (0-4)
scores = [options.index(r) for r in responses]

total_score = cas_score(scores)

st.write(f"## Your CAS Score is: {total_score}")

if total_score <= 5:
    st.write("Your anxiety level related to Coronavirus seems to be low.")
elif 5 < total_score <= 9:
    st.write("Your anxiety level related to Coronavirus is moderate.")
else:
    st.write("Your anxiety level related to Coronavirus is high. It's recommended to speak with a professional.")

st.write("""
**Note:** This is a basic screener and should not be used as a diagnostic tool.
Always consult with a mental health professional for a comprehensive evaluation.
""")
