# simple python program to take input as arguments from user
# To take args from the user we can take args parse 
# first import argparse , you can either use 
import argparse as ap
# calling the argument parser 
parser = ap.ArgumentParser()
# declare args
parser.add_argument("name" , type=str)
parser.add_argument("age" , type=int)


# after that we have to review all the args using parse_args()
args = parser.parse_args()

fullname = args.name(0,5)
print(fullname)
print(args.name , args.age )


# for usage check take_args.py -h 