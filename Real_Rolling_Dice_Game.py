import streamlit as st
import random
import time

st.title(" Real Rolling Dice")

# Direct image URLs
dice_images = {
    1: "https://upload.wikimedia.org/wikipedia/commons/1/1b/Dice-1-b.svg",
    2: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Dice-2-b.svg",
    3: "https://upload.wikimedia.org/wikipedia/commons/b/b1/Dice-3-b.svg",
    4: "https://upload.wikimedia.org/wikipedia/commons/f/fd/Dice-4-b.svg",
    5: "https://upload.wikimedia.org/wikipedia/commons/0/08/Dice-5-b.svg",
    6: "https://upload.wikimedia.org/wikipedia/commons/2/26/Dice-6-b.svg",
}

# Placeholder for dice
dice_placeholder = st.empty()

# CSS Animation
st.markdown("""
<style>
@keyframes spin {                          # This is used when we need to add animation and editing 
        0% {transform: rotate(0deg);}      # 0 degree rotation of dice
        100% {transform: rotate(720deg);}  # 360+360 degree rotation of dice } 
.spin 
{ 
   animation: spin 0.5s linear infinite;   # speed of the spin in linear means constant form/speed 
} 
</style> """,unsafe_allow_html=True)       # This is used to forcefull allow css as streamlit doesnot allow usage of html,css,javascript

# Roll Dice Button
if st.button("Roll Dice"):

    # Rolling animation
    for i in range(10):
        num = random.randint(1, 6)
        dice_placeholder.markdown(
            f"<img src='{dice_images[num]}' width='120' class='spin'>",
            unsafe_allow_html=True
        )
        time.sleep(0.1)

    # Final result
    final = random.randint(1, 6)
    dice_placeholder.image(dice_images[final], width=120)
    st.success(f" You got: {final}")