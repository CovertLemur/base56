import sys
import random
import string

def help_menu():
    help_message = 'python3 b56.py [Length of String to Output]'
    print("Usage:")
    print("-" * len(help_message))
    print(help_message)

def check_input():
    help_arguments = ['-h', '--help']
    if sys.argv[1] in help_arguments:
        help_menu()
        exit(1)
    else:
        try:
            sys.argv[1] = int(sys.argv[1])
            return sys.argv[1]
        except ValueError:
            print("Input was not valid.\n")
            help_menu()
            exit(0)

def random_string():
    string_length = check_input()
    all_characters = string.ascii_letters + string.digits
    ignored_characters = '0OoIl1'
    output = ''
    for s in range(string_length):
        output += random.choice([s for s in all_characters if s not in ignored_characters])
    print(output)

def run():
    check_input()
    random_string()

if __name__ == "__main__": 
    run()
