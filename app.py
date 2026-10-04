
import streamlit as st
import joblib

# Load trained ML model
model = joblib.load("spam_email_model.pkl")

# Load TF-IDF vectorizer
vectorizer = joblib.load("tfidf_vectorizer.pkl")


# Page configuration
st.set_page_config(
    page_title="Spam Email Detector",
    page_icon="📧",
    layout="centered"
)


# Main title
st.title("📧 Spam Email Detector")

st.write(
    "An NLP and Machine Learning based application "
    "that classifies emails as Spam or Ham."
)


# Sidebar
with st.sidebar:
    st.header("About the Project")

    st.write(
        "This project uses Natural Language Processing "
        "(NLP) and Machine Learning to detect spam emails."
    )

    st.write("**NLP:** TF-IDF")
    st.write("**ML:** Multinomial Naive Bayes")
    st.write("**Task:** Spam vs Ham Classification")


# Email input
st.subheader("Enter Email")

email_text = st.text_area(
    "Paste your email below:",
    height=220,
    placeholder="Example: Congratulations! You have won a prize..."
)


# Prediction button
if st.button("🔍 Predict Email", use_container_width=True):

    if email_text.strip() == "":
        st.warning("Please enter an email first.")

    else:
        # Convert email text into TF-IDF features
        email_tfidf = vectorizer.transform([email_text])

        # Make prediction
        prediction = model.predict(email_tfidf)[0]

        st.subheader("Prediction Result")

        if prediction == 1:
            st.error("🚨 SPAM EMAIL")
            st.write("This email has been classified as spam.")

        else:
            st.success("✅ HAM EMAIL")
            st.write("This email appears to be legitimate.")


# Footer
st.divider()

st.caption(
    "Spam Email Detection | NLP + Machine Learning"
)
