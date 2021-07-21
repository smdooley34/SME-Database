from google.cloud import firestore
import os
import streamlit as st

def page_body():
    """
    A method representing the "body" of the page, in this case a list of all SMEs in the application. Each SME card has
    information concerning a particular SME. This information consists of, for now, their name, title, workplace, and
    a personal summary that would be written by each SME. Data pulled in comes from a mock database set hosted in Google
    Cloud Firebase. This database has a graphical interface that allows users to perform quite complicated database
    interactions via a graphical interface. The actual database technology used here is Google Firestore, which itself
    is an implementation of Python's standardized Database API v2.0, making this simple to use with Streamlit and Python
    in general.

    @see https://console.firebase.google.com
    @see https://www.python.org/dev/peps/pep-0249/
    """
    st.header("All SMEs")

    # TODO store the secret firestore key in `Streamlit Sharing` itself and get streamlit secrets to work properly
    firestore_key_path = ".streamlit/firestore-key.json"

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = firestore_key_path
    db = firestore.Client().from_service_account_json(firestore_key_path) # Connect to the "SME" database on Firebase

    subject_matter_experts = db.collection(u"subject_matter_experts").stream()

    # Loop through the database collection of SMEs
    for subject_matter_expert in subject_matter_experts:
        subject_matter_expert_dict = subject_matter_expert.to_dict() # Convert internally to a Python dict

        # dict keys here are actually database keys in Firestore. You would need to be signed in to see the proper values
        with st.beta_expander(subject_matter_expert_dict["name"] + " - " + str(subject_matter_expert_dict["age"]) + " years old"):
            st.header(subject_matter_expert_dict["name"])
            st.write(subject_matter_expert_dict["jobTitle"])

            st.subheader("Personal Summary")
            st.write(subject_matter_expert_dict["personalSummary"])

            if subject_matter_expert_dict["companyName"]:
                st.subheader("Works At")
                st.write(subject_matter_expert_dict["companyName"])

            if subject_matter_expert_dict["connections"]:
                st.subheader(subject_matter_expert_dict["name"] + "'s Connections")
                st.write(", ".join(subject_matter_expert_dict["connections"]))
