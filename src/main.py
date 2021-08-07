"""Main Application Entrypoint

This file serves as the main entrypoint for the application.
"""

from sme_app import sme_app
import streamlit as st

def main():
    """
    The main entrypoint for the application. It sets some basic Streamlit configuration data for the application and
    loads the Streamlit view containing the entire app.
    """
    st.set_page_config(page_title="SME Database", layout="wide", initial_sidebar_state="expanded")

    sme_app() # The Main Application method... Everything to do with application logic should be contained within

    return None

if __name__ == "__main__":
    main()
