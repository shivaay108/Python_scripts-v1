# To take args from the user we can take args parse 
import argparse as ap

parser = ap.ArgumentParser()
# declare args
parser.add_argument("name" , type=str)
parser.add_argument("age" , type=int)


args = parser.parse_args()
fullname = args.name(0,5)
print(fullname)
print(args.name , args.age )


