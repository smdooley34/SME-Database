<h1>User Guide</h1>

<p>
    <a href="#Requirements">Requirements</a> •
    <a href="#Installation">Installation</a> •
    <a href="#Known-Issues">Known Issues</a>
</p>

This project is about connecting Subject-Matter Experts (SMEs) and displaying them in a way that could be helpful,
intuitive, and powerful for other users of the site, whether academic, professional, or just a user interested in
finding experts in subjects they are interested in.

## Requirements
* Latest Version Of [Python](https://www.python.org/) (3.9.6 As Of This Writing)
* Latest Version Of [Streamlit](https://docs.streamlit.io/en/stable/) (0.86.0 As Of This Writing)

## Installation
The live site is hosted on [Streamlit Sharing](https://share.streamlit.io/smdooley34/sme-database/main/src/main.py) at
https://share.streamlit.io/smdooley34/sme-database/main/src/main.py

If you would like to build from source, follow these instructions:

From your command line:

```bash
# I Just Create A `Scratch` Directory At The Top Level Of My OS
cd /
mkdir Scratch && cd Scratch

# Clone The Repository
git clone https://github.com/smdooley34/SME-Database.git

# Run The Streamlit App By Running:
cd SME-Database/src/
streamlit run main.py
```

You will need to install the streamlit dependency so check the Streamlit website for more setup instructions if needed.

## Known Issues
* Database connection is down - would be top priority if there was an actual user base
* Private Google Firestore database key (allows anyone to read/write to the database) should not be publicly viewable.
