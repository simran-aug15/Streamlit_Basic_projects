import streamlit as st
st.title("Calculator")
num1=st.number_input("Enter your first number: ")
num2=st.number_input("Enter your second number: ")
operation=st.selectbox("Select opertions you want to perform: ",["Addition "],["Subtraction "],["Multiplication "],["Division "])
if st.button("calculate"):
    if operation=="Addition":
        st.write(num1+num2)
    elif operation=="Subtraction":
        st.write(num1-num2)
    elif operation=="Multiplication":
        st.write(num1*num2)
    elif operation=="Division":
        st.write(num1/num2)
    else:
        st.write("Wrong input")    

