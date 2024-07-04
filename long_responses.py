import random

H_feelings = "I don't have feelings I am a bot obviously"
fav_sport = "Bots cannot play sports, and I am one."


def unknown():
    response = ['Could you please re-phrase that?',
                "...",
                "I can't get you",
                "What does that mean?"][random.randrange(4)]
    return response
