import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
import pandas as pd

# Download stopwords (Run once)
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load the saved model and vectorizer
svm_model = joblib.load("svm_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Function to clean text
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)  # Remove single characters
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = text.lower()  # Convert to lowercase
    text = ' '.join(word for word in text.split() if word not in stop_words)  # Remove stopwords
    return text

# Streamlit App Interface
st.title("Twitter Hate Speech Detector")
st.write("Enter a tweet to check if it contains hate speech.")

# User Input
user_input = st.text_area("Enter Tweet:")
st.image(r"C:\Users\Vishwa\Desktop\GUVI captone\twitter\2329257_bird_twitter_twitter logo_website_icon.png",width=200)

if st.button("Predict"):
    if user_input:
        cleaned_text = clean_text(user_input)
        transformed_text = tfidf.transform([cleaned_text])  # Convert text to numerical features
        prediction = svm_model.predict(transformed_text)[0]

        # Display Result
        if prediction == 1:
            st.error("⚠️ Hate Speech Detected!")
            st.image(r"C:\Users\Vishwa\Desktop\GUVI captone\twitter\thumbsdown.jpg")
        else:
            st.success("✅ No Hate Speech Detected.")
            st.image(r"C:\Users\Vishwa\Desktop\GUVI captone\twitter\thumbsup.jpg")
    else:
        st.warning("Please enter a tweet before predicting.")
