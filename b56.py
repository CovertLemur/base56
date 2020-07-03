#!/usr/bin/env python3

import sys
import random
import string

stringLength = int(sys.argv[1])
def randomString(stringLength):
    charactersAll = string.ascii_letters + string.digits
    charactersIgnore = '0OoIl1'
    print( ''.join(random.choice([s for s in charactersAll if s not in charactersIgnore]) for i in range(stringLength)) )

if __name__ == "__main__": 
    randomString(stringLength)
