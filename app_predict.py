import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_path = "./notebooks/models/distilbert_emotion_final"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.eval()

# Label map
label_map = {
    0: ("sadness", "#add8e6"),  # pastel blue
    1: ("joy", "#fff8b0"),       # pastel yellow
    2: ("love", "#ffc0cb"),      # pastel pink
    3: ("anger", "#ffb3b3"),     # light red
    4: ("fear", "#dab6fc"),      # light purple
    5: ("surprise", "#ffd580")   # light orange
}

# Predict function
def predict_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_id = int(torch.argmax(logits, dim=1))
    return label_map[predicted_class_id]

# --- Streamlit App Layout ---

st.set_page_config(page_title="🌿 MoodFlow - Emotion Detector", page_icon="🌿", layout="centered")


st.title("🌿 MoodFlow: Emotion Classifier")
st.write("Enter a sentence and discover the predicted emotion!")

# User input
user_input = st.text_area("Your text here:", "")

if st.button("Predict Emotion"):
    if user_input.strip() != "":
        predicted_label, color = predict_emotion(user_input)
        st.markdown(
            f"<h2 style='text-align: center; color: {color};'>🌸 Predicted Emotion: {predicted_label.capitalize()}</h2>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Please enter some text first 🌸")
