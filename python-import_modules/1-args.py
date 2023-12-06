import sys

def display_arguments():
    num_arguments = len(sys.argv) - 1 
    print("{} argument{}:".format(num_arguments, "s" if  num_arguments != 1 else ''),  end="")
    print()
  

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(1, arg))
if __name__ == "__main__":
    display_arguments()