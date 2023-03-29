import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Hello",
    page_icon="👋", layout="wide"
)

st.sidebar.success("Select above.")
st.sidebar.title('Sidebar')
st.sidebar.header('Upload Your Image')
uploaded_file = st.sidebar.file_uploader("Choose a file")

# Check if file has been uploaded
if uploaded_file is not None:
    st.session_state['image'] = uploaded_file
    image = Image.open(uploaded_file)
    st.sidebar.header('Your Image')
    st.sidebar.image(image, caption='Your input Image')


if "shared" not in st.session_state:
   st.session_state["shared"] = True


st.markdown("<h1 style='text-align: center; '>Neucleus counting from Immunofluorescence tissue</h1>", unsafe_allow_html=True)
spacer,coldes,spacer = st.columns([1,10,1])
with coldes:
    st.markdown("<h5 style='text-align: center; The Web Application for Automatic Nucleus Counting using DAPI Immunofluorescence Tissue Biopsies images is a user-friendly tool designed to automatically quantify the number of nuclei present in uploaded images. The application utilizes advanced computer vision and machine learning algorithms to accurately identify and count the number of nuclei in DAPI-stained tissue biopsy images. The output of the application is presented in multiple formats including an image with identified nuclei highlighted, a numerical value indicating the total number of nuclei, and a table containing additional metrics such as the position and distribution of nuclei across the image. This Web Application would be beneficial for researchers and medical professionals working in pathology, oncology, and cell biology, as it would save time and increase the accuracy of their analyses. </h5>", unsafe_allow_html=True)
spacer,colh2,spacer = st.columns([1,2,1])
with colh2:
    st.markdown("<hr align='center'; width=100%;size='-1'>  ", unsafe_allow_html=True)
st.text(" ")
