def merge_overlapping(array):
    my_return = []
    for interval in array:
        not_in_intervals = True

        for found_interval in my_return:
            if interval[0] >= found_interval[0]:
                # Intervals overlap, [x1, y1] [x2, y2]
                # x1 >= x2 and x1 <= y1

                # x2  x1  y2  y1
                if interval[0] <= found_interval[1]:
                    # Checking which value is the greater
                    if interval[1] > found_interval[1]:
                        found_interval[1] = interval[1]
                    not_in_intervals = False
                    break
            # Checking the opposite conditions of the above
            else:
                # Intervals overlap, [x1, y1] [x2, y2]
                # x1 <= x2 and x2 <= y1

                # x1  x2  y2  y1
                if interval[1] >= found_interval[0]:
                    # Checking which value is the lesser
                    if interval[0] < found_interval[0]:
                        found_interval[0] = interval[0]
                    not_in_intervals = False
                    break

        if not_in_intervals:
            my_return.append(interval)
    return my_return
