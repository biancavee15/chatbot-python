GREETING_KEYWORDS = ("hello", "hi", "what's up")
GREETING_RESPONSES = ["hello friend", "hi!", "what's up?"]
print("hello!")
sentence = raw_input("")
def check_for_greeting(sentence):
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return(random.choice(GREETING_RESPONSES))

