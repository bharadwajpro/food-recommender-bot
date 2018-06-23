from random import randint
import sys

if len(sys.argv) == 3:
    print('Here you go', randint(int(sys.argv[1]), int(sys.argv[2])))
else:
    print('Sorry I don\'t know')
