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
import  streamlit_vertical_slider  as svs


st.set_page_config(
    page_title="Counting Nucleus",
    layout="wide"
)
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

realtime_update = True

st.markdown("<h1 style='text-align: center; font-size:400%;'>Welcome to</h1>", unsafe_allow_html=True)
spacer,colh1,spacer = st.columns([13,11,10])
with colh1:
    imagehead = Image.open('logi-removebg.png')
    st.image(imagehead,width=269)
spacer,colh2,spacer = st.columns([1,2,1])
with colh2:
    st.markdown("<hr align='center'; width=100%;size='-1'>  ", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; '>Web Application for cell counting from Immunofluorescence tissue</h4>", unsafe_allow_html=True)
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
    image = Image.open(uploaded_file)
    img , araaylable = cell_counting(image)
    imagee = Image.fromarray(img)
    df_result = get_df(araaylable)
    with col2:
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.image(image, caption='Your input Image')
    spacer,colrun = st.columns([3,5])
    # with colrun:
    #     if st.button(' RUN '):
    #         run = True
    # if run:
    spacer,col3,spacer = st.columns([1,6,8])
    with col3:
            st.header('Result')
            numbercell = len(df_result. index)
            option = st.selectbox('Result Option',('Large Image', 'Compared Image'))
            numbercell = len(df_result. index)
            st.markdown(
            """ ###### Number of Nucleus is <span style="background-color: #C9A4A0; font-size:16.0pt; color:white">&nbsp;{temp}&nbsp;</span> nucleus """.format(temp=str(numbercell))  , unsafe_allow_html=True)    
            csv = convert_df(df_result)
            st.text(" ")
    spacer,coladjust1,coladjust2,coladjust3,coladjust4,coladjust5,spacer = st.columns([1,2,2,2,2,2,1])
    with coladjust1:
        width = st.slider('Adjust image width in pixels?', 0, 2000, 1000)
    with coladjust2:
        left = st.slider('Zoom from left by percentage of width', 0, 50, 0)
    with coladjust3:
        right = st.slider('Zoom from right by percentage of width', 0, 49, 1)
    with coladjust4:
        st.write("Zoom from top by percentage of height")
        top = svs.vertical_slider( 
                    default_value=1, 
                    step=1, 
                    min_value=0, 
                    max_value=50,
                    slider_color= '#BD8F8A', #optional
                    track_color='#F4DBC9', #optional
                    thumb_color = '#AA706A' #optional
                    )
        top = int(top or 0 )
    with coladjust5:
        st.write("Zoom from bottom by percentage of height")
        bottom = svs.vertical_slider( 
                    default_value=1, 
                    step=1, 
                    min_value=0, 
                    max_value=49,
                    slider_color= '#BD8F8A', #optional
                    track_color='#F4DBC9', #optional
                    thumb_color = '#AA706A' #optional
                    )
        bottom = int(bottom or 0 )


    if option == 'Large Image':
            st.write("#")
            st.text(" ")
            st.text(" ")
            st.text(" ")
            spacer,col5,spacer = st.columns([1,7,1])
            with col5:
                # st.image(imagee, caption='Your result Image',use_column_width= 'always')
                # st.image(imagee, caption='Your result Image',width=width)
                box_color = st.color_picker(label="Box Color", value='#0000FF')
                cropped_img = st_cropper(imagee, realtime_update=realtime_update, box_color=box_color)
                st.image(cropped_img,width=width)
                


    else :
            st.write("#")
            st.text(" ")
            st.text(" ")
            st.text(" ")
            spacer,col9,spacer = st.columns([1,12,1])
            im =imagee
            w, h = im.size
            
            # Setting the points for cropped image
            left = w * left/100
            top = h * top/100
            right = w - ( w * right/100)
            bottom = h - (h * bottom/100)
            
            # Cropped image of above dimension
            # (It will not change original image)
            im1 = im.crop((left, top, right, bottom))
            with col9:
                st.image(im1, caption='Your result Image',width=width)
    spacer,coltable,spacer = st.columns([1,12,1])
    with coltable:
        st.write(df_result)
    spacer,col7,col6,spacer = st.columns([4,5,5,4])
    with col7:
            st.download_button(
                label="Download data as csv",
                data=csv,
                file_name='Result_Nucleus.csv',
                mime='text/csv',
            )
    with col6:
            buf = BytesIO()
            imagee.save(buf, format="png")
            byte_im = buf.getvalue()
            btn = st.download_button(
                label="Download Image as png",
                data=byte_im,
                file_name="result.png",
                mime="image/png"
                )

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