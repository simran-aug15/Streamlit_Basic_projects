import streamlit as st
from streamlit_drawable_canvas import st_canvas
st.title("🎨 Whiteboard Drawing App")
st.sidebar.header("Tools")
color = st.sidebar.color_picker("Pick Color","#000000")
stroke_width=st.sidebar.slider("Brush Size",1,20,5)
canvas_result=st_canvas
(
    fill_color="rgba(255,255,255,0)",
    stroke_width=stroke_width
    stroke_color=color,
    background_color="#ffffff",
    height=400,
    width=600,
    drawing_mode="freedraw",
    key="canvas"




)