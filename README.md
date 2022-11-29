# About us...

Antonio Ramón Molina Milla, Ramón.

- [LinkedIn](https://www.linkedin.com/in/armolinamilla/)
- [Twitter](https://mobile.twitter.com/commiteatv)
- [Some info](https://armolina.github.io)

Javier Martinez Alcantara, Javi.

- [LinkedIn](https://www.linkedin.com/in/javier-martinez-alcantara/)
- [Twitter](https://twitter.com/JavierMarAlc)
- [Some info](https://jmaralc.github.io/)

# 🤠 Codurance Professional Python Series (CoPPS)

Welcome pythonistas! This is the **second** session of the 2022 CoPPS. As you might know the CoPPS are the series of articles,
meetings, videos and in general documentation generated at Codurance for the community. 

While in the previous season we focus in the three pillars of software architecture (patterns, testing and architecture), 
in this season we are approaching python from the professional perspective that we have in our daily experience. 
We are pretty aware of the benefit of coding in python and also the relevance of XP (extreme programming) so we tried to combine them
to provide tips, documentation and conversation that could rise the professionalism of the community. 

The topics we are going to treat during this season are:
- Usages and integrations of optional static typing in python [6 October 2022] [VIDEO](https://youtu.be/fgnXC2U9Xmc), [REPO](https://gitlab.com/jmaralc/static_typing_in_python)
- Pythonic testing [25 October 2022] [VIDEO](https://youtu.be/VCANk894hPY), [REPO](https://gitlab.com/jmaralc/testing_python_2022)
- Collections in python: best practices [10 November 2022] [VIDEO](https://www.youtube.com/watch?v=eK_xJH18Vig), [REPO](https://gitlab.com/jmaralc/collections_in_python)
- Parallelism: processes, threads and corutines [22 November 2022] [VIDEO](https://youtu.be/voBeGVwHY_k), [REPO](https://gitlab.com/jmaralc/concurrency_and_parallelism_in_python)
- **gRPC, an efficient alternative to connect our services** (this repo) [1 December 2022]

What we pretend here is to treat these topics in an elegant, applied and enjoyable way...and as rigorous as possible.

Our wish is that you enjoy and take some learnings home. The adventure could start just by cloning this repo.

⚠️ **IMPORTANT**⚠️
Review all the branches and try to follow the slides to understand the flow of the session.

# Motivation
We are really used to communicate and interconnect our different services with REST apis. This is just a possibility that
is based more in the simplicity and the widespread usage of these rather than any other parameter. Nonetheless sometimes 
we face situations were we need a boost of improvement in this communication. For these cases we have at hand the gRPC. 

gRPC follow the traditional efficiency of classic RPC but in a new fashion making use of protobuffers for serialization and 
HTTP/2 for establishing the communication. These two features consolidate gRPC as a viable possibility when we are connecting
our services and we need a boost.

In this session Ramon will drive us with his experience using this technology in production, so that you can take home a reference
to start using it in your projects. He will introduce a great example using Magic the Gathering card game, to show a possible
implementation where two services (a producer and a consumer) exchange information about the cards of the game.

# [Session slides](https://docs.google.com/presentation/d/1q-LAkZQdWfM2qvOlYh93W16v_ITFs2vsWvuTDtqD0gs/edit?usp=sharing)

# Setup

For this talk you will need python 3.10 in your computer. We will use poetry for installing the packages and keeping the virtual environment. So I recommend you to install it with:

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

Further information about installation [here](https://python-poetry.org/docs/#installation)

Once poetry is installed running a command is as simple as:
```commandline
poetry run 
```

# Global Goal

- Spread the knowledge of python
- Promote pythonistas awareness and adoption of good practices and technologies
- Present our professional experience with python
- Facilitate safe spaces for people to show and talk 

# Structure of the repository/project
In this repo we are going to find the next branches. Each branch matches a part of the presentation so staty tune and follow the presentation
provided above to be on track. The branches are:

- **main** -> this branch keep the code for the session.

# Special thanks to..
For the opportunity to share it with you:

[**CODURANCE**](https://codurance.com/)
