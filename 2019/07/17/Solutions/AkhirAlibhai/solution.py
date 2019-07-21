def level_order(array):
    curr_power = 1
    curr_count = curr_power
    curr_array = []
    my_return = []
    for element in array:
        if curr_count == 0:
            my_return.append(curr_array)
            curr_array = []
            curr_power *= 2
            curr_count = curr_power
        curr_array.append(element)
        curr_count -= 1

    my_return.append(curr_array)
    return my_return
