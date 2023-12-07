import sys

def display_arguments():
    num_arguments = len(sys.argv) - 1 
    # plural = 's' if  num_arguments != 1 else ''
    print("{} argument{}{}".format(num_arguments, 's' if  num_arguments != 1 else '' , '.' if num_arguments == 0 else ':'))
   
  
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
if __name__ == "__main__":
    display_arguments()