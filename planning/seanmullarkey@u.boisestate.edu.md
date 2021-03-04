# Sean Mullarkey

**NOTE: Examples shown here would be considered C- (or lower) work.**

## User Story

As a user, I want to be able to connect to spotify, pick a song, and then play it on the discord interface. 

## Tasks

1. I will be able to connect to the spotify API by getting a valid token and checking to see if I can get valid HTTP Responses through get/post requests
2. Using the API connection, I want to be able to interact with the endpoint by using user input requests. Using command line arguments I will see if I can get valid JSON responses back
3. Once the API connection is established and I can get responses through user input, I will integrate this feature using discord messages instead.
4. Once the discord messages returns valid JSON, I then have to be able to actually use the media player functionality within discord to pass data into so it knows what songs to play
5. Finally I must write tests for all these features and ensure it passes. Integrate these tests within our existing testing files

### Time estimation method

The team estimates that each of my tasks is roughly 8 hours of work by comparing previous projects they have done that is similar to this one.

## Definition of Done

- Task 1 DOD - I will know that I am done if I established a connection if every request I make gets a 200-204 response.
- Task 2 DOD - I will know that I am done if a user input requests get back data I was expecting
- Task 3 DOD - I will know that I am done if a user requests data through discord and gets valid json back
- Task 4 DOD - I will know that I am done if I hear music coming from discord
- Task 5 DOD - I will know that I am done if all my tests pass.
