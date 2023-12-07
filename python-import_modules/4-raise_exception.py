def raise_exception():
    raise NameError("An exception type")

try:
    raise_exception()
except NameError as ne:
  print("Exception has been raised")
