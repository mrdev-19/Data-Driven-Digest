import streamlit as st
import os
from deta import Deta
from dotenv import load_dotenv
import base64
from streamlit_card import card

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
st.text_input("")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

icon("search")
selected = st.text_input("", "Search...")
button_clicked = st.button("OK")


hasClicked = card(
  title="Demo Card!",
  text="Some description",
  image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTF9W9vwDNn5X7zAVeDHXgUKo0nBy0pqCaDcw&s",
  url="https://www.linkedin.com/in/mrdev19/"
)