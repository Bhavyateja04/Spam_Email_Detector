import streamlit as st
import joblib
import string

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

st.title("📧 Spam Email Detection System")

st.markdown("""
This application uses **Natural Language Processing (NLP)** and
**Machine Learning** to classify messages as Spam or Not Spam.
""")

message = st.text_area("Enter Message")

if st.button("Predict"):

    cleaned = clean_text(message)

    vectorized = vectorizer.transform([cleaned])

    prediction = model.predict(vectorized)[0]

    probabilities = model.predict_proba(vectorized)[0]

    confidence = max(probabilities) * 100

    if prediction == "spam":
        st.error(f"🚨 SPAM ({confidence:.2f}% confidence)")
    else:
        st.success(f"✅ NOT SPAM ({confidence:.2f}% confidence)")