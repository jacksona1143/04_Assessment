show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this quiz before? ")

    # If they say yes, output 'program continues'
    if show_instructions == "yes":
        print("program continues")

    elif show_instructions == "y":
        print("program continues")

    elif show_instructions == "no":
        print("display instructions")

    elif show_instructions == "n":
        print("display instructions")

    # If they say no, output 'display instructions'
    else:
        print("Please answer yes / no")