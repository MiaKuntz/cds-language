import argparse

# defining function
def input_parse():
    # initialize the parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--name", type=str, default="Kevin")
    parser.add_argument("--age", type=int, required=True)
    # parse the argument from command line
    args = parser.parse_args()
    # return arguments
    return args

# defining hello function
def hello(name, age):
    print("Hello, my name is " + name + "!")
    print("I am " + str(age) + " years old!")

# defining main function
def main():
    # run imput parse to get name
    args = input_parse()
    # pass name to hello()
    hello(args.name, args.age)

# only if the code is called from the command line, then run the main function
if __name__=="__main__":
    main()
