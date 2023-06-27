import random


def yes_no(question):
    while True:
        # Ask the user if they have played before
        show_instructions = input(question).lower()

        # If they say yes, output 'program continues'
        if show_instructions == "yes" or show_instructions == "y":
            print("program continues")
            continue

        elif show_instructions == "no" or show_instructions == "n":
            show_instructions = "no"
            print("display instructions")
            continue

        # If they say no, output 'display instructions'
        else:
            print("Please answer yes or no")
            continue


yes_no("Have you played this game before? ")
