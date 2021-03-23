# Meeting 7

- Attendance: All in attendance

This week we all met to discuss the first parts of our individual feature development tasks. Sean has got things setup so we can hit the Spotify API endpoint and get information about songs, which is really cool to see. Ben has got TheAudioDB's API also up and running, and showed us some code he wrote that allows us to now "play" songs in the Discord chat and get data per user about musical tastes, which was also really neat to see working. I explained the latest updates to the Heroku system, including our new integration between Github and Heroku so that parity is maintained between the two repositories: the one on Github, and the one internal to the Heroku deployment.

My tasks for the coming week:

- Run tests on the Heroku-Github deployment to ensure that code pushed to the master Github branch deploys correctly as a Docker container
- Start working on figuring out what Heroku seemingly has two versions of the bot spooled up, one controlled via the CLI and one controlled via the web interface
- Get Docker instructions out to group
