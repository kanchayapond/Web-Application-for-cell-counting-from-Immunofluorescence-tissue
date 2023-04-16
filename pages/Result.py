import streamlit as st
import os
from PIL import Image
from io import BytesIO
from yolo_func import run
from streamlit_cropper import st_cropper
from streamlit.components.v1 import html

# import img
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


st.set_page_config(page_title="Result", page_icon="⬇️",layout="wide")
st.markdown(""" <style> div.stButton > button:first-child { background-color: rgb(198 , 198 , 198);width: 100% } </style>""", unsafe_allow_html=True)

st.sidebar.header("Result Page")
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

if 'image' not in st.session_state:
    image = None
else:
    image = st.session_state['image'] 
    st.sidebar.header("Your Uploaded Image")
    st.sidebar.image(image)


# st.markdown("<h1 style='text-align: center; '>Neucleus counting from Immunofluorescence tissue</h1>", unsafe_allow_html=True)
if image is not None:
    # YOLOv5 part
    image = Image.open(image)
    image.save('temp.jpg')  # Save image to temp.jpg
    image_src = 'temp.jpg'
    img, araaylable = run(source=image_src, weights='weights/best.pt')
    imagee = Image.fromarray(img[:,:,::-1])
    df_result = araaylable
    # Delete temp.jpg
    os.remove('temp.jpg')
    # Delete runs/detect
    os.system('rm -rf runs/detect')

    spacer,col3,spacer = st.columns([1,6,7])
    with col3:
            st.header('Result')
    spacer,colhbreak,spacer = st.columns([1,12,1])
    with colhbreak:
        st.markdown("<hr align='center'; width=100%;size='0'>  ", unsafe_allow_html=True)
    spacer,colrsult,spacer = st.columns([1,6,7])
    with colrsult:
            numbercell = len(df_result. index)
            option = st.selectbox('Result Option',('Large Image', 'Zoomable Image'))
            numbercell = len(df_result. index)
            st.markdown(
            """ ##### Number of Nucleus is <span style="background-color: #A4A4A4; font-size:16.0pt; color:white">&nbsp;{temp}&nbsp;</span> nucleus """.format(temp=str(numbercell))  , unsafe_allow_html=True)    
            csv = convert_df(df_result)

    if option == 'Large Image':
            spacer,colLarge,spacer = st.columns([1,12,1])
            with colLarge:
                st.image(imagee, caption='Your result Image',use_column_width= 'always')
                # st.image(imagee, caption='Your result Image',width=width)
                
    if option == 'Zoomable Image':
            spacer,colzoom,spacer = st.columns([1,12,1])
            with colzoom:
                box_color = st.color_picker(label="Box Color", value='#f991a2')
                cropped_img = st_cropper(imagee, realtime_update=True, box_color=box_color)
                st.image(cropped_img,use_column_width= 'always')

    spacer,coltable,spacer,col7,spacer = st.columns([1,7,1,5,1])
    with coltable:
        st.write(df_result)
    with col7:
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")

        st.download_button(
            label="Download data as csv",
            data=csv,
            file_name='Result_Nucleus.csv',
            mime='text/csv',
        )
        buf = BytesIO()
        imagee.save(buf, format="png")
        byte_im = buf.getvalue()
        st.text(" ")
        st.text(" ")

        btn = st.download_button(
            label="Download Image as png",
            data=byte_im,
            file_name="result.png",
            mime="image/png"
            )
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
else :
    st.warning('You didn\'t upload image. Please upload image first at the Home page.', icon="⚠️")
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