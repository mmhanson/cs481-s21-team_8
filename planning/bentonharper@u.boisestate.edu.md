# Ben Harper

## User Story

As a developer of the Discord bot, I want to be able to submit requests
to the AudioDB database for information about the current song, so that
the information can be saved and accessed later so users can see a
list of played songs or the 'music taste' rankings when they type those 
commands.

## Tasks

1. I will get a token for the AudioDB and make sure I can make requests for a given track 
   and artist, as well as understand the response and pick out the information we need.
2. I will write the class to save song information, along with a function to add them to 
   a list, and print that list oldest song first.
3. I will write the code to save the song's like ratio with the user who requested it, 
   and use that to calculate each user's 'music taste' ratio and be able to print them out in
   order of 'best' to 'worst.'
4. I will combine my code from my test files with the main bot file so that the information
   can be displayed in Discord when users type certain commands.
5. I will write tests that will cover all the cases that affect my code and add it to our 
   main test file.

### Time estimation method

Each of my tasks is approximately 8 hours of work. This is based on talking with my 
team members, as well as extra time being alloted since I've never used Python, and 
the AudioDB has very minimal documentation, therefore I expect each task will take 
quite a bit of research and testing on top of the coding time. The time of my later 
tasks could decrease slightly, as I become more familiar with the language and the database.

## Definition of Done

- Task 1 DOD - I will know that I am done when I can successfully make a request to the
               database and print out the wanted information (title, artist, album,
               likes, and dislikes) for a song.
- Task 2 DOD - I will know that I am done when I can request multiple songs, then
               using the command to print them, they all have the correct information
               and are in the correct order.
- Task 3 DOD - I will know I am done when the song is correctly paired with the user
               that requested it, and it correctly averaged with their overall ratio,
               plus when the command is used, all users and their ratios are printed
               in order.
- Task 4 DOD - I will know I am done when all the above functionality can be ran through
               Discord, rather than a terminal.
- Task 5 DOD - I will know I am done after all my tests have been added to our GitHub
               Actions .yml file, and they pass every time it is ran.
