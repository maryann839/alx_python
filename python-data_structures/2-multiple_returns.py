def multiple_returns(sentence):
    if not sentence:
       return 0, None
    else:
        return(len(sentence), sentence[0])
   
    
# print("length: {} - First character:{}".format(len, sentence))
  