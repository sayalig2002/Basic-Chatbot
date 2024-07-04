import re

import long_responses
import long_responses as long


def msg_proba(user_msg, recognized_words, single_response=False, required_words=[]):
    msg_certainty = 0
    has_required_words = True

    for word in user_msg:
        if word in recognized_words:
            msg_certainty += 1

    percentage = float(msg_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_msg:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_all_msg(msg):
    highest_proba_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_proba_list
        highest_proba_list[bot_response] = msg_proba(msg, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'holla', 'yoo'], single_response=True)
    response("I'm doing extra fine and you?", ['how', 'are', 'you', 'doing'], required_words=['how'])
    response(long_responses.H_feelings, ["do", 'you', 'have', 'feelings'], required_words=['you', 'feelings'])
    response(long_responses.fav_sport, ["what", 'is', 'your', 'favourite', 'sport'], required_words=['you', 'sports'])

    best_match = max(highest_proba_list, key=highest_proba_list.get)
    # print(highest_proba_list)
    return long.unknown() if highest_proba_list[best_match] < 1 else best_match


def get_response(user_input):
    split_msg = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_msg(split_msg)
    return response


# Testing the response system


while True:
    print("Bot: " + str(get_response(input('You: '))))

