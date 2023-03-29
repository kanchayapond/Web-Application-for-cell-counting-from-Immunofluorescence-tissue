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
# import img

st.set_page_config(page_title="Result", page_icon="⬇️",layout="wide")

st.sidebar.header("Resut")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 4rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

data = {'Nucleus': [1, 2, 3, 4],
        'Location X': [20.444, 21.22, 19.567, 18.234],
        'Location Y': [3.20, 0.21, 1.19, 2.18],
        'Area': [20, 21, 19, 18]}
df_result = pd.DataFrame(data)

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
    

st.markdown("<h1 style='text-align: center; '>Neucleus counting from Immunofluorescence tissue</h1>", unsafe_allow_html=True)
image = st.session_state['image'] 
if image is not None:
    image = Image.open(image)
    img , araaylable = cell_counting(image)
    imagee = Image.fromarray(img)
    df_result = get_df(araaylable) 
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
    with col3:
            st.header('Result')
            numbercell = len(df_result. index)
            option = st.selectbox('Result Option',('Large Image', 'Zoomable Image'))
            numbercell = len(df_result. index)
            st.markdown(
            """ ###### Number of Nucleus is <span style="background-color: #C9A4A0; font-size:16.0pt; color:white">&nbsp;{temp}&nbsp;</span> nucleus """.format(temp=str(numbercell))  , unsafe_allow_html=True)    
            csv = convert_df(df_result)
            st.text(" ")
    



    if option == 'Large Image':
            st.write("#")
            st.text(" ")
            st.text(" ")
            st.text(" ")
            spacer,colLarge,spacer = st.columns([1,12,1])
            with colLarge:
                st.image(imagee, caption='Your result Image',use_column_width= 'always')
                # st.image(imagee, caption='Your result Image',width=width)
                
    if option == 'Zoomable Image':
            # spacer,coladjustzoom,spacer = st.columns([1,6,7])
            # with coladjustzoom:
            #     width = st.slider('Adjust image width in pixels?', 0, 2000, 1000)

            st.write("#")
            st.text(" ")
            st.text(" ")
            st.text(" ")
            spacer,colzoom,spacer = st.columns([1,12,1])
            with colzoom:
                # st.image(imagee, caption='Your result Image',use_column_width= 'always')
                # st.image(imagee, caption='Your result Image',width=width)
                box_color = st.color_picker(label="Box Color", value='#f991a2')
                cropped_img = st_cropper(imagee, realtime_update=True, box_color=box_color)
                st.image(cropped_img,use_column_width= 'always')

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