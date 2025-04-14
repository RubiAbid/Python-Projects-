import streamlit as st

# Title of the Website
st.title("Welcome to My Streamlit Website")

# Description
st.write("This is a simple website created using Streamlit.")

# Adding an input field where users can type their name
name = st.text_input("Enter your name:")

# Adding a button that will respond when clicked
if st.button("Submit"):
    if name:
        st.write(f"Hello {name}, welcome to the website!")
    else:
        st.write("Please enter your name to proceed.")

# Additional Content (e.g., images, videos)
st.image("https://via.placeholder.com/400", caption="A placeholder image")

# Optional: Display some more information
st.write("Streamlit makes it easy to create web apps in Python. No need to use HTML, CSS, or JavaScript!")
