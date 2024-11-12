import streamlit as st
import segno
import time

def generate_qrcode(url):
    qrcode = segno.make_qr(url)
    qrcode.save("images/qrcode_streamlit.png",
                scale=10)

def generate_qrcode_page():

    # add a title
    st.title("QR Code Generator")

    # add a textbox
    url = st.text_input("Please enter the data you want to encode:")

    if url:
        with st.spinner("Generate QR Code"):
            time.sleep(3)
        generate_qrcode(url)
        st.image("images/qrcode_streamlit.png",
                 caption="Here is the qr code")

    st.markdown("Made by Tami 🩷")