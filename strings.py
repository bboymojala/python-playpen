#Take the first command line argument to your script and transform it in the following ways:

#Convert it to all upper case letters
#Append three exclamation points

#After you transform the string in this way, print the new string to the console.

import string # not needed?
import sys

input = sys.argv[1]
output = input.upper() + '!!!'

print(output)
