#!/bin/bash
#this is now the docker knowledgebase file - this file should only be run from inside the repo's main directory where this file is located with ./build.sh
#you can follow along by uncommenting the commands with a double pound sign in front, and replacing the hash notes below with the generated hash from the process
#the start command can be left uncommented once filled out to turn build.sh in a generic "take me to my local container" command
#in docker there are two entities we are concerned with: images and containers
#an image is a template for containers and is built from a Dockerfile with the command:
##docker build -t music-bot-container .
#in this case, it creates an image called "music-bot-container"
#when this build command executes, it runs the commands in the Dockerfile programmatically
#so, it pulls a python image, creates a working directory called /code, installs the necessary packages, copies the files from current directory into /code, and then copies the .env file into /code
#when this is done, the "docker images" command can be used to see all current images
#there should be one called "music-bot-container"
#from here, we can create infinite hypothetical containers from this image
#these are disposable, one-off environments that we can use to interact with instances of the bot locally
#to create an image, the "docker create" command is used:
##docker create -t -i music-bot-container bash
#the -t option tells docker to allocate a pseudo-TTY connection (a bash shell that we can connect to) and the -i option tells docker to "keep STDIN open even if not attached" which I'm not 100% sure them eaning of but I believe is essentially saying continuing taking terminal input into the pseudo-TTY
#the "docker create" command will print out a hash that represents the container in ID form - this can then be used to shell into the container with:
##docker start -a -i <first 10 or so container hash characters>
#the -a option attaches STDOUT/STDERR and -i attaches STDIN
#so just copy the first 10  or so digits of the hash into the end there and the container will start and place you into an interactive shell inside of the /code working directory
#from here you can run the bot by navigating to the main.py file and running it with python - bot will start normally and come online
#you can exit the container and return to your normal terminal by running "exit"
#to get back into the container, just run the start command again
#this instance of the container is persistent - you can add files and make changes and it should keep them between exits (but I HIGHLY recommend backups)
#to view all containers you've created, run "docker ps -a"
#to stop the container, run:
##docker stop <first 10 or so container hash characters>
#to remove the container entirely (which will require creating a new one again starting with the "docker create" command and will delete all local changes inside the container, run:
##docker container rm <first 10 or so container hash characters>
