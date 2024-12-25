import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load your trained model
@st.cache_resource
def load_model(path):
    model = tf.keras.models.load_model(path)
    return model

model = load_model(".\\Inception v3 model.h5")

# Class names for your dataset
class_names = ["AmurLeopard", "Badger", "BlackBear", "cow", "muskdeer", "redfox", "roedeer",
    "sable", "sikadeer", "weasel", "wildboar"]

# Streamlit GUI
st.title("Wild life species Image Classification with ML Model")
st.write("Upload an image, and the model will classify it into one of the 11 classes.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Classifying...")
    
    # Preprocess the image
    image = image.resize((320, 240))
    image_array = np.array(image) / 255.0  # Normalize the image
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Make a prediction
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions[0])
    confidence = np.max(predictions[0])

    # Show the result
    st.write(f"Predicted Class: {class_names[predicted_class]}")
    st.write(f"Confidence: {confidence:.2f}")
