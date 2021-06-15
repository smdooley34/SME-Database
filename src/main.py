########################################################################################################################
# main.py
#
# Serves as the main entrypoint for the application. See the README for more details.
########################################################################################################################

import json

# Opens JSON File To Bring In Data (Mock Data, For Now, With Attributes That May Or May Not Really Be Useful)
file_handle = open('mocks/subject-matter-experts.json')

# Returns JSON Object As A Dictionary
subject_matter_experts = json.load(file_handle)

for subject_matter_expert in subject_matter_experts:
    print(subject_matter_expert)

file_handle.close()
