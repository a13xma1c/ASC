"""
A command-line controlled coffee maker.
"""

import sys
import string
import os

"""
Implement the coffee maker's commands. Interact with the user via stdin and print to stdout.

Requirements:
    - use functions
    - use __main__ code block
    - access and modify dicts and/or lists
    - use at least once some string formatting (e.g. functions such as strip(), lower(),
    format()) and types of printing (e.g. "%s %s" % tuple(["a", "b"]) prints "a b"
    - BONUS: read the coffee recipes from a file, put the file-handling code in another module
    and import it (see the recipes/ folder)

There's a section in the lab with syntax and examples for each requirement.

Feel free to define more commands, other coffee types, more resources if you'd like and have time.
"""

"""
Tips:
*  Start by showing a message to the user to enter a command, remove our initial messages
*  Keep types of available coffees in a data structure such as a list or dict
e.g. a dict with coffee name as a key and another dict with resource mappings (resource:percent)
as value
"""

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  #!!! when making coffee you must first check that you have enough resources!
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
commands = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

# Coffee examples
ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"

# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"

# Coffee maker's resources - the values represent the fill percents
RESOURCES = {WATER: 100, COFFEE: 100, MILK: 100}

"""
Example result/interactions:

I'm a smart coffee maker
Enter command:
list
americano, cappuccino, espresso
Enter command:
status
water: 100%
coffee: 100%
milk: 100%
Enter command:
make
Which coffee?
espresso
Here's your espresso!
Enter command:
refill
Which resource? Type 'all' for refilling everything
water
water: 100%
coffee: 90%
milk: 100%
Enter command:
exit
"""

# print("I'm a simple coffee maker")
# print("Press enter")
# sys.stdin.readline()
# print("Teach me how to make coffee...please...")
if __name__ == "__main__":
    print("I'm a smart coffee maker")
    while True:
        print("Enter command:")
        command = sys.stdin.readline().strip().lower()
        if command not in commands:
            print("not supported")
        else:
            if command == LIST_COFFEES:
                files = os.listdir("recipes/")
                for file in files:
                    print(file[:-4])
            elif command == MAKE_COFFEE:
                print("Which coffee?")
                available_types = [f[:-4] for f in os.listdir("recipes/")]
                coffee_type = sys.stdin.readline().strip().lower()
                if coffee_type not in available_types:
                    print("Choose from: ")
                    for t in available_types:
                        print(t)
                else:
                    f = open("recipes/" + coffee_type + ".txt", "r")
                    file_content = f.readlines()
                    not_enough = False
                    resource_copy = RESOURCES
                    for line in file_content[1:]:
                        usage_map = line.strip().split("=")
                        value = int(usage_map[1])
                        if RESOURCES[usage_map[0]] >= value:
                            RESOURCES[usage_map[0]] = RESOURCES[usage_map[0]] - value
                        else:
                            not_enough = True
                            print("Please refill %s" % RESOURCES[usage_map[0]])
                    if not_enough:
                        RESOURCES = resource_copy
                    print("Here's your %s" % coffee_type)
            elif command == REFILL:
                print("Which resource? Type 'all' for refilling everything")
                resource = sys.stdin.readline().strip().lower()
                if resource in RESOURCES.keys():
                    RESOURCES[resource] = 100
                    for k, v in RESOURCES.items():
                        print("%s: %s%%" % (k, v))
                elif resource == "all":
                    for k, v in RESOURCES.items():
                        RESOURCES[k] = 100
                        print("%s: %s%%" % (k, v))
                else:
                    print("Not a valid resource")
            elif command == RESOURCE_STATUS:
                for k, v in RESOURCES.items():
                    RESOURCES[k] = 100
                    print("%s: %s%%" % (k, v))
            elif command == HELP:
                for c in commands:
                    print(c)
            elif command == EXIT:
                break
