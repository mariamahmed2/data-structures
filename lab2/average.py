# fun to calc. the average
def average(arr, length):
    # Find sum of array element
    sum = 0
    for i in range(length):
        sum += arr[i]

    return sum / length;

import re

main_list = input()
if main_list == '[]':
    print(0.0)
else:
    # search for numbers
    temp = re.findall(r'[-+]?\d+', main_list)
    # creat a list of these numbers
    num_list = list(map(int, temp))

    # get avg
    avg = average(num_list, len(num_list))

    print(avg)
