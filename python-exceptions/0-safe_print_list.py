#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            # Try to print the element at index i
            print(my_list[i], end="")
            count += 1  # Increment count for each element printed
    except IndexError:
        # If IndexError occurs, we stop the loop because we ran out of elements
        pass
    print()  # Move to the next line after printing
    return count
