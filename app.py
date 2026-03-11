import streamlit as st
import joblib

# Load the trained model and vectorizer
@st.cache_resource
def load_model():
    model = joblib.load('models/spam_classifier_model.pkl')
    vectorizer = joblib.load('models/count_vectorizer.pkl')
    return model, vectorizer

# App configuration
st.set_page_config(page_title="Spam Email Detector", page_icon="🚫", layout="centered")

# Custom CSS for styling
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1 {
        color: #1f3a93;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stTextArea textarea {
        font-size: 1.1rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Main layout
st.title("🚫 Spam Email Detector")
st.markdown("### Easily detect whether an email or message is Spam or Ham!")
st.write("Just paste your text below and click the **Check for Spam** button.")

# Input text area
user_input = st.text_area("Enter your message here:", height=150, placeholder="E.g. Congratulations! You've won a $1,000 Walmart gift card! Click here to claim...")

# Loading model
try:
    model, vectorizer = load_model()
except Exception as e:
    st.error(f"Error loading the model. Make sure `train_model.py` has been executed successfully. Details: {e}")
    st.stop()

# Prediction button
if st.button("Check for Spam", type="primary"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        # Preprocess and predict
        input_data = vectorizer.transform([user_input])
        prediction = model.predict(input_data)[0]
        
        st.markdown("---")
        st.subheader("Result:")
        
        if prediction == 1:
            st.error("🚨 **This message looks like SPAM.** Don't click any suspicious links!")
        else:
            st.success("✅ **This message seems like HAM (Safe).**")
        
        st.markdown("---")

st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Powered by Scikit-Learn & Streamlit</p>", unsafe_allow_html=True)
