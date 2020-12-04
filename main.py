import streamlit as st 
from PIL import Image

import style 


image_size = 400

st.title("iFACADE")

img = st.sidebar.selectbox(
    'Select image',
    ('amber.jpg', 'one.jpg')
)

style_name = st.sidebar.selectbox(
    'Select style',
    ('candy', 'mosaic', 'rain_princess', 'udnie')
)

model = "saved_models/" +  style_name + ".pth"
input_image = "images/content-images/" + img 
output_image =  "images/output-images/" + style_name + "-" + img

st.write("### Source Image:")
image = Image.open(input_image)
st.image(image, width = image_size)

clicked = st.button("Stylize")

if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)

    st.write("### Output Image:")
    image = Image.open(output_image)
    st.image(image, width = image_size)