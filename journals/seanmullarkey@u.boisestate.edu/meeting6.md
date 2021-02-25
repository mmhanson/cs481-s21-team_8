# Meeting 6

- Attendance: Everyone present

We started to build out the continuous integration for our project. We set up our github actions to run a build and test job. The build job will run the build.sh script and the test job will run flake8 as well as run the test.sh script. We have no problems building out the project but the testing will fail because distest still has outdated packages. We don't quite know how to integrate .env variables within our github actions so we will need to look into doing that

My task for this week:
- Figure out how to use .env variables within github actions
- clean up code to make flake8 happy
- pressure the author of distest to make the framework compatible with Discord tokens generated in 2021


