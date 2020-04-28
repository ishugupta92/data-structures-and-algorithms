"""
Assignment for Class 2 of Python Training
"""


# returns an array with the num added at the middle index.
def insert_shift_array(arr, num):
    arr_len = len(arr)
    prev = num
    for i in range(arr_len):
        if i >= (arr_len)/2:
            temp = arr[i]
            arr[i] = prev
            prev = temp
    arr.append(prev)
    return arr
