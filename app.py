import streamlit as st
import joblib

model = joblib.load("spam_model.pkl")

st.set_page_config(
    page_title="Spam Message Detector",
    page_icon="📩"
)

st.title("📩 NLP Spam Message Detector")
st.write("Check whether a message is spam or normal.")

message = st.text_area("Enter your message:")

if st.button("Check Message"):
    if message.strip():
        prediction = model.predict([message])[0]

        if prediction == "spam":
            st.error("This message is SPAM!")
        else:
            st.success("This message is NORMAL (HAM).")
    else:
        st.warning("Please enter a message first.")