FROM ubuntu:14.04
MAINTAINER Dave
RUN apt-get -qq update
RUN apt-get -qqy install wget python
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN rm get-pip.py
# Or use requirements.txt
RUN pip install WebOb Werkzeug webapp2

# TODO
# Clone code from Github
