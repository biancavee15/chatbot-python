import random
import time
import os

name = "Chatty"
weather = "sunny"
greetIn = ["hello", "hi", "sup", "hey"]
nameIn = ["what is your name", "name"]
describeIn = ["what are you"]

greetOut = ["hello friend", "hi there"]
nameOut = ["my name is Chatty", "I'm Chatty"]
describeOut = ["I'm Chatty a chatty chatbot"]
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
print 'Chatty is listening'
while True:
    message = input('=>')
    mesLower = message.lower()
    if message == '':
        print '>>> See you later!'
        time.sleep(1)
        os.system("sudo shutdown -h now")
    elif mesLower in nameIn:
            print '>>>' + (random.choice(nameOut))
    elif mesLower in greetIn: 
            print '>>>' + (random.choice(greetOut))
    elif mesLower in describeIn:
            print '>>>' + (describeOut)
