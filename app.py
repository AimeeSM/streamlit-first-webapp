import streamlit as st

# Title of the app
st.title("Student Information")

name = st.text_input(label="Enter the student's name:", value="")

options = [i+1 for i in range(100)]
age = st.slider(label="Enter the student's age:", min_value=0, max_value=100, value=50)

if st.button("Display", type="primary"):
    st.write(name + " has " + str(age) + "yo.")

    
