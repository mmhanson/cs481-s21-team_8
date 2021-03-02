# Meeting 6

- Attendance: All were present

This week we spent our time setting up the CI lab, we did some research into GitHub Actions for python code and made some tests based
one some sample files we found. We then were also able to get the status badge in our README working, but it's still failing becuase
we realized that our tests can't actual build and run our bot because we can't post the token on GitHub. We also had a problem when we
divided our code into two sections, build and test. They initially were running simulataniously, which caused errors, but with a little
more research we found the code to make test wait for build to finish. Other than that, this meeting went smoothly.

My task for this week:

- Try to figure out how to let GitHub access our token without leaking it
- Keep researching how to write a discord bot
