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
from streamlit.components.v1 import html
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)



st.set_page_config(page_title="Upload", page_icon="⬆️", layout="wide")
local_css("style.css")
st.markdown(""" <style> div.stButton > button:first-child { background-color: rgb(198 , 198 , 198);width: 100% } </style>""", unsafe_allow_html=True)
st.sidebar.header("Upload Page")

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

# st.markdown("<h1 style='text-align: center; '>Neucleus counting from Immunofluorescence tissue</h1>", unsafe_allow_html=True)
# spacer,colh2,spacer = st.columns([1,2,1])
# with colh2:
#     st.markdown("<hr align='center'; width=100%;size='-1'>  ", unsafe_allow_html=True)
st.text(" ")
st.write("#")
st.text(" ")
spacer,col1,spacer = st.columns([1,41,1])
run = False
option = 'Image'
with col1:
    st.header('Upload Your Image')
spacer,colh2,spacer = st.columns([1,41,1])
with colh2:
    st.markdown("<hr align='center'; width=100%;size='-1'>  ", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    spacer,col2,spacer = st.columns([1,10,1])
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
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    spacer,Button,spacer = st.columns([3,3,3])
    with Button:
        if st.button("Start Analysis and go to Result page"):
            nav_page("Result")
# else :
#     st.text(" ")
#     st.write("#")
#     st.text(" ")
#     st.text(" ")
#     st.text(" ")
#     st.write("#")
#     st.text(" ")
#     st.text(" ")
#     st.write("#")
#     st.text(" ")
#     st.text(" ")
#     st.text(" ")
#     st.write("#")
#     st.text(" ")
#     st.text(" ")
#     st.text(" ")
#     st.write("#")
#     st.text(" ")
#     st.text(" ")
#     st.text(" ")
#     st.write("#")
#     st.text(" ")
#     st.text(" ")
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


# spacer,footer,spacer = st.columns([1,10,1])
# with footer:
#     st.markdown("<hr align='center' width='100%;' size='10'>  ", unsafe_allow_html=True)
# spacer,footer3,footer2,spacer = st.columns([4,3,5,1])
# with footer3:
#     st.markdown("<h2 style='text-align: left; color:#8a613e;  '>Members : </h2>  ", unsafe_allow_html=True)
# with footer2:
#     st.markdown("<p style='text-align: left; color:#73664f; '>Ms. Kanchayapond Seajoong</p>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: left; color:#73664f;'>Ms. Nichapat Nobnorb</p>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: left; color:#73664f;'>Mr. Wayu Ragwongsiri</p>", unsafe_allow_html=True)
#     st.text(" ")
# st.markdown("<h6 style='text-align: center; color:#73664f; '>Web Application for Automatic Nucleus Counting 3D Immunofluorescence Tissue Biopsies Using Image Processing</h6>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center; color:#73664f; font-size:80%; '>A PROJECT SUBMITTED IN PARTIAL FULFILLMENT OF THE REQUIREMENTS FOR THE DEGREE OF BACHELOR OF SCIENCE (COMPUTER ENGINEERING) FACULTY OF ENGINEERING KING MONGKUT’S UNIVERSITY OF TECHNOLOGY THONBURI 2022</p>", unsafe_allow_html=True)
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