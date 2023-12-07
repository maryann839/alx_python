def no_c(my_string):
    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
    result= ""
    for char in my_string:
      if char.lower() != "c":
         result += char
          
    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
    return result
