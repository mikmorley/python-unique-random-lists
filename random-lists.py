# Python Random Lists Generator
# -----------------------------
# Description:
#     Generates lists of unique random (alphanumeric|alpha|numeric) strings from argument defined specifications.
#     Purpose to be used as auxilary unique random string generation, or stand alone unique list generation for data population.
#     Each value generated is unique within the outputted list.
# Author: Michael Morley
# Github: https://github.com/mikmorley
# Website: https://michael.morley.cloud

import random
import string
import sys

def argument_help():
    print("")
    print("The following arguments must be defined:")
    print("")
    print("    --count\tTotal count of unique random strings to be generated.")
    print("    --length\tThe length of each unique random string.")
    print("    --uppercase\tDefines if random string should include Uppercase letters. y/n")
    print("    --lowercase\tDefines if random string should include Lowercase letters. y/n")
    print("    --numbers\tDefines if random string should include Numbers. y/n")
    print("")
    print("     python random-lists.py --count <number> --length <number> --uppercase <y/n> --lowercase <y/n> --numbers <y/n>")
    print("")
    print("e.g. python random-lists.py --count 10 --length 24 --uppercase n --lowercase y --numbers y")
    print("")
    sys.exit()

# Checking valid arguments are set.
if len(sys.argv) < 11:
    argument_help()
else:
    try:
        count_idx = sys.argv.index("--count")+1
        length_idx = sys.argv.index("--length")+1
        uppercase_idx = sys.argv.index("--uppercase")+1
        lowercase_idx = sys.argv.index("--lowercase")+1
        numbers_idx = sys.argv.index("--numbers")+1

        arr_length = int(sys.argv[count_idx])
        str_length = int(sys.argv[length_idx])

        if sys.argv[uppercase_idx] == "y":
            has_uppercase = True
        else:
            has_uppercase = False
  
        if sys.argv[lowercase_idx] == "y":
            has_lowercase = True
        else:
            has_lowercase = False

        if sys.argv[numbers_idx] == "y":
            has_numbers = True
        else:
            has_numbers = False

    except:
        argument_help()



# Function to generate a random value based on parameters
def generate_random(str_length, has_uppercase, has_lowercase, has_numbers):
    if has_uppercase and has_lowercase and not has_numbers:
        random_str_req = string.ascii_uppercase + string.ascii_lowercase
    elif has_uppercase and has_numbers and not has_lowercase:
        random_str_req = string.ascii_uppercase + string.digits
    elif has_lowercase and has_numbers and not has_uppercase:
        random_str_req = string.ascii_lowercase + string.digits
    elif has_lowercase and not has_uppercase and not has_numbers:
        random_str_req = string.ascii_lowercase
    elif has_uppercase and not has_lowercase and not has_numbers:
        random_str_req = string.ascii_uppercase
    elif has_numbers and not has_lowercase and not has_uppercase:
        random_str_req = string.digits
    else:
        random_str_req = string.ascii_uppercase + string.ascii_lowercase + string.digits
    x = ''.join(random.choice(random_str_req) for _ in range(str_length))
    return x

# Function to build list of unique randoms based on parameters
def build_list(str_length, has_uppercase, has_lowercase, has_numbers, arr_length):
    i = 0
    unique_values = []
    while i < arr_length:
        
        # Generate initial random value
        value = generate_random(str_length, has_uppercase, has_lowercase, has_numbers)

        # Set iteration constraints
        value_exists = 0
        value_check_count = arr_length
        k = 0

        # Continue iteration until a value that is not present in the list is generated.
        # To prevent infinite iterations, only sub-iterate for the maximum list length.
        while value_exists == 0 and k < value_check_count:
            if value not in unique_values:
                # If value is not present in list, append to list.
                unique_values.append(value)
                value_exists = 1
            else:
                # Value is present in list, a new random value is to be generated, and uniqueness checked again.
                value = generate_random(str_length, has_uppercase, has_lowercase, has_numbers)
                k = k+1

        i = i+1

    return unique_values


# Return the list of unique
list_of_uniques = build_list(str_length, has_uppercase, has_lowercase, has_numbers, arr_length)

# Output List
for value in list_of_uniques:
    print(value)

# Exit after output
sys.exit(0)