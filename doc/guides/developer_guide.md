<h1>Developer Guide</h1>

<p>
    <a href="#Overview">Overview</a> •
    <a href="#App-Architecture">App Architecture</a> •
    <a href="#User-Flow">User Flow</a> •
    <a href="#Install">Install</a> •
    <a href="#Future-Work">Future Work</a>
</p>

## Overview
This project source code represents the frontend code for a "SME Database" project, which is about creating a website
where academics, professionals, and any other interested users can discover and search for Subject-Matter-Experts (SMEs)
in a helpful and intuitive way.

The frontend code here is written in Python and utilizes the Streamlit web development framework, to allow for a
relatively easy JavaScript-esque development experience. For a backend, we are using Google Firestore, a Google Cloud
based NoSQL database. The database has a visual experience on [Google Firebase](https://firebase.google.com), making
for exceptionally easy management. For now, this database is linked to a personal Google account, but database
interactions are enabled via the private key stored in `src/.streamlit`. To gain access to the Firebase, you would
require access (for now) to that Google account, unfortunately. Migrating to an organization-hosted account could
certainly be a TODO, along with hiding the private key used to connect to Firestore.

## App Architecture
The main application entrypoint is called, logically, `main.py`. In it, the base Streamlit configuration is set and the
main application Streamlit "component" is called. All frontend code that represents the Streamlit application is
contained in the call to the `sme_app()` method defined in `sme_app.py`.

For now, the entire application consists of a left-oriented sidebar and the main page to the right of that sidebar. The
page displayed to the right of the sidebar is dictated by the associated control located within said sidebar.

The application is organized such that it was intended to be relatively easy to add components, views, options, etc.
Usually, this takes the form of easily-scalable data structures like enumerations, allowing for easy additions. Main
pages; of the app should have their main methods called `page_body()`. This is to allow for easy scaling using the
controlling logic in the sidebar.

As stated before, Firestore is by nature a NoSQL database and so queries to the backend take the form of NoSQL queries.
I would highly recommend reading about [NoSQL](https://en.wikipedia.org/NoSQL) if you are unfamiliar. To query the
database, you can use the general framework outlined in `search.py`. You use (for now, again) the private key stored
in the repository to establish a connection using the Python API provided by Google. You can then retrieve data
asynchronously from the main database table by simply querying using simple NoSQL syntax.

Beyond some learning curve with Streamlit and Firestore, I believe the application is in such a state that it should be
relatively straightforward to scale the app in complexity and capabilities.

Finally, the application is hosted on [Streamlit Sharing](https://streamlit.io/sharing/smdooley34/sme-database/main/src/main.py).
However, there is currently an issue with the database connection on the hosted site, certainly a TODO.

## User Flow
The main flow of the application would be in my view, like a library. Users can view other users on the application via
the `All SMEs` page, but other pages and parts of the application would aid in the discovery of interesting metadata of
those users. In other words, this would hopefully become quite a bit more useful if we have many users with a decent
amount of metadata collected on each.

For now, the user can search via several modes, with each mode representing a query of different metadata associated
with users registered on the application such as Name, SME Connections, Job Title, etc.

My idea would be to vastly increase the number and ways with which the user could see and search other SMEs' data.
This data should of course not consist of anything too personal, and be purely professional in nature. Addresses and
phone numbers should be strictly professional, in other words. There would be quite a few links to other pages and
links to the states of those pages as well. For example, there could be names hyperlinked to search queries. While I
did not have the development time necessary to complete such functionality, I don't imagine them being all that hard
to develop with Streamlit.

## Install
Ideally, I would recommend any potential developers develop on the same IDE and platform to avoid any inconsistencies.
I have been using JetBrains' [PyCharm](https://www.jetbrains.com/pycharm/) Community Edition to develop code for this
project. [Git](https://git-scm.com) and [GitHub](https://github.com/) for version control are requirements.

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

## Future Work
There are quite a few TODOs in the project from limited development time. Chiefly, there exists an issue with the
Streamlit Sharing-hosted site where the application is unable to properly utilized the private Firestore key and
establish a proper database connection. Another TODO takes the form of not storing the private key in version control
at all, since it is best practice having the key be a private environment secret. Modifying Streamlit Sharing Secrets
to work properly would be the route here.

Also take note of the vision I outlined above for how development of application features should probably proceed.
