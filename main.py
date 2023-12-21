import streamlit as st

def main():
    st.title("Coronavirus Anxiety Scale (CAS)")
    st.write("**Instructions"": Please indicate how often you've experienced the following over the last 2 weeks.\n \
    0 = Not at all, 1 = Rare, less than a day or two, 2 = Several days, 3 = More than 7 days, 4 = Nearly every day over the last 2 weeks.")

    # Define the questions
    questions = [
        "I felt dizzy, lightheaded, or faint when I read or listened to news about the coronavirus.",
        "I had trouble falling or staying asleep because I was thinking about the coronavirus.",
        "I felt paralyzed or frozen when I thought about or was exposed to information about the coronavirus.",
        "I lost interest in eating when I thought about or was exposed to information about the coronavirus.",
        "I felt nauseous or had stomach problems when I thought about or was exposed to information about the coronavirus."
    ]

    # Initialize the total score
    total_score = 0

    # Iterate over questions
    
    for i, question in enumerate(questions, 1):
        response = st.radio(f"{i}. {question}", range(5), key=f"q{i}")
        total_score += response
    
    # Submit button
    if st.button('Submit'):
        if total_score >= 9:
            st.write("Your score is", total_score, ". This may indicate significant coronavirus-related anxiety. It's advisable to consult a healthcare professional for a more comprehensive evaluation.")
        else:
            st.write("Your score is", total_score, ".")
        st.write("Please note: This tool is not a substitute for professional medical advice.")

if __name__ == "__main__":
    main()
