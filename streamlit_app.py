import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
from datetime import time, datetime
from PIL import Image
import PIL.ImageOps   
from io import BytesIO


st.set_page_config(
    page_title="Counting Nucleus",
    layout="wide"
)
data = {'Nucleus': [1, 2, 3, 4],
        'Location X': [20.444, 21.22, 19.567, 18.234],
        'Location Y': [3.20, 0.21, 1.19, 2.18],
        'Area': [20, 21, 19, 18]}
df_result = pd.DataFrame(data)
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


st.markdown("<h1 style='text-align: center; font-size:450%;'>Welcome to</h1>", unsafe_allow_html=True)
spacer,colh1,spacer = st.columns([13,11,10])
with colh1:
    imagehead = Image.open('logi-removebg.png')
    st.image(imagehead,width=300)
spacer,colh2,spacer = st.columns([1,2,1])
with colh2:
    st.markdown("<hr align='center' width='100%;' size='10'>  ", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; '>Web Application for cell counting from Immunofluorescence tissue</h4>", unsafe_allow_html=True)
st.text(" ")
st.write("#")
st.text(" ")
spacer,col1,spacer,col2,spacer = st.columns([1,3,1,3,1])
with col1:
    st.header('Upload Your Image')
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        # imagee = cv2.imread(uploaded_file.name)
        imagee = PIL.ImageOps.invert(image)
        colourPixels = image.convert("RGB")
        colourArray = np.array(colourPixels.getdata()).reshape(image.size + (3,))
        indicesArray = np.moveaxis(np.indices(image.size), 0, 2)
        allArray = np.dstack((indicesArray, colourArray)).reshape((-1, 5))
        df_result = pd.DataFrame(allArray, columns=["y", "x", "red","green","blue"])
    else:
        image = Image.open('pii.jpeg')
        imagee = PIL.ImageOps.invert(image)
#        st.info('☝️ Upload a image file')
    
with col2:
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.image(image, caption='Your input Image')

spacer,col3,spacer,col4,spacer = st.columns([1,3,1,3,1])
with col3:
    st.header('Result')
    st.write('Number of Nucleus is ',len(df_result. index) ,'nucleus')    
    csv = convert_df(df_result)
    st.write(df_result)
    
with col4:
    st.write("#")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.image(imagee, caption='Your result Image')

spacer,col5,col6,spacer = st.columns([2,3,4,10])
with col5:
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='Result_Nucleus.csv',
        mime='text/csv',
    )
with col6:
    buf = BytesIO()
    imagee.save(buf, format="png")
    byte_im = buf.getvalue()
    btn = st.download_button(
        label="Download Image",
        data=byte_im,
        file_name="result.png",
        mime="image/png"
        )
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