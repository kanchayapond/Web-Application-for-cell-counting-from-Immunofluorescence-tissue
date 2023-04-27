import streamlit as st
from io import BytesIO
from PIL import Image
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
    st.sidebar.markdown('## Your uploaded image', unsafe_allow_html=True)
    st.sidebar.image(image, use_column_width=True)
    if st.sidebar.button('Upload another image', use_container_width=True):
        st.session_state['is_analyzed'] = False
        # Passthrough to upload button
        nav_page('')
    st.sidebar.warning('Zoom in by dragging a rectangle around the area, zoom out by double-clicking.', icon="⚠️")

    numbercell = len(df_result.index)
    st.markdown(""" #### Number of Nucleus is <span style="background-color: #A4A4A4; font-size:16.0pt; color:white">&nbsp;{temp}&nbsp;</span> nucleus """.format(temp=str(numbercell)), unsafe_allow_html=True)

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

    st.markdown('---')
    st.markdown('#### Result Table', unsafe_allow_html=True)
    csv = convert_df(df_result)

    df_resultshow1=df_result.drop(columns=['xmin','ymin','xmax','ymax'])

    # Read in your dataframe
    df = df_resultshow1

    # Set the number of rows to display per page
    rows_per_page = 10

    # Initialize the current page number
    current_page = st.session_state.get("current_page", 1)

    # Calculate the total number of pages
    total_pages = int(len(df) / rows_per_page) + 1

    # Create the navigation buttons and container
    spacer, previous_button, dropdown_page, next_button,  spacer = st.columns([4, 6, 6, 6,4])
    with previous_button:
        st.write(" ")
        st.write(" ")
        if st.button("Previous"):
            if current_page > 1:
                current_page -= 1
                st.session_state["current_page"] = current_page

    # Create numbered dropdown for choosing a page of the table
    with dropdown_page:
        # st.write("Go to page:")
        page_selection = st.selectbox("", list(range(1, total_pages + 1)), index=current_page - 1)
        if page_selection != current_page:
            current_page = page_selection
            st.session_state["current_page"] = current_page

    # Create the "Next" button
    # with next_button:
        # if st.button("Next"):
        #     if current_page < total_pages:
        #         current_page += 1
        #         st.session_state["current_page"] = current_page
    with next_button:
        st.write(" ")
        st.write(" ")
        if st.button("Next") and current_page < total_pages:
            current_page += 1
            st.session_state["current_page"] = current_page
        
    # with show_all_button:
    #     if st.button("Show all rows"):
    #         rows_per_page = len(df)
    #         current_page = 1
    #         st.session_state["current_page"] = current_page

    # Calculate the starting and ending row numbers for the current page
    start_row = (current_page - 1) * rows_per_page
    if rows_per_page == len(df):
        end_row = len(df)
    else:
        end_row = min(start_row + rows_per_page, len(df))

    # Display the set of rows based on the starting and ending row numbers
    if end_row > start_row:
        st.write(df[start_row:end_row])
    else:
        st.write(df[start_row:])
     


    # st.write(df_resultshow1, use_container_width='always', text_align='center')
    spacer, dwn_btn_t, spacer = st.columns([4,6,4])
    with dwn_btn_t:
        st.download_button(
        label="🗒️ Save table",
        data=csv,
        file_name='{}.csv'.format(st.session_state['image_name'][:-4]),
        mime='text/csv',
        use_container_width=True
    )

    # Load your data into a pandas DataFrame
    data = df_resultshow1

    # Define the number of rows to display per page
    page_size = 25


    # Calculate the total number of pages needed
    num_pages = int(len(data) / page_size) + 1

    # Define a page number variable to keep track of the current page
    page_num = 1

    # Define the starting and ending row indices for the current page
    start_idx = (page_num - 1) * page_size
    end_idx = start_idx + page_size

    # Add buttons to move to the previous and next page

    col1, col2, col3 = st.columns([1, 2, 1])
    if col1.button('Prev') and page_num > 1:
        page_num -= 1

    if col3.button('Nextt') and page_num < num_pages:
        page_num += 1

    start_idx = (page_num - 1) * page_size
    end_idx = start_idx + page_size
    # Add the page number slider between the "Prev" and "Next" buttons
    with col2.container():
        new_page_num = st.slider('Page Number', 1, num_pages, page_num)
        if new_page_num != page_num:
            page_num = new_page_num
            start_idx = (page_num - 1) * page_size
            end_idx = start_idx + page_size


        # Display the DataFrame with pagination
    col2.write(f"Showing rows {start_idx + 1} to {min(end_idx, len(data))} of {len(data)}")
    st.write(data[start_idx:end_idx])



    # columns = st.multiselect("Columns:",df_result.columns)
    # filter = st.radio("Choose by:", ("inclusion","exclusion"))

    # if filter == "exclusion":
    #     columns = [col for col in df_result.columns if col not in columns]
    # df_result[columns]
    # df_resultselect=df_result[columns]
    # csv2 = convert_df(df_resultselect)
    

else:
    st.warning('You didn\'t upload image. Please upload image first at the Home page.', icon="⚠️")