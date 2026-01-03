# imports

# global variable
PALINDROME_TURE_MSG = "The string is a palindrome."
PALINDROME_FALSE_MSG = "The string is not a palindrome."

# get User input
def get_user_input():
    msg = input("Enter your STRING that you want to check :\n")
    return msg

# check palindrome
def palindrome_check(msg):
    length = len(msg)
    for i in range(length // 2):
        if msg[i] != msg[length - 1 - i]:
            return False
    return True


# set the resualt
def generate_palindorme_msg_result(palindorme_result):
    if palindorme_result == True:
        print(PALINDROME_TURE_MSG)
    else:
        print(PALINDROME_FALSE_MSG)

# run application
user_input_msg = get_user_input()
generate_palindorme_msg_result(palindrome_check(user_input_msg))
