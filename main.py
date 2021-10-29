from fastapi import FastAPI
import random

app = FastAPI()

jokes = [
    "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus.",
    "What do Alexander the Great and Winnie the Pooh have in common? Same middle name.",
    "I was horrified when my wife told me that my six-year-old son wasn't actually mine. Apparently I need to pay more attention during school pick-up.",
    "What is the opposite of a croissant? A happy uncle.",
    "If April showers bring May flowers, what do May flowers bring? Pilgrims.",
    "Which branch of the military accepts toddlers? The infantry.",
    "Did you know you can actually listen to the blood in your veins? You just have to listen varicosely.",
    "Though I enjoy the sport, I could never date a tennis player. Love means nothing to them.",
    "I have a joke about time travel, but I'm not gonna share it. You guys didn't like it.",
    "What's the opposite of irony? Wrinkly.",
    "I was kidnapped by mimes once. They did unspeakable things to me.",
    "Got a PS5 for my little brother. Best trade I've ever done!",
    "What do the movies Titanic and The Sixth Sense have in common? Icy dead people.",
    "I finally decided to sell my vacuum cleaner. All it was doing was gathering dust!",
    "When you die, what part of the body dies last? The pupils…they dilate.",
    "A friend of mine went bald years ago, but still carries around an old comb. He just can't part with it."
]

@app.get("/")
def read_root():
    joke = random.choice(jokes)
    return {"joke": joke}
