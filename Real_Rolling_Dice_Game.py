import streamlit as st
import random
import time
st.title("Real Rolling Dice")
if st.button("Roll Dice"):
    final=random.randint(1,6)
    st.success(f"you got: {final}")

#Dice images
dice_images={
    1: "https://game-icons.net/1x1/delapouite/dice-six-faces-one.html",
    2: "https://game-icons.net/tags/dice.html",
    3: "https://www.shutterstock.com/image-vector/one-dice-number-three-on-visible-1240489420",
    4: "https://game-icons.net/tags/dice.html",
    5: "https://www.reddit.com/r/rpg/comments/8nt7n3/i_was_annoyed_that_there_were_no_android_dice/",
    6: "https://game-icons.net/tags/dice.html"
}

 # Place holder
 dice_placeholder=st.empty()