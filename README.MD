##BEEPBOOPBOT

Hello, I am Deven! I am an avid coder, and I have been coding in python for 5 years. Before this section in AT Coding, I had no clue that Discord Bots could be coded in Python! After learning about some extra python functions, I started to play around with the bots and learned by experience.

BEEPBOOPBOT is a discord bot that can react and reply to requests and messages. BEEPBOOPBOT's given prefix is "$" but he will respond to some commands without it. his activators include:

@beepboopbot

$startx #creates new channel for you

// includes a entry in the array below 
["Hello","Hey","Hi","Howdy","Yo","WHAZZUP","G'DAY"]

responds BOOP to BEEP and if you type BOT after, it will celebrate

Clear function:
$clear -(insert number or a)	#clears your last number of messages, or last 50 (a) messages clear -a clear -5 clear -2

RICKROLL (1 out of 10000 messages)

The Beepboopbot function was not the hardest, but define hard because I started out not knowing about the channel.history function so I had to create an array and depending on how long it was, check if the user said BEEP and BOT and where in the array it is. but after I figured the channel.history, I cleaned it up and made it less problematic. The basics of the function follow: Take the last 5 messages, if the 3rd one is beep and the last one is bot, celebrate by sending emojis for the last 10 messages.

The $startx function was really cool because Startx is an actual function in linux that startx a virtual desktop(vs cli). What it does is finds who sent the message (message.author) and it creates a new channel with their name. Then it adds their name and channel-id (as a two long list called tuple) and only responds to commands if the name corresponds with the channel-id. And then it messages this:
("[{0.author.name}@".format(message)+message.guild.name+" **~**]$ ")
This is for example if I said $startx, it would create a new channel and send Hackerman@()