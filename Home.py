import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import base64
import streamlit.components.v1 as components



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
    page_icon="👋", layout="wide"
)
st.sidebar.header('Upload Your Image')
# expander = st.sidebar.expander("About Your Upload Image")
st.sidebar.write("For now, we support only upload DAPI immunofluorescence tissue images in PNG, JPEG, or TIF file format. Additionally, the file size must not exceed 10 MB, and only one image can be uploaded at a time. ")
exam = Image.open('img/example.png')
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # styles = {'material-icons':{'color': 'red'},
    #       'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'},
    #       'notification-text': {'':''},
    #       'close-button':{'':''},
    #       'link':{'':''}}

    # st.sidebar.custom_notification_box(icon='info', textDisplay='You can only upload image with...', externalLink='more info', url='#', styles=styles, key="foo")
    st.session_state['image'] = uploaded_file
    image = Image.open(uploaded_file)
    st.sidebar.image(image, caption='Your input Image')
    if st.sidebar.button("Start Analysis and go to Result page"):
        nav_page("Result")
else :
    st.sidebar.image(exam,width=150)    



    


st.markdown(""" <style> div.stButton > button:first-child { background-color: rgb(255 , 255 , 255);width: 100% } </style>""", unsafe_allow_html=True)
file_ = open("img/ezgif-2-d384fada9f.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
spacer,headimg,spacer,headtitl,spacer = st.columns([1,16,1,24,1])
with headimg:

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif" width="300">',
        unsafe_allow_html=True,
    )
with headtitl:
    st.markdown("<h1 style='text-align: center; '>Neucleus counting from Immunofluorescence tissue</h1>", unsafe_allow_html=True)
st.text(" ")
spacer,colh2,spacer = st.columns([1,41,1])
with colh2:
    st.markdown("<hr align='center'; width=100%;size='-1'>  ", unsafe_allow_html=True)
# spacer,colh2,spacer = st.columns([2,8,2])
# with colh2:
#     example = Image.open('img/example.png')
#     st.image(example)
spacer,icon,des,spacer = st.columns([1,3,38,1])
with icon:
    dess = Image.open('img/des.png')
    st.image(dess)    
with des:
    st.header("Description")
spacer,descrip,spacer = st.columns([1,41,1])
with descrip:
    st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><p style='font-size:120%;' >The Web Application for Automatic Nucleus Counting using DAPI Immunofluorescence Tissue Biopsies images is a user-friendly tool designed to automatically quantify the number of nuclei present in uploaded images. The application utilizes advanced computer vision and machine learning algorithms to accurately identify and count the number of nuclei in DAPI-stained tissue biopsy images. The output of the application is presented in multiple formats including an image with identified nuclei highlighted, a numerical value indicating the total number of nuclei, and a table containing additional metrics such as the position and distribution of nuclei across the image.</p></div>", unsafe_allow_html=True)
spacer,icon2,des2,spacer = st.columns([1,3,38,1])
with icon2:
    how = Image.open('img/how.png')
    st.image(how)    
with des2:
    st.header("How to use this Web Application")

spacer,coldes,spacer,colimg,spacer = st.columns([1,20,5,16,1])
with coldes:
    # st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><h4>Step 1 : Go to the upload page </h4></div>", unsafe_allow_html=True)
    # st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><p style='font-size:120%;' >Go to the upload page by clicking on the sidebar or the button 'Start using this Web Application' below this page. </p></div>", unsafe_allow_html=True)
    st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><h4>Step 1 : Upload your image</h4></div>", unsafe_allow_html=True)
    st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><p style='font-size:120%;' >Upload your DAPI immunofluorescence tissue biopsy image by clicking the 'Browse file' button and selecting the image file from your computer. Once you have selected the file, click the 'Upload' button to upload the image. </p></div>", unsafe_allow_html=True)
    # step2 = Image.open('img/step2.png')
    # st.image(step2)    
    st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><h4>Step 2 : Check the uploaded image and go to Result page</h4></div>", unsafe_allow_html=True)
    st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><p style='font-size:120%;' >Check the uploaded image to make sure it is the correct file and that it has been uploaded correctly. Then click the 'Start Analysis and go to Result page' or 'Result' button in the sidebar to proceed to the results page.</p></div>", unsafe_allow_html=True)
    # step3 = Image.open('img/step3.png')
    # st.image(step3)    
    st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><h4>Step 3 : Results</h4></div>", unsafe_allow_html=True)
    st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><p style='font-size:120%;' >On the results page, you will see an image with the identified nuclei highlighted, as well as a count of the number of nuclei in the image. There also be a table with additional data, such as the position of each nucleus.</p></div>", unsafe_allow_html=True)
    # step4 = Image.open('img/step4.png')
    # st.image(step4)    
    st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><h4>Step 4 : Select dropdown menu</h4></div>", unsafe_allow_html=True)
    st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><p style='font-size:120%;' >Use the dropdown menu to select a large image or a zoomable image for the result image that is shown in the web application.</p></div>", unsafe_allow_html=True)
    # step5 = Image.open('img/step5.png')
    # st.image(step5)    
    st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><h4>Step 5 : Save table result and image result</h4></div>", unsafe_allow_html=True)
    st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><p style='font-size:120%;' >Save the table result and the image result by clicking the 'Download data as csv' and 'Download Image as png' buttons.</p></div>", unsafe_allow_html=True)
    # step6 = Image.open('img/step6.png')
    # st.image(step6)
    st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><h4>Step 6 : Back to upload page</h4></div>", unsafe_allow_html=True)
    st.markdown("<style>div.a {text-indent: 0px;\}</style><div class='a'><p style='font-size:120%;' >Click on the 'Back to Upload Page' button to return to the upload page and upload another image</p></div>", unsafe_allow_html=True)
    # backupload = Image.open('img/backupload.png')
    # st.image(backupload)
with colimg:
    # Upload = Image.open('img/Upload.png')
    # st.image(Upload , use_column_width= 'always')
    Result = Image.open('img/Result.png')
    st.image(Result , use_column_width= 'always')


st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
# spacer,Button,spacer = st.columns([3,2,3])
# with Button:
#     if st.button("Start using this Web Application"):
#         nav_page("Upload")


st.text(" ")
st.text(" ")
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
spacer,footer,spacer = st.columns([1,41,1])
with footer:
    st.markdown("<hr align='center' width='100%;' size='10'>  ", unsafe_allow_html=True)

spacer,Authors,spacer,licenses,spacer = st.columns([1,25,1,15,1])
with Authors:
    st.markdown("<h3 style='text-align: left;   '>Authors : </h3>  ", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;  '>Please feel free to contact us with any issues, comments, or questions.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;  '>Ms. Kanchayapond Seajoong</p>", unsafe_allow_html=True)
    st.markdown("- Email: kanchayapond.earn@mail.kmutt.ac.th",unsafe_allow_html=True)
    st.markdown("- Github: https://github.com/kanchayapond",unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; '>Ms. Nichapat Nobnorb</p>", unsafe_allow_html=True)
    st.markdown("- Email: nichapat.best@mail.kmutt.ac.th",unsafe_allow_html=True)
    st.markdown("- Github: https://github.com/NichapatNobnorb",unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;'>Mr. Wayu Ragwongsiri</p>", unsafe_allow_html=True)
    st.markdown("- Email: wayu.windy@mail.kmutt.ac.th",unsafe_allow_html=True)
    st.markdown("- Github: https://github.com/cusniwtt",unsafe_allow_html=True)

with licenses:
    st.markdown("<h3 style='text-align: left;   '>Licenses : </h3>  ", unsafe_allow_html=True)
    st.text("- Python")
    st.text("- Streamlit")
    st.text("- PyTorch")
    st.text("- TensorFlow")


spacer,foottt,spacer = st.columns([1,41,1])
with foottt:
    st.text(" ")
    st.write("#")
    st.text(" ")
    # st.markdown("<hr align='center' width='100%;' size='10'>  ", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left;  '>Web Application for Automatic Nucleus Counting 3D Immunofluorescence Tissue Biopsies Using Image Processing</h6>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;  font-size:80%; '>A PROJECT SUBMITTED IN PARTIAL FULFILLMENT OF THE REQUIREMENTS FOR THE DEGREE OF BACHELOR OF SCIENCE (COMPUTER ENGINEERING) FACULTY OF ENGINEERING KING MONGKUT’S UNIVERSITY OF TECHNOLOGY THONBURI 2022</p>", unsafe_allow_html=True)