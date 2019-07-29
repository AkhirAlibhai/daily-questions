def check_valid_parentheses(string):
    curr_parentheses = 0

    for character in string:
        if character == '(':
            curr_parentheses += 1
        elif character == ')':
            curr_parentheses -= 1

        # If we ever have a negate number for curr_parentheses
        # the string can never be valid
        if curr_parentheses < 0:
            return False

    # If curr_parentheses == 0, the string is valid
    return curr_parentheses == 0


def valid_parentheses_process(string):
    my_return = set()

    # If the string is valid
    if check_valid_parentheses(string):
        my_return.add(string)
        return my_return

    # Removing a character and checking those string
    for i in range(0, len(string)):
        my_return = my_return | valid_parentheses(string[:i] + string[i+1:])

    return my_return


def keep_highest_length(strings):
    my_return = set()
    curr_max = 0

    # Looping through each string
    for string in strings:
        # If the string is larger than the current largest
        if len(string) > curr_max:
            curr_max = len(string)
            my_return = set()
            my_return.add(string)
        # If the string is the same as the current largest
        elif len(string) == curr_max:
            my_return.add(string)

    return my_return


def valid_parentheses(string):
    my_return = valid_parentheses_process(string)

    # To remove any strings that remove more than the minimal characters
    return keep_highest_length(my_return)