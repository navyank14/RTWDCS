import streamlit as st

import tensorflow as tf

from keras.models import load_model

import os

from PIL import Image





# Load YOLOv5 model

@st.cache_resource

def load_model():

    model = torch.hub.load("ultralytics/yolov5", "custom", path="./weights/best.pt", force_reload=True)

    return model



def main():

    st.title("Waste Detection App")



    model = load_model()



    # Upload image

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image:

        image = Image.open(uploaded_image)

        st.image(image, caption="Uploaded Image", use_column_width=True)



        # Perform inference

        results = model(image)

        results.render()



        # Display predictions

        st.image(results.imgs[0], caption="Detections", use_column_width=True)

        st.write(results.pandas().xyxy[0])  # Display predictions in a table



if __name__ == "__main__":

    main()



# Waste categorization and disposal guidance

def predict_waste(image, model):

    # Preprocess the image

    img = image.resize((224, 224))  # Resize as per your model input size

    img_array = tf.keras.utils.img_to_array(img)

    img_array = tf.expand_dims(img_array, axis=0)  # Add batch dimension

    img_array = img_array / 255.0  # Normalize



    # Predict

    predictions = model.predict(img_array)

    class_index = tf.argmax(predictions[0]).numpy()  # Get predicted class

    categories = ['Plastic', 'Metal', 'Organic', 'Glass', 'Other']  # Update as per your dataset

    disposal_methods = {

        'Plastic': 'Recycle it at a plastic recycling facility.',

        'Metal': 'Recycle it at a metal recycling facility.',

        'Organic': 'Compost it or dispose in an organic waste bin.',

        'Glass': 'Recycle at a glass recycling point.',

        'Other': 'Dispose according to local waste management guidelines.'

    }

    category = categories[class_index]

    disposal = disposal_methods.get(category, "No disposal method available.")

    return category, disposal



# Streamlit app layout

st.title("Waste Detection and Disposal Guide")

st.write("Upload an image of waste to identify its category and learn how to dispose of it.")



# File uploader

uploaded_file = st.file_uploader("Choose a waste image...", type=["jpg", "png", "jpeg"])



if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("Processing...")



    # Load the model

    model = load_waste_model(MODEL_PATH)

    if model:

        # Predict

        category, disposal = predict_waste(image, model)

        st.success(f"Category: {category}")

        st.info(f"Disposal Method: {disposal}")