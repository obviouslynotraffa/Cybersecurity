# Define a simple calculator.
# The user uses the terminal and it has three variables.
# - input1: first integer number
# - input2: second integer number
# - type of operation: a number associated to the operation
#    (e.g., 0 for the addition)


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--x1", type = int)
parser.add_argument("--x2", type = int)
parser.add_argument("--y", type = int)
args = parser.parse_args()

#usage example: python ex2.py --x1 1 --x2 2 --y 3


x1=args.x1
x2=args.x2
op=args.y


if op == 0:
    print(f" The sum is: {x1 + x2}")
elif op == 1:
    print(f"The sub is: {x1-x2}")
elif op == 3:
    print(f" The division is: {x1 / x2}")
elif op == 4:
    print(f"The product is: {x1 * x2}")


