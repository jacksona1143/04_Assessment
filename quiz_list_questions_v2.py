
def questions(questionNumber,returnType):

    if questionNumber == 1:
     questionToAsk = "What is the purpose of a return statement in a function?"
     expectedAnswer = "c"

    elif questionNumber == 2:
     questionToAsk = "Which keyword is used to define a function in Python?"
     expectedAnswer = "c"

    elif questionNumber == 3:
     questionToAsk = "What is recursion in Python?"
     expectedAnswer = "b"

    elif questionNumber == 4:
     questionToAsk = "What is the purpose of the map function in Python?"
     expectedAnswer = "a"

    elif questionNumber == 5:
     questionToAsk = "Which of the following is used to invoke a question?"
     expectedAnswer = "d"

    elif questionNumber == 6:
     questionToAsk = "What happens if you call a function without providing the required number of arguments in Python?"
     expectedAnswer = "a"

    elif questionNumber == 7:
     questionToAsk = "What is the purpose of the enumerate function in Python?"
     expectedAnswer = "b"

    elif questionNumber == 8:
     questionToAsk = "Which function can be used to find the length of a list or string in Python?"
     expectedAnswer = "d"

    elif questionNumber == 9:
     questionToAsk = "Which of the following is used to define a default value for a function parameter in Python?"
     expectedAnswer = "d"

    elif questionNumber == 10:
     questionToAsk = "Which key word is used to invoke a function in Python? "
     expectedAnswer = "a"



    if returnType == 0:
     print( "\nQuestion ",questionNumber,": ",questionToAsk,"\n" )
    else:
        return(expectedAnswer)



