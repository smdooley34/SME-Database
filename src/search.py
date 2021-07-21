from enum import Enum
from google.cloud import firestore
import os
import streamlit as st

class SearchMode(Enum):
    Connection = 'Connection'
    JobTitle = 'Job Title'
    Name = 'Name'

def page_body():
    """
    A method representing the "body" of the page, in this case a search query page which allows the user to search for
    SMEs in the application using a variety of search filters.
    """
    st.header("Search")
    st.subheader("Search For SMEs With A Few Different Options")

    search_mode_selection = st.radio(
        help="Search For SMEs That Have Particular Connections, Titles, Or Names...",
        label="Search By",
        options=(SearchMode.Connection.value, SearchMode.JobTitle.value, SearchMode.Name.value),
    )

    search_form = st.form(key="search_form", clear_on_submit=False)
    search_query = search_form.text_input(label="", value="Search...", max_chars=50)
    search_button = search_form.form_submit_button(label="Search")

    if search_button:
        results = get_search_results(search_query, SearchMode[str(search_mode_selection).replace(" ", "")])

        # Loop through the results returned from the database query
        for result in results:
            result_dict = result.to_dict() # Convert internally to a Python dict

            # dict keys here are actually database keys in Firestore. You would need to be signed in to see the proper values
            with st.beta_expander(result_dict["name"] + " - " + str(result_dict["age"]) + " years old"):
                st.header(result_dict["name"])
                st.write(result_dict["jobTitle"])

                st.subheader("Personal Summary")
                st.write(result_dict["personalSummary"])

                if result_dict["companyName"]:
                    st.subheader("Works At")
                    st.write(result_dict["companyName"])

                if result_dict["connections"]:
                    st.subheader(result_dict["name"] + "'s Connections")
                    st.write(", ".join(result_dict["connections"]))

def get_search_results(search_query, search_mode):
    """
    Returns search results when the user clicks the submit button. This function returns results based both on the users
    input but also the selected search mode.

    :param search_query: a string containing the users input text for the query
    :param search_mode: the search mode of the query
    :return: a Generator of results based on the query
    """
    # TODO store the secret firestore key in `Streamlit Sharing` itself and get streamlit secrets to work properly
    firestore_key_path = ".streamlit/firestore-key.json"

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = firestore_key_path
    db = firestore.Client().from_service_account_json(firestore_key_path) # Connect to the "SME" database on Firebase

    if search_mode == SearchMode.Connection:
        return db.collection(u"subject_matter_experts").where(u"connections", u"array_contains", search_query).stream()

    elif search_mode == SearchMode.JobTitle:
        return db.collection(u"subject_matter_experts").where(u"jobTitle", u"in", [search_query]).stream()

    elif search_mode == SearchMode.Name:
        return db.collection(u"subject_matter_experts").where(u"name", u"in", [search_query]).stream()
