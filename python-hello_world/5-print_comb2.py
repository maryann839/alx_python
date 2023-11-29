# numbers = range(10)
for i in range(99):
  print("{:02}".format(i), end=", " if i < 98 else "\n" )
