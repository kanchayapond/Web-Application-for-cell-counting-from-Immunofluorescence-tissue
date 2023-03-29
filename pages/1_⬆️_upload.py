import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import time, datetime
from PIL import Image
import PIL.ImageOps   
from io import BytesIO
from matplotlib import cm
from ML import invert
from imagemks_function import vis,get_df,labelvis,cell_counting
from streamlit_image_comparison import image_comparison
from streamlit_cropper import st_cropper

st.set_page_config(page_title="Upload", page_icon="⬆️", layout="wide")

st.sidebar.header("Upload")

st.markdown("""
        <style>
               .block-container {
                    padding-top: 4rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)


@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

if "shared" not in st.session_state:
   st.session_state["shared"] = True

st.markdown("<h1 style='text-align: center; '>Neucleus counting from Immunofluorescence tissue</h1>", unsafe_allow_html=True)
spacer,coldes,spacer = st.columns([1,12,1])
with coldes:
    st.markdown("<h5 style='text-align: center; '>คำอธิบายจ้า~ ยาวๆ longlong ONCE UPON A TIME a girl named Cinderella lived with her stepmother and two stepsisters.  Poor Cinderella had to work hard all day long so the others could rest. It was she who had to wake up each morning when it was still dark and cold to start the fire.  It was she who cooked the meals. It was she who kept the fire going. The poor girl could not stay clean, from all the ashes and cinders by the fire. </h5>", unsafe_allow_html=True)
spacer,colh2,spacer = st.columns([1,2,1])
with colh2:
    st.markdown("<hr align='center'; width=100%;size='-1'>  ", unsafe_allow_html=True)
st.text(" ")
st.write("#")
st.text(" ")
spacer,col1,spacer,col2,spacer = st.columns([1,6,1,5,1])
run = False
option = 'Image'
with col1:
    st.header('Upload Your Image')
    uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    with col2:
        st.session_state['image'] = uploaded_file
        image = Image.open(uploaded_file)
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.image(image, caption='Your input Image')
    # spacer,colrun = st.columns([3,5])
    # with colrun:
    #     if st.button(' RUN '):
    #         run = True
    # if run:
    spacer,colhbreak,spacer = st.columns([1,9,1])
    with colhbreak:
        st.markdown("<hr align='center'; width=100%;size='-1'>  ", unsafe_allow_html=True)
    spacer,col3,spacer = st.columns([1,6,7])
else :
    st.text(" ")
    st.write("#")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.write("#")
    st.text(" ")
    st.text(" ")
    st.write("#")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.write("#")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.write("#")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.write("#")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.write("#")
    st.text(" ")
    st.text(" ")

st.text(" ")
st.write("#")
st.text(" ")
st.text(" ")


spacer,footer,spacer = st.columns([1,10,1])
with footer:
    st.markdown("<hr align='center' width='100%;' size='10'>  ", unsafe_allow_html=True)
spacer,footer3,footer2,spacer = st.columns([4,3,5,1])
with footer3:
    st.markdown("<h2 style='text-align: left; color:#8a613e;  '>Members : </h2>  ", unsafe_allow_html=True)
with footer2:
    st.markdown("<p style='text-align: left; color:#73664f; '>Ms. Kanchayapond Seajoong</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; color:#73664f;'>Ms. Nichapat Nobnorb</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; color:#73664f;'>Mr. Wayu Ragwongsiri</p>", unsafe_allow_html=True)
    st.text(" ")
st.markdown("<h6 style='text-align: center; color:#73664f; '>Web Application for Automatic Nucleus Counting 3D Immunofluorescence Tissue Biopsies Using Image Processing</h6>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color:#73664f; font-size:80%; '>A PROJECT SUBMITTED IN PARTIAL FULFILLMENT OF THE REQUIREMENTS FOR THE DEGREE OF BACHELOR OF SCIENCE (COMPUTER ENGINEERING) FACULTY OF ENGINEERING KING MONGKUT’S UNIVERSITY OF TECHNOLOGY THONBURI 2022</p>", unsafe_allow_html=True)
#        st.info('☝️ Upload a image file')
    # with open(imagee, "rb") as file:
        # btn = st.download_button(
        #     label="Download image",
        #     data=file,
        #     file_name="result.png",
        #     mime="image/png"
        #   )
# with st.expander('About this app'):
#   st.write('This app shows the various ways on how you can layout your Streamlit app.')
#   st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
# st.write('Hello world!')
# st.header('st.button')

# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')
# if st.button('Upload Image'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')
# if st.button('Save Image'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')
# if st.button('Save Table'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')
# st.selectbox('Save Table',('Save Table as CSV','Save Image'))