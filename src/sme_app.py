"""SME App

This file contains one method that represents, when called, the main SME application and streamlit view. It should
contain all high-level objects representing various main parts of the app.

This file contains the following methods:

    * sme_app - the main application method, as described above
"""

import streamlit as st

import all_smes
import search

ApplicationPages = {
    "All SMEs": all_smes,
    "Search": search
}

def sme_app():
    """
    A method representing the main application window, containing a sidebar with `About` and `Navigation` sections
    (possibly more sections in the future) and also one of a few selected pages to the right of the sidebar, dictated
    by the currently selected page (also housed in the sidebar).
    """
    st.sidebar.header("About")
    st.sidebar.subheader("Welcome to the SME Database! This application is designed to help you search for subject"
                         "matter experts (SMEs) that you may need or find useful in your academic or professional "
                         "projects.")

    st.sidebar.header("Navigation")

    # Build a radio button list out of the pages of the application, represented by the keys of the enum defined above
    selection = st.sidebar.radio("Pages", list(ApplicationPages.keys()))

    # Load the "page_body" method of the selected page, representing the arbitrary contents of that page
    page = ApplicationPages[selection]
    page.page_body()
