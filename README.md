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
various attributes, SMEs. The app will display via the command line but also via a GUI down the line I think. This may
take the form of some simple HTML or possibly with the help of a simple framework like Django?
