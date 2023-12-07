def multiple_returns(sentence):
    if not isinstance(sentence, tuple) or not sentence:
       return None
    length = len(sentence)
    first = len(sentence[0])
    print("length: {} - First character:{}".format(length, first))
    