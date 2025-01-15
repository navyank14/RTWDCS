import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

# Ensure paths are correct
MODEL_PATH = './weights/waste_model.h5'

# Load the trained waste detection model
def load_waste_model(model_path):
    try:
        model = load_model(model_path)
        st.success("✅ Model loaded successfully!")
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

# Image preprocessing and prediction
def predict_waste(image, model):
    try:
        # Resize and normalize the image for model input
        img = image.resize((224, 224))
        img_array = tf.keras.utils.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Perform prediction
        predictions = model.predict(img_array)
        class_index = np.argmax(predictions[0])  # Get the predicted class index

        # Define categories and disposal methods
        categories = ['Plastic', 'Metal', 'Organic', 'Glass', 'Other']
        disposal_methods = {
            'Plastic': 'Recycle it at a plastic recycling facility.',
            'Metal': 'Recycle it at a metal recycling facility.',
            'Organic': 'Compost it or dispose in an organic waste bin.',
            'Glass': 'Recycle at a glass recycling point.',
            'Other': 'Dispose according to local waste management guidelines.'
        }

        # Get the predicted category and disposal method
        category = categories[class_index]
        disposal = disposal_methods.get(category, "No disposal method available.")
        return category, disposal

    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
        return None, None

# Streamlit app layout
st.title("Waste Detection and Classification :")
st.write("Capture an image using your camera to identify the waste category and learn how to dispose of it.")

# Load the model when the app starts
model = load_waste_model(MODEL_PATH)

# Camera input
camera_image = st.camera_input("Capture a waste image...")

if camera_image and model:
    try:
        # Convert the captured image to a PIL image
        image = Image.open(io.BytesIO(camera_image.getvalue()))

        # Show the image
        st.image(image, caption="Captured Image", use_column_width=True)
        st.write("Processing...")

        # Predict using the loaded model
        category, disposal = predict_waste(image, model)
        if category:
            st.success(f"Category: {category}")
            st.info(f"Disposal Method: {disposal}")
    except Exception as e:
        st.error(f"❌ Error processing the image: {e}")

# File uploader
uploaded_file = st.file_uploader("Choose a waste image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Processing...")        

# Test the model with a local image
if st.button("Test Model with Local Image"):
    test_image_path = r"C:/Users/HP/OneDrive/Pictures/Screenshots/test_image.jpg"
    try:
        test_image = Image.open(test_image_path)
        st.image(test_image, caption="Test Image", use_column_width=True)
        category, disposal = predict_waste(test_image, model)
        st.success(f"Category: {category}")
        st.info(f"Disposal Method: {disposal}")
    except Exception as e:
        st.error(f"❌ Error loading test image: {e}")
