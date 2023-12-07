def safe_print_division(a, b):
   try:
      result = a / b
   except ZeroDivisionError:
      result = None
   finally:
      print("Inside result: {}".format(result))
      if result is not None:
         print("{} / {} = {}".format(a, b, result))
      # else:
      #    print("{} / {} = None".format(a, b))
      
   
# print("{} / {} = {}".format(a, b, (a/ b)))

