def raise_exception():
    raise TypeError("An Exception type")
try:
    raise_exception()
except TypeError as te:
    print("Exception has been raised")