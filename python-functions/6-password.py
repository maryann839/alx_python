def validate_password(password):
    
    if len(password) < 8:
         return False
    has_upper = False
    has_lower = False
    has_digit = False
    
    for i in password:
            if i.islower():
                has_lower = True
            if i.isupper():
                has_upper = True
            if i.isdigit():
                has_digit = True
   
    if has_lower and has_upper and has_digit and not " " in password:
                return True
    else:
         return False
    
    
