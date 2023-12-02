#a program that prints all possible combinations of two digits 
for tens in range(10):
    for units in range(tens + 1, 10):
        print("{}{}".format(tens, units), end=", " if units < 89 else "\n")
print()
