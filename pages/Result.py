import streamlit as st
from io import BytesIO
from streamlit_cropper import st_cropper
from streamlit.components.v1 import html
import plotly.graph_objs as go

from utility.logger import setup_logging
if 'logger' not in st.session_state:
    st.session_state['logger'] = setup_logging()
    st.session_state['logger'].info('Result page loaded')

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

def process_image(image):
    # Do something with the cropped image
    st.image(image, use_column_width='always')

st.set_page_config(page_title="Result", page_icon="⬇️",layout="wide")
st.markdown(""" <style> div.stButton > button:first-child { background-color: rgb(198 , 198 , 198);width: 100% } </style>""", unsafe_allow_html=True)

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

if 'image' not in st.session_state:
    image = None
    st.session_state['logger'].info('No image uploaded')
else:
    # Check if image is analyzed, to prevent re-analyzing, bugs
    if st.session_state['is_analyzed']:
        image = None
    else:
        image = st.session_state['image']
        #st.sidebar.header("Your Uploaded Image")
        #st.sidebar.image(image)

if image is not None:
    result_image = st.session_state['result_image']
    df_result = st.session_state['df_result']
    #st.markdown('## Result')
    #st.markdown('---')
    numbercell = len(df_result.index)
    st.sidebar.markdown(""" #### Number of Nucleus is <span style="background-color: #A4A4A4; font-size:16.0pt; color:white">&nbsp;{temp}&nbsp;</span> nucleus """.format(temp=str(numbercell)), unsafe_allow_html=True)
    
    buf = BytesIO()
    result_image.save(buf, format="png")
    byte_im = buf.getvalue()
    btn = st.sidebar.download_button(
        label="Save image",
        data=byte_im,
        file_name='{}.png'.format(st.session_state['image_name'][:-4]),
        mime="image/png",
        use_container_width=True
    )
    
    #option = st.sidebar.selectbox('Result Option',('Large Image', 'Zoomable Image'))
    csv = convert_df(df_result)
    st.sidebar.write(df_result.iloc[:,1:], use_column_width='always')
    st.sidebar.download_button(
        label="Save table",
        data=csv,
        file_name='{}.csv'.format(st.session_state['image_name'][:-4]),
        mime='text/csv',
        use_container_width=True
    )

    #if option == 'Large Image':
    #    st.image(result_image, caption='Your result Image', use_column_width='always')

    #if option == 'Zoomable Image':
    if True:
        # Create figure
        fig = go.Figure()

        # Constants
        img_width = 1000
        img_height = 1000
        scale_factor = 0.85

        # Add invisible scatter trace.
        # This trace is added to help the autoresize logic work.
        fig.add_trace(
            go.Scatter(
                x=[0, img_width * scale_factor],
                y=[0, img_height * scale_factor],
                mode="markers",
                marker_opacity=0
            )
        )

        # Configure axes
        fig.update_xaxes(
            visible=False,
            range=[0, img_width * scale_factor]
        )

        fig.update_yaxes(
            visible=False,
            range=[0, img_height * scale_factor],
            # the scaleanchor attribute ensures that the aspect ratio stays constant
            scaleanchor="x"
        )

        # Add image
        fig.add_layout_image(
            dict(
                x=0,
                sizex=img_width * scale_factor,
                y=img_height * scale_factor,
                sizey=img_height * scale_factor,
                xref="x",
                yref="y",
                opacity=1.0,
                layer="below",
                source=result_image)
        )

        # Configure other layout
        fig.update_layout(
            width=img_width * scale_factor,
            height=img_height * scale_factor,
            margin={"l": 0, "r": 0, "t": 0, "b": 0},
        )
        st.plotly_chart(fig, use_container_width=True)
        #cropped_img = st_cropper(result_image, realtime_update=True, box_color='#EADDCA')
        #st.image(cropped_image, use_column_width='always')
    
    #spacer,coltable,spacer = st.columns([1,12,1])
    #with coltable:
    #    st.write(df_result)

    #col7,col6 = st.columns([2,2])
    #with col7:
    #    st.sidebar.download_button(
    #        label="Save table",
    #        data=csv,
    #        file_name='{}.csv'.format(st.session_state['image_name'][:-4]),
    #        mime='text/csv',
    #    )
    #with col6:
    #    buf = BytesIO()
    #    result_image.save(buf, format="png")
    #    byte_im = buf.getvalue()
    #    btn = st.sidebar.download_button(
    #        label="Save image",
    #        data=byte_im,
    #        file_name='{}.png'.format(st.session_state['image_name'][:-4]),
    #        mime="image/png"
    #        )
else:
    st.warning('You didn\'t upload image. Please upload image first at the Home page.', icon="⚠️")