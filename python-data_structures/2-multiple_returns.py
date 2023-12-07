def multiple_returns(sentence):
    if not isinstance(sentence, tuple) or not sentence:
       return None
    length, first = multiple_returns(sentence)
    print("length: {} - First character:{}".format(length, first))
    