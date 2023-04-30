import streamlit as st
from io import BytesIO
from PIL import Image
from streamlit.components.v1 import html
import plotly.graph_objs as go

from utility.logger import setup_logging
if 'logger' not in st.session_state:
    st.session_state['logger'] = setup_logging()
    st.session_state['logger'].info('Result page loaded')

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

def generate_dropdown_list(df, section_size):
    return ['{} - {}'.format((i+1), i+10) for i in range(0, len(df), section_size)]

st.set_page_config(
    page_title="Result", 
    page_icon="⬇️",
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
st.markdown("""
    <style>
           .block-container {
                padding-top: 1rem;
            }
    </style>
    """, unsafe_allow_html=True)

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

    # Define custom CSS to expand the table to the width of the sidebar
    st.markdown(
        f"""
        <style>
            .sidebar .css-1e0n0sd {{
                width: 100%;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.warning('Zoom in by dragging a rectangle around the area, zoom out by double-clicking.', icon="⚠️")
    st.sidebar.markdown('## Your uploaded image', unsafe_allow_html=True)
    st.sidebar.image(image, use_column_width=True)
    if st.sidebar.button('Upload another image', use_container_width=True):
        st.session_state['is_analyzed'] = False
        # Passthrough to upload button
        nav_page('')

    numbercell = len(df_result.index)
    st.markdown(""" ### Number of Nucleus is <span style="background-color: #A4A4A4; font-size:16.0pt; color:white">&nbsp;{temp}&nbsp;</span> nucleus """.format(temp=str(numbercell)), unsafe_allow_html=True)

    # Create figure
    fig = go.Figure()
    # Constants
    img_width = 1000
    img_height = 800
    scale_factor = 0.825
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

    spacer, dwn_btn, spacer = st.columns([4,6,4])
    with dwn_btn:
        # Use PIL
        buf = BytesIO()
        #result_image = Image.fromarray(result_image[:,:,::-1])
        result_image.save(buf, format="png")
        byte_im = buf.getvalue()
        btn = st.download_button(
            label="🏞️ Save image",
            data=byte_im,
            file_name='{}.png'.format(st.session_state['image_name'][:-4]),
            mime="image/png",
            use_container_width=True
        )

    # Table of results
    st.markdown('---')
    head, spacer, select_box = st.columns([4, 3, 6])
    with head:
        st.markdown('### Result Table', unsafe_allow_html=True)

    df_result_show = df_result.drop(columns=['xmin','ymin','xmax','ymax'])
    start = 1
    stop = 10
    current_section = st.session_state.get("start", start)
    st.session_state.get("stop", stop)

    dropdown_list = generate_dropdown_list(df_result_show, 10)

    with select_box:
        jump_to_section = st.selectbox("Jump to nucleus number", dropdown_list)

    if int(jump_to_section.split()[0]) != current_section:
        start = int(jump_to_section.split()[0])
        stop = int(jump_to_section.split()[2])

    st.dataframe(df_result_show.iloc[start-1:stop], use_container_width=True)

    spacer, dwn_btn_t, spacer = st.columns([4,6,4])
    with dwn_btn_t:
        st.download_button(
        label="🗒️ Save table",
        data=convert_df(df_result),
        file_name='{}.csv'.format(st.session_state['image_name'][:-4]),
        mime='text/csv',
        use_container_width=True
    )

else:
    st.warning('You didn\'t upload image. Please upload image first at the Home page.', icon="⚠️")