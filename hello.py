import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋", layout="wide"
)

st.sidebar.success("Select above.")

st.markdown("<h1 style='text-align: center; '>Neucleus counting from Immunofluorescence tissue</h1>", unsafe_allow_html=True)
spacer,coldes,spacer = st.columns([1,10,1])
with coldes:
    st.markdown("<h5 style='text-align: center; '>คำอธิบายจ้า~ ยาวๆ longlong ONCE UPON A TIME a girl named Cinderella lived with her stepmother and two stepsisters.  Poor Cinderella had to work hard all day long so the others could rest. It was she who had to wake up each morning when it was still dark and cold to start the fire.  It was she who cooked the meals. It was she who kept the fire going. The poor girl could not stay clean, from all the ashes and cinders by the fire. </h5>", unsafe_allow_html=True)
spacer,colh2,spacer = st.columns([1,2,1])
with colh2:
    st.markdown("<hr align='center'; width=100%;size='-1'>  ", unsafe_allow_html=True)
st.text(" ")
