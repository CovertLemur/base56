import random
import string
import argparse

def args(): 
    parser = argparse.ArgumentParser(description='Script to make an unambiguous string.')
    parser.add_argument('-l', metavar='#', type=int, help='The length of the string to be generated.', dest='int_mode')
    args = parser.parse_args()
    return args

def random_string(string_length):
    all_characters = string.ascii_letters + string.digits
    ignored_characters = '0OoIl1'
    output = ''
    for s in range(string_length):
        output += random.choice([s for s in all_characters if s not in ignored_characters])
    print(output)

def run():
    random_string(args().int_mode)

if __name__ == "__main__": 
    run()
