import streamlit as st

def main():
    st.title("Coronavirus Anxiety Scale (CAS)")
    st.write("**Instructions**: Please indicate how often you've experienced the following over the *last 2 weeks*.")

    # Questions and corresponding options
    options = ['Not at all', 'Rare, less than a day or two', 'Several days', 'More than 7 days', 'Nearly every day over the last 2 weeks']
    questions = [
        "I felt dizzy, lightheaded, or faint, when I read or listened to news about the coronavirus.",
        "I had trouble falling or staying asleep because I was thinking about the coronavirus.",
        "I felt paralyzed or frozen when I thought about or was exposed to information about the coronavirus.",
        "I lost interest in eating when I thought about or was exposed to information about the coronavirus.",
        "I felt nauseous or had stomach problems when I thought about or was exposed to information about the coronavirus."
    ]
    
    # Displays drop down menus allowing users to select their answwers to the questions.
    responses = [st.selectbox(q, options) for q in questions]

    # Map the responses to scores (0-4) and calculate total score.
    scores = [options.index(r) for r in responses]
    total_score = sum(scores)
    
    # Submit button
    if st.button('Submit'):
        if total_score >= 9:
            st.write("Your CAS score is", total_score, ". This indicates dysfunctional coronavirus-related anxiety. Please consult a mental health professional.")
        else:
            st.write("Your CAS score is", total_score, ". This doesn't indicate dysfunctional coronavirus-related anxiety. \
            But, if you feel something's wrong, you should still consult a mental health professional.")
if __name__ == "__main__":
    main()
