error_message = "\nThank you for playing. Try again later...🐔🐔🐔"


def checkyesno(user_response):
    # added version 2
    if user_response.lower() == "xxx":
        print(error_message)
        exit(0)
        # added version 1
    elif user_response.lower() == "y" or user_response.lower() == "yes":
        func_result = "y"
        # added version 1
    elif user_response.lower() == "n" or user_response.lower() == "no":
        func_result = "n"
        # added version 1
    else:
        func_result = "error"

    return func_result


def checknumber(user_response):
    # added version 2
    #print(user_response.isnumeric())
    #exit(0)

    if user_response.lower() == "xxx":
        print(error_message)
        exit(0)
        # added version 1

    elif user_response.isnumeric() == False:
        funcresult = "error"
        # added version 3 -> to exclude input that is not numeric

    elif int(user_response) <= 10 and int(user_response) > 0:
        funcresult = "pass"

    else:
        funcresult = "error"

    return funcresult


def cleananswer(user_response):
    answer_list = ('a', 'b', 'c', 'd')
    answer_list_numbers = (1,2,3,4)



    if user_response.lower() == "xxx":
        print(error_message)
        exit(0)
    elif user_response.lower() not in answer_list and user_response.lower() not in answer_list_numbers:
       funcresult = "error_entry"
       return funcresult
    elif user_response.lower() in answer_list:
        funcresult = user_response.lower()
        return funcresult
    elif user_response.lower() == '1':
        funcresult = "a"
        return funcresult
    elif user_response.lower() == '2':
        funcresult = "b"
        return funcresult
    elif user_response.lower() == '3':
        funcresult = "c"
        return funcresult
    elif user_response.lower() == '4':
        funcresult = "d"
        return funcresult
    else:
        funcresult = "error"
        return funcresult
