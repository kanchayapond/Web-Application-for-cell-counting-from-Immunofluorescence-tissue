import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import base64
# get full working path
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utility.crop_func import check_resolution
from utility.processing import analyzing
from utility.logger import setup_logging
if 'logger' not in st.session_state:
    st.session_state['logger'] = setup_logging()
    st.session_state['logger'].info('Home page loaded')

if not os.path.exists('temp'):
    os.makedirs('temp')
    st.session_state['logger'].info('Create temp/ folder')
else:
    st.session_state['logger'].info('temp/ folder already exists')

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

st.set_page_config(
    page_title="Home",
    page_icon="👋", 
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(""" 
    <style> 
        div.stDownloadButton > button:first-child {
            color: rgb(0 , 0 , 0);
            background-color: rgb(219 , 223 , 232); 
            width: 100%;
        } 
    </style>""", unsafe_allow_html=True)

# Uploader
st.sidebar.header('Upload Your Image')
uploaded_file = st.sidebar.file_uploader("Choose a file", type=['png','jpg','tif'])
if uploaded_file is not None:
    # State update
    st.session_state['image_name'] = uploaded_file.name
    st.session_state['image'] = uploaded_file
    st.session_state['logger'].info('Image uploading...')

    # Show image
    #image = io.imread(uploaded_file)   # Use skimage
    image = Image.open(uploaded_file)   # Use PIL
    st.sidebar.image(image)
    st.session_state['logger'].info('Image uploaded')

    # Analyzer
    if st.sidebar.button("Start Analysis", use_container_width=True):
        st.session_state['logger'].info('Start Analysis')
        uploaded_file = None
        st.session_state['is_analyzed'] = False
        
        # YOLOv5 part
        # Check resolution of image
        state = check_resolution(image)

        # Analyze image
        result_image, df_result = analyzing(state)
        st.session_state['result_image'] = result_image
        st.session_state['df_result'] = df_result

        nav_page("Result")

file_ = open("img/ezgif-2-d384fada9f.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
spacer,headimg,spacer,headtitl = st.columns([1,20,1,24])
with headimg:
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif" width="320">',
        unsafe_allow_html=True,
    )
with headtitl:
    st.markdown("# Imgpress", unsafe_allow_html=True)
    st.markdown("##### Automated Quantification of DAPI-stained Nuclei in Immunofluorescence Tissue", unsafe_allow_html=True)
    st.markdown("create by [S. Kanchayapond](https://github.com/kanchayapond), [N. Nichapat](https://github.com/NichapatNobnorb) and [R. Wayu](https://github.com/cusniwtt)")

st.markdown("---", unsafe_allow_html=True)

st.markdown("### Summary", unsafe_allow_html=True)
st.markdown("""
The web application for automatic nucleus counting for immunofluorescence tissue (DAPI) is a 
user-friendly tool that uses advanced computer vision and machine learning algorithms to accurately 
count the number of nuclei in DAPI-stained tissue biopsy images. It provides multiple output formats, 
including an image with identified nuclei highlighted, a numerical value indicating the total number of 
nuclei, and a table containing additional metrics.
""", unsafe_allow_html=True)
st.info("""
With our state-of-the-art model, YOLOv5, we have achieved outstanding performance with an **F1-score of 0.902** 
and a **DSC (Dice Similarity Coefficient) of 0.713**. This high-performing model will be seamlessly 
integrated into our web application, ensuring accurate and efficient nucleus counting in DAPI-stained 
tissue biopsy images.
Details of our work are provided in the following paper: 
[Web Application for Automatic Nucleus Counting Immunofluorescence Tissue Biopsies](https://github.com/kanchayapond/Web-Application-for-cell-counting-from-Immunofluorescence-tissue)
""", icon="ℹ")

st.markdown("### How to use?", unsafe_allow_html=True)
coldes,spacer,colimg = st.columns([22,1,14])
with coldes:
    st.markdown("""
    **Step 1: Upload your image** </br>
    To upload a DAPI immunofluorescence tissue biopsy image, navigate to the left panel and go to 
    the **Browse files** button. The image should be in `.png`, `.jpg`, or `.tif` format, and the file 
    size should not exceed 10 MB.</br>
    When you upload already, click the **Start Analysis** button in the left panel.
    """, unsafe_allow_html=True)
    with st.expander("ℹ️ More Information about DAPI image", expanded=False):
        st.info("""
        We recommended to upload a DAPI image with resolution should be between 300x240 
        pixels to 400x340 pixels. The image should have a nucleus size similar to the example image 
        displayed in the right pane. However, images uploaded without meeting 
        these size recommendations will be cropped to a size of 320x256 pixels.
        The result image will be combined to same resolution as the uploaded image.
        """, icon="ℹ")
    st.markdown("""
    **Step 2: Check the Results** </br>
    On the results page, you will see an image with the identified nuclei highlighted, as well as a 
    count of the number of nuclei in the image. There also be a table with additional data, such as 
    the position of each nucleus. </br>
    *Additional:* to save the table and image result by clicking the **Save table** and **Save image** 
    buttons. Table will be saved as `.csv` file and image will be saved as `.png` file.
    """, unsafe_allow_html=True)
    st.info("""
        The table will contain the following columns:
        - ***xmin***: x-coordinate of the top-left corner of the nucleus
        - ***ymin***: y-coordinate of the top-left corner of the nucleus
        - ***xmax***: x-coordinate of the bottom-right corner of the nucleus
        - ***ymax***: y-coordinate of the bottom-right corner of the nucleus
        - ***x (px)***: x-coordinate of the nucleus center
        - ***y (px)***: y-coordinate of the nucleus center
        - ***Mean Intensity***: mean intensity of the nucleus
        - ***Horizontal radius (px)***: horizontal radius of the nucleus
        - ***Vertical radius (px)***: vertical radius of the nucleus
        - ***Area (px^2)***: area of the nucleus
        """, icon="ℹ")

with colimg:
    Result = Image.open('img/sample.png')
    st.image(Result, use_column_width= 'always', caption='Recomended example of DAPI image')
    Not_rec = Image.open('img/not_rec.png')
    st.image(Not_rec, use_column_width= 'always', caption='Not recomended example of DAPI image')

st.markdown("---", unsafe_allow_html=True)

Authors, licenses = st.columns([24,16])
with Authors:
    st.markdown("""
    ### Authors
    Please feel free to contact us with any issues, comments, or questions.
    """, unsafe_allow_html=True)
    st.markdown("""
    **Ms. Kanchayapond Seajoong**
    - Email: kanchayapond.earn@mail.kmutt.ac.th
    - Github: [github.com/kanchayapond](https://github.com/kanchayapond)
    """, unsafe_allow_html=True)
    st.markdown("""
    **Ms. Nichapat Nobnorb**
    - Email: nichapat.best@mail.kmutt.ac.th
    - Github: [github.com/NichapatNobnorb](https://github.com/NichapatNobnorb)
    """, unsafe_allow_html=True)
    st.markdown("""
    **Mr. Wayu Ragwongsiri**
    - Email: wayu.qwertyuiop@mail.kmutt.ac.th
    - Github: [github.com/cusniwtt](https://github.com/cusniwtt)
    """, unsafe_allow_html=True)

with licenses:
    st.markdown("### Licenses")
    st.markdown("[MIT License Copyright (c) 2023 Earnn](https://github.com/cusniwtt/Web-Application-for-cell-counting-from-Immunofluorescence-tissue/blob/main/LICENSE)", unsafe_allow_html=True)

st.markdown("---", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;  '>Web Application for Automatic Nucleus Counting 3D Immunofluorescence Tissue Biopsies Using Image Processing</h6>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;  font-size:80%; '>A PROJECT SUBMITTED IN PARTIAL FULFILLMENT OF THE REQUIREMENTS FOR THE DEGREE OF BACHELOR OF SCIENCE (COMPUTER ENGINEERING), FACULTY OF ENGINEERING, KING MONGKUT’S UNIVERSITY OF TECHNOLOGY THONBURI 2022</p>", unsafe_allow_html=True)