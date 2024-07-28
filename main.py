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

#--------------------------------------------------
#hide the header and footer     

hide_ele="""
        <style>
        #Mainmenu {visibility:hidden;}
        footer {visibility:hidden;}
        header {visibility:hidden;}
        </style>
        """
st.markdown(hide_ele,unsafe_allow_html=True)
#---------------------------------------------------
st.header("This page has articles and tutorials :)")