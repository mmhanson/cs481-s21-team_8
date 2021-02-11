# Meeting 4

- Attendance: Everyone present

We decided for our project, we will use a docker container to handle our build scripts. We gathered the dependencies necessary for our tech lab discord bot run and any more we think we may need in the future such as the requests library to handle external API requests. Then Forrest installed docker on a new virtual machine and began to build the docker container. To build we simply will spin a new container up.

We started looking into ways to host our application. We found that Heroku is a pretty common hosting platform for a lot of discord bots that are currently active. We also found that heroku is able to handle docker containers. If we decide to use any form of a backend database, heroku provides free sql backends such as clearDB to be able to hold any information our bot might need in the future. 

My task for this week:
- Look into what other dependencies our container may need in the future
- Look into other hosting platforms that can handle docker containers
- Start thinking about what information our bot will need to hold in order for our application to work successfully.

