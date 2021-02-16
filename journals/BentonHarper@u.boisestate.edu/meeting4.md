# Meeting 4

- Attendance: All were present

This week we discussed the best ways we could do the build.sh and clean.sh files for our discord bot, what exactly we'd have to do.
Since we're writing it in python, we discussed what pip installs and such we'd have to do, and eventually we decided we would run 
the whole thing in a docker container, so our build and clean files would just start and stop the container, we also had to add a
docker file that installed all the necessary things to run our bot. Forrest really did the most work with docker since he was most
experienced with it. We also discussed how we were going to run it on heroku and did some research for putting docker containers
on heroku.

My task for this week:

- Research docker to better understand how to run our bot
- Research heroku to be able to use it later on
- Keep researching how to write a discord bot
