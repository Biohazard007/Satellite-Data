import streamlit as st
from multiapp import MultiApp
from apps import (

    timelapse,
    
)

st.set_page_config(layout="wide")


apps = MultiApp()

apps.add_app("Create Timelapse", timelapse.app)


# The main app
apps.run()
