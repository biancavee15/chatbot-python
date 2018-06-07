import random
import time
import os

# name = "Chatty"
# weather = "sunny"
greetIn = ["hello", "hi", "sup", "hey"]
nameIn = ["what is your name", "name"]
describeIn = ["what are you"]
favColorIn = ["whats your favorite color", "fav color"]

greetOut = ["hello friend", "hi there"]
nameOut = ["my name is Chatty", "I'm Chatty"]
describeOut = ["I'm Chatty a chatty chatbot", "a bot obviously"]
favColorOut = ["green", "pink", "orange", "holo"]
# responses = {
#     "What's your name?": [
#         "my name is {0}".format(name), 
#         "hi, i'm {0}".format(name), 
#         "they call me {0}".format(name)
#     ],
#     "How are you":[ 
#         "Doing well",
#         "kinda sad",
#         "very very excited!"
#     ],
#     "what's the weather today?":[
#         "It's {0} today!".format(weather),
#         "The weather is {0}".format(weather)
#     ],
    
#     "default": "My name is {0} Ask me anything you want".format(name)
# }

print('Chatty is listening')

while True:
    message = raw_input('>>> ')
    # print(message)
    mesLower = message.lower()
    if message == '':
        print('>>> See you later!')
        time.sleep(1)
    elif mesLower in nameIn:
        print '>>>' + (random.choice(nameOut))
    elif mesLower in greetIn: 
        print '>>>' + (random.choice(greetOut))
    elif mesLower in describeIn:
        print '>>>' + (random.choice(describeOut))
    elif mesLower in favColorIn:
        print '>>>' + (random.choice(favColorOut))
    else:
        print ("Sorry, I don't understand") 
