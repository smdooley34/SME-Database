import streamlit as st

import all_smes
import search

ApplicationPages = {
    "All SMEs": all_smes,
    "Search": search
}

def sme_sidebar():
    """
    A method representing the sidebar for the application, containing the `About` and `Navigation` sections (possibly
    more sections in the future)
    """
    st.sidebar.header("About")
    st.sidebar.subheader("Welcome to the SME Database! This application is designed to help you search for subject"
                         "matter experts (SMEs) that you may need or find useful in your academic or professional "
                         "projects.")

    st.sidebar.header("Navigation")

    selection = st.sidebar.radio("Pages", list(ApplicationPages.keys()))
    page = ApplicationPages[selection]
    page.page_body()
