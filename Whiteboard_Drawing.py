import streamlit as st
from streamlit_drawable_canvas import st_canvas
st.title("🎨 Whiteboard Drawing App")
st.sidebar.header("Tools")
color = st.sidebar.color_picker("Pick Color","#000000")
stroke_width=st.sidebar.slider("Brush Size",1,20,5)
