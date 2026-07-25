import streamlit as st
st.title("My First App")  # Create a title for app
st.write("Hello students welcome to my live classes for Python AI")


#input widgets
name=st.text_input("Enter your name: ")   # for text input from user
age=st.slider("Select your age: ",10,50)

if st.button("Submit"):      # If user click submit then the text will be displayed to that person 
    st.write(f"Hello {name}, you are {age} years old")

