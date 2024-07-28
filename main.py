import streamlit as st
import os
from deta import Deta
from dotenv import load_dotenv
import base64


load_dotenv(".env")

def load_icon(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Load your icon from local storage
icon_path = "icon.png"
icon_base64 = load_icon(icon_path)

page_title="Data Driven Digest"
layout="centered"

st.set_page_config(page_title=page_title,page_icon="icon.png",layout=layout)
st.title(page_title)

st.header("This page has articles and tutorials :)")