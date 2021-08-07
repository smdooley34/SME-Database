<div align="center">
  <h1>SME Database</h1>

  <h4>
    HCI 584X Project About Creating A Python Application To Allow A User To See Subject-Matter-Experts (SMEs) In A
    Helpful Way.
  </h4>

  [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/smdooley34/sme-database/main/src/main.py)
</div>

## Summary
This project is about creating a prototype website where academics, professionals, and any other interested users can
discover and search for Subject-Matter-Experts (SMEs) in a helpful and intuitive way. While the fully realized idea
would be to create a comprehensive website that displays a large amount of data in a myriad of different ways, the
prototype concerns getting base functionality working. Hopefully, this would be done in a way that scales well and
allows for the end-goal ideas to be implemented in a relatively straightforward manner.

## Project URLs
* SME Database (Hosted On Streamlit Sharing) - https://share.streamlit.io/smdooley34/sme-database/main/src/main.py
* SME Database (GitHub) - https://github.com/smdooley34/SME-Database - You're Here!
* Firestore Database (Must Be Signed In) - https://console.firebase.google.com/u/1/project/sme-database-65c6d

## Architecture
There are a few parts to this project. First and foremost is the usage of the Streamlit Python web development
framework as a frontend. While not as comprehensive as some frameworks, Streamlit's goal is to enable simple apps with
little code. The idea of Streamlit is to turn data scripts into rendered units.

The application is hosted on the cloud via [Streamlit Sharing](https://streamlit.io/sharing). The gist of this
functionality is that Streamlit looks for a configured repository and loads the set application entrypoint file, in this
case `main.py`.

Here is a screenshot of the projects' Cloud Firestore:
![img.png](screenshots/screen_three.png)
As you can see, there is a nice GUI which allows one to create or otherwise import data. This database can be accessed
based on a private key that is included in the projects source code for easier code. I struggled to get
[Streamlit Secrets](https://blog.streamlit.io/secrets-in-sharing-apps/) to work properly for some reason. However, if
this were in a "production" environment, we would certainly not want to be handing out the private key to the database
to everyone.

In Firestore, you can see that one can create collections and documents. As their names suggest, collections are sets
of documents and documents can be thought of as generic "objects" in a collection. The documents contain the actual
fields and data pertaining to a database entry. This can be queried and otherwise interacted with quite easily with
Google's Python APIs.

The frontend site talks to a backend database that is hosted on the cloud via [Google Firebase](https://firebase.google.com).
On Firebase, I created a Google Firestore database that holds mock data for the application. This is connected to my
personal Gmail account (from which I will include screenshots to show how it works). Firestore is then configured in the
frontend code to talk to this Firestore database. Firestore supports various query operations and also has first-class
support for Streamlit, making development easier.

## Project Update (June 21st, 2021)
For the last several times I've worked on this project, I've been going over in my head how best to proceed with a
graphical user interface for the SME database. I decided to go with Python's built-in Tkinter library, as it is pretty
simple and straightforward to use.

I only have what is shown in the screenshot below working. That is, the base GUI and layout along with the displaying
of the mock data I created last time. I will certainly still need to implement the logic around user input, and the
resulting display of relevant data based on that input. I will also still need to brainstorm how I'm going to be
getting real live data back from some sort of internet endpoint. I'm not sure if I'll have enough time to carry the
project all the way through the way I had originally conceived, with all of this considered.

## Project Update (July 7th, 2021)

### Self Assessment
For the last several weeks, I've been going over the feedback I received and decided to switch up the platform for the
SME application from the way I originally conceived it. I'll be using, based on an in-class suggestion, to use
Streamlit. While it has been a struggle learning both the ins-and-outs of Python and Streamlit, I believe I'm making
decent progress, especially after moving away from the far simpler Tkinter.

### Major Updates
* Moving to Streamlit
* Adding more extensive mock data with more planned
* Making the application be a multi-page web app for flexibility

### Next Steps
* Flesh out the entire application, as broad as that is. I'd like to have each page of the application link to different
  parts of the app
* Implement missing features such as an actually functional search feature (shouldn't actually be hard, I think)
* Think of more features and pages to add to the application as a whole to make the whole thing seem useful and coherent

I don't believe I'll need any particular help yet:)

![img.png](screenshots/screen_two.png)

## IDE/Project Setup
I'll be using JetBrains' [PyCharm](https://www.jetbrains.com/pycharm/) Community Edition to develop code for this
project. I will of course be utilizing [Git](https://git-scm.com) and [GitHub](https://github.com/) for version control.

You will also need a [Python](https://www.python.org/) interpreter. I will be using the latest version (3.9.6 as of
this writing). Now, from your command line:

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
