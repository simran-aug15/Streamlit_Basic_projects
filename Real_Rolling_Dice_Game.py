import streamlit as st
import random
import time
st.title("Real Rolling Dice")
if st.button("Roll Dice"):
    final=random.randint(1,6)
    st.success(f"you got: {final}")