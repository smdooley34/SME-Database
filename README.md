<div align="center">
  <h1>SME Database</h1>

  <h4>
    HCI 584X Project About Creating A Python Application To Allow A User To See Subject Matter Experts (SMEs) In A
    Helpful Way.
  </h4>
</div>

## Summary
This project is certainly a work-in-progress in concept, but my vision for it is to serve as a visualization tool of
sorts for finding SMEs in various fields or subject matters. I suppose for now the "data" pertaining to each SME will be
considered mock data, but I am also imagining that this will eventually come from an external database endpoint of some
kind. What I mean by this is take, for example, if Wikipedia was your "database" of people, then we could create our own
database from such an external database.

## Project Update (June 21st, 2021)
For the last several times I've worked on this project, I've been going over in my head how best to proceed with a
graphical user interface for the SME database. I decided to go with Python's built-in Tkinter library, as it is pretty
simple and straightforward to use.

I only have what is shown in the screenshot below working. That is, the base GUI and layout along with the displaying
of the mock data I created last time. I will certainly still need to implement the logic around user input, and the
resulting display of relevant data based on that input. I will also still need to brainstorm how I'm going to be
getting real live data back from some sort of internet endpoint. I'm not sure if I'll have enough time to carry the
project all the way through the way I had originally conceived, with all of this considered.

### Some Potential Milestones & Self Reflection
* Hook Up User Input To Results
* Bring In Live Data From An Endpoint Rather Than Mock Data
* Improve The General GUI

As I stated above, while I am unsure if I will be able to carry the project all the way through completion the way I
originally wanted to, I am altogether pleased. I've learned quite a bit about Python in general so far and am
starting to understand how to read APIs and libraries to incorporate them into my own programs.

![img.png](screenshots/screen_one.png)

## IDE/Project Setup
I'll be using JetBrains' [PyCharm](https://www.jetbrains.com/pycharm/) Community Edition to develop code for this
project. I will of course be utilizing [Git](https://git-scm.com) and [GitHub](https://github.com/) for version control.

You will also need a [Python](https://www.python.org/) interpreter. I will be using the latest version (3.9.5 as of
this writing). Now, from your command line:

```bash
# I Just Create A `Scratch` Directory At The Top Level Of My OS
cd /
mkdir Scratch && cd Scratch

# Clone The Repository
git clone https://github.com/smdooley34/SME-Database.git 
```

## Project Architecture
As of now, I'm thinking of making this a very simple query page that allows a user to search, in various ways and by
various attributes, SMEs. The app displays a window GUI using Python's builtin
[Tkinter](https://docs.python.org/3/library/tkinter.html) interface.
