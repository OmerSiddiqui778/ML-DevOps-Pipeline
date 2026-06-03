import streamlit as st 
import numpy as np 
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model 
from PIL import Image 

model = load_model("model.keras")

st.title("AI vs Real Image classification")
st.write("Upload an image the model will classify it as an AI-generated or Real..")


uploaded_file = st.file_uploader("Choose an Image..", type=['jpg', 'png', 'jpeg'])

def predict(img):
    img = img.resize((224,224))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    pred = model.predict(img_array)[0][0]
    return pred

if uploaded_file is not None: 
    img = Image.open(uploaded_file)
    st.image(img, caption= "uploaded image")
    pred = predict(img)

    if pred > 0.5: 
        st.success(f"Prediction: **Real** ({pred})")
    else: 
        st.error(f"Prediction: **AI Generated** ({pred})")