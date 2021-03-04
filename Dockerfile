FROM centos:7

RUN yum -y install python3-devel
RUN yum -y install gcc
RUN pip3 install -U python-dotenv
RUN pip3 install requests
RUN pip3 install discord.py
RUN pip3 install git+https://github.com/sean-keisuke/distest.git
