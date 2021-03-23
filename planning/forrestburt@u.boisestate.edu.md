# Forrest Burt

## User Story

As a developer of the Discord bot, I want to a have a unified and standardized way to push code to the Github repository and have it be propagated to the Heroku environment so that it can be deployed there. I also want to have a standard way to interact with the Docker/Heroku instances for maintenance or testing.

## Tasks

1. I will link the Github and Heroku repositories together in such a way that pushes made to the the master branch of the Github are deployed on Heroku. The devlopment branch should not have this functionality.
2. I will have the Heroku respository set up in such a way that the dynos that run the bot can be turned on and off from both the Heroku CLI and the Heroku webpage without duplication of bot instances occuring.
3. I will have a way of spooling up a local version of the bot via a local install of Docker and the Dockerfile in the repository, along with command available to interact with the bot inside the container (i.e. a bash shell).
4. I will have a way of interacting with the live production Heroku instance with the container running inside of it (i.e. a bash shell).
5. I will have a way of running the tester bot in an ancillary dyno so that we can perform automated testing on the primary bot using the tester bot we currently have.

### Time estimation method

Each of these tasks is approximately 8 hours of work. Getting this far with Heroku and Docker together has taken a long time, and there are a lot of different hurdles to get over as we find out more and more about these systems.

## Definition of Done

- Task 1 DOD - I will know that I am done when a bot developer can push code to the master branch and have it be automatically deployed to Heroku.
- Task 2 DOD - I will know that I am done when it is established that there is parity between the CLI dyno controls and the web interface dyno controls.
- Task 3 DOD - I will know that I am done when there is a standard set of commands that can take an environment from no Docker to Docker running with the local bot container.
- Task 4 DOD - I will know that I am done when there is a standard set of commands that allow a bot developer to interact directly with the production dyno.
- Task 5 DOD - I will know that I am done when the tester bot is being run in a dyno and is successfully testing the primary bot also running in a dyno.
