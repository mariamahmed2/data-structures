import re
Even_Sum = 0
Odd_Sum = 0

main_list = input()
if main_list == '[]':
    print([0, 0])
else:
    # search for numbers
    temp = re.findall(r'[-+]?\d+', main_list)
    # creat a list of these numbers
    num_list = list(map(int, temp))


    for j in range(len(num_list)):
        if (num_list[j] % 2 == 0):
            Even_Sum += num_list[j]
        else:
            Odd_Sum += num_list[j]


    print([Even_Sum, Odd_Sum])
