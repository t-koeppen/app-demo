import streamlit as st
from decode_qrcode_page import decode_qrcode_page
from generate_qrcode_page import generate_qrcode_page

st.set_page_config(
    page_title="QR Code Generator v2",
    page_icon="🐆"
)

# add a banner
st.image("https://i.pinimg.com/564x/7b/b2/09/7bb2095f10d02ae481405f478c6a5be1.jpg")

# create a side bar with different pages
options = ['Generate QR Code', 'Decode QR Code', 'About Me']
page_selection = st.sidebar.selectbox("Menu", options)

# when the user selects a page, we want to show something
if page_selection == "Generate QR Code":
    generate_qrcode_page()
elif page_selection == "Decode QR Code":
    decode_qrcode_page()
elif page_selection == "About Me":
    st.write("Hello, my name is Tamea <3")
    st.image("images/Tamea.JPG",
             caption="That's that me espresso")
