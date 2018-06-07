import random
from flask import Flask, render_template, request, jsonify
app = Flask(__name__, static_url_path='')

# print("hello")

name = "Chatty"
weather = "sunny"
responses = {
    "What's your name": [
        "my name is {0}".format(name), 
        "hi, i'm {0}".format(name), 
        "they call me {0}".format(name)
    ],
    "How are you":[ 
        "Doing well",
        "kinda sad",
        "very very excited!"
    ],
    "what's the weather today":[
        "It's {0} today!".format(weather),
        "The weather is {0}".format(weather)
    ],
    
    "default": "My name is {0} Ask me anything you want".format(name)
}


def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else: 
        bot_message = responses["default"]
    return bot_message


@app.route('/')
def root():
    return render_template('index.html')

# for serving JS https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask

@app.route('/message/<msg>')
def get_msg(msg):
    # return msg
    return respond(msg)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')