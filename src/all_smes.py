import json
import streamlit as st

def page_body():
    """
    A method representing the "body" of the page, in this case a list of all SMEs in the application
    """
    st.header("All SMEs")

    subject_matter_experts = json.load(open('mocks/subject_matter_experts.json'))

    for subject_matter_expert in subject_matter_experts:
      beta_expander_title = subject_matter_expert['name'] + ' - ' + str(subject_matter_expert['age']) + ' years old'

      with st.beta_expander(beta_expander_title):
        if subject_matter_expert['jobTitle']:
          st.subheader("Job Title")
          st.write(subject_matter_expert['jobTitle'])

        if subject_matter_expert['companyName']:
          st.subheader("Works At")
          st.write(subject_matter_expert['companyName'])

        st.subheader("Personal Summary")
        st.write(subject_matter_expert['personalSummary'])
