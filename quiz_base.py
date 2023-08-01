# load functions from other files
from quiz_instructions import *
from quiz_list_questions_v2 import *
from quiz_list_answers_v2 import *
from check_inputs import *

# set variables for game controls
max_rounds = 10
spacer_1 = "\n\n================================================================"
spacer_2 = "================================================================\n"
spacer_3 = "\n\n###################################################################"
spacer_4 = "###################################################################\n"

# show welcome message to gamer
print('\nWelcome to my game. Would you like to read the instructions first? ( or enter xxx to quit at any stage )\r\n')
var_played_before = input("Please enter yes or no: ")

# run validation on user's answer
my_return = "forceLoop"

while my_return != 'y' and my_return != 'n':
    my_return = checkyesno(var_played_before)
    # if valid answer is y then show instructions
    if my_return == 'y':
        gameinstruction()
        pass
    # if valid answer is n then continue without showing instructions
    elif my_return == 'n':
        pass
    # if the answer is invalid then prompt the gamer to enter a valid input
    elif my_return == 'error':
        var_played_before = input("That was not a valid input. Please enter yes or no... ")

        # ask gamer how many rounds they would like to attempt
var_total_questions = input("\n\rOkay... How many questions would you like to attempt? ( max 10 ) ")

total_questions = "forceLoop"

while total_questions != "pass":
    # run validation on user's answer
    total_questions = checknumber(var_total_questions)
    # if the gamers response is valid
    if total_questions == 'pass':
        pass
    else:
        var_total_questions = input("\n\rPlease enter a whole number between 1 and 10... ")
        # run validation on user's answer
        # total_questions = checknumber(var_total_questions)

print("\n\rExcellent,", int(var_total_questions), "questions coming right up!")
print(spacer_2)

# set base game variables
round_number = 1
answered_correctly = 0
# this function uses the input 0 or 1 to return either the question for the round...
# or it returns the correct answer for the round
correct_answer = questions(round_number, 1)

# loop through questions as long as the current round number...
# is less than or equal to both the number of rounds the gamer chose...
# and the maximum number of questions I made available
while int(round_number) <= int(max_rounds) and int(round_number) <= int(var_total_questions):

    questions(round_number, 0)
    answers(round_number)
    user_answer = input("\nEnter your answer here: ")
    # this function converts numbers 1-4 to match with a-d; and looks for the quit input xxx
    clean_answer = cleananswer(user_answer)
    round_number = int(round_number) + 1
    correct_answer = questions(round_number - 1, 1)
    # print(clean_answer,correct_answer,round_number) -> test that the correct answer is being returned

    # if the user's answer is valid and correct... show message and then continue to next question
    if correct_answer == clean_answer:
        answered_correctly = int(answered_correctly) + 1
        # round_number = int(round_number) + 1
        print(spacer_1)
        print("Yay you chose the correct answer!")
        print(spacer_2)
        continue

    # if the user's answer is not valid correct... show message and then continue to next question
    else:
        print(spacer_1)
        print("Sorry...The correct answer is ", correct_answer)
        print(spacer_2)
        continue

# End Game Stats
print(spacer_3)
print("                          GAME SUMMARY")
print(spacer_4)
print(spacer_3)

# if the gamer does not answer any questions correctly. Show this message
if answered_correctly == 0:
    print(spacer_1)
    print("You failed to answer any questions correctly\n\nBetter luck next time!", "\N{unamused face}")
    print(spacer_2)

    # if the gamer answers some questions correctly. Show this message
elif int(answered_correctly) == int(var_total_questions):
    print("You answered all the questions correctly!")
    print("You are a champion", "\U0001F600")
    print(spacer_4)

    # if the gamer answers all the questions correctly. Show this message
else:
    success_rate = round(int(answered_correctly) / int(var_total_questions) * 100, 1)
    print("You answered ", answered_correctly, " question/s correctly out of ", var_total_questions)
    print("That's a success rate of ", success_rate, "%")
    print("Play again any time!")
    print(spacer_4)
