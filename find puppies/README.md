# COMM113 First Bot
This bot takes your location as an argument and generates an HTML webpage of adoptable dogs near you. This was a bit of a departure from my original proposal, but I found that it would be hard for me to go with those ideas as Sunlight Foundation (whose API I was planning on using) was recently taken over by ProPublica, so their API is in a bit of a disarray at the moment.

Anyway, this bot uses two RescueGroups.org APIs, one to find the adoptable dogs based on a user-inputted location and one to identify the adoption shelter that a specific dog is currently at based on its organizational ID. I don't use any previously downloaded data as this API automatically pulls down the most recent information for user queries.

I also used Flask to build the HTML webpages, relying heavily upon the "First News App" tutorial, which is pretty apparent since I used the tutorial's CSS style on my own site.

The most difficult part of this project was most likely identifying the APIs that I would be calling for my bot and then reading the copious amounts of documentation to understand what search fields I'm supposed to include in my query. Also challenging was remembering the bits of CSS that I learned a few years ago, in order to make small adjustments to the tutorial's style.

The final product could obviously still use work. If I had more time to work on this, I would probably add the additional functionality of choosing the search criteria prior to making the API call. Doing so would likely involve me reading up on how to make Flask sites interactive, which I just didn't have time to do now given that it's dead week and I have another CS project due Friday. Overall, though, I had a lot of fun making this and hopefully you as the user will have some fun exploring what the bot is capable of!
