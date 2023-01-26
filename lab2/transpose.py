import re
import math

# function to split the list into list of small lists
def split(List, length):
    for i in range(0, len(List), length):
        yield List[i:i + length]

     # input the main list
main_list = input()
#print(test_string)
# handel test cases
if main_list == '[]':
    print('[]')
elif main_list == '[[]]':
    print('[[]]')
else:
    # search for numbers
    temp = re.findall(r'[-+]?\d+', main_list)
    # creat a list of these numbers
    num_list = list(map(int, temp))
#\d+
    # print(res)
    # print(type(res))
    # get the number of cols. and rows.
    length = int(math.sqrt(len(num_list)))

    # print(length)
    # creat a list of lists to be transposed
    list_to_trans = list(split(num_list, length))

    # transpose the matrix
    tran = [[row[i] for row in list_to_trans] for i in range(len(list_to_trans[0]))]
    print(tran)
