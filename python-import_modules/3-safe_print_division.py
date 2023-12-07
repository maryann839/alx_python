def safe_print_division(a, b):
   try:
      result = a / b
   except ZeroDivisionError:
      print('Division by Zero is invald')
      raise
   except Exception as e:
      print('an error occured')
      return None
   else:
      print("indide result: {}".format(result))
      return result
   finally:
      pass
   #   print("{} / {} = {}".format(a, b, (a/ b)))
# a = 10
# b = 5
# result = safe_print_division(a, b)
# print("{} / {} = {}".format(a, b, (a/ b)))

# try:
#     x = 1 / 2
# except ZeroDivisionError:
#     print('Divided by zero.')
# else:
#     print('No exceptions raised.')
# finally:
#     print('This gets executed no matter what.')
