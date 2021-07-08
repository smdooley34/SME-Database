from enum import Enum

import streamlit as st

class SearchMode(Enum):
    Connection = 'Connection'
    JobTitle = 'Job Title'
    Name = 'Name'

def page_body():
    """
    A method representing the "body" of the page, in this case a search query page which allows the user to search for
    SMEs in the application using a variety of search filters
    """
    st.header("Search")
    st.subheader("Search For SMEs With A Few Different Options")

    search_mode_selection = st.radio("Search By", [mode.value for mode in SearchMode])

    search_form = st.form(key="search_form", clear_on_submit=False)
    search_query = search_form.text_input(autocomplete=search_smes_auto_complete(), label="", value="Search SMEs...", max_chars=50)
    search_button = search_form.form_submit_button(label="Search")

    if search_button:
        results = get_search_results(search_query, SearchMode[str(search_mode_selection).replace(" ", "")])

        for result in results:
            st.write(result)

def get_search_results(search_query, search_mode):
    """
    TODO Needs real search results - simply compare against mock JSON data

    Returns search results when the user clicks the submit button. This function returns results based both on the users
    input but also the selected search mode.

    :param search_query: a string containing the users input text for the query
    :param search_mode: the search mode of the query
    :return: an array of results based on the above parameters
    """
    if search_mode == SearchMode.Connection:
        return ['Result One', 'Result Two']

    if search_mode == SearchMode.JobTitle:
        return ['Result One', 'Result Two']

    if search_mode == SearchMode.Name:
        return ['Result One', 'Result Two']

def search_smes_auto_complete():
    """
    TODO Needs implemented

    Returns a suggested autocomplete result for the user so that they can speed up their searches.

    :return: a string autocomplete suggestion based on the users input text
    """
    return 'TODO'
