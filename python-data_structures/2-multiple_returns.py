def multiple_returns(sentence):
    if not isinstance(sentence, tuple) or not sentence:
       return None
    length = len(sentence)
    first = sentence[0]
    return("length: {} - First character:{}".format(length, first))
    