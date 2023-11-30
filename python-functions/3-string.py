def reverse_string(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reverse_str 
    return reversed_str

