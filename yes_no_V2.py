import random


def yes_no(question):
    while True:
        # Ask the user if they have played before
        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response == "yes" or response == "y":
            print("program continues")
            continue

        elif response == "no" or response == "n":
            show_instructions = "no"
            print("display instructions")
            continue

        # If they say no, output 'display instructions'
        else:
            print("Please answer yes or no")
            continue



yes_no("Have you played this game before? ")


