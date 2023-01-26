# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

main_list = input()

try:
    num = int(input())
    # search for numbers
    temp = re.findall(r'[-+]?\d+', main_list)
    # creat a list of these numbers
    num_list = list(map(int, temp))

    for i in range(len(num_list)):
        if (num_list[i] == num):
            num_list.remove(num_list[i])
            num_list.append(num)
    print(num_list)
except main_list == '[]':
    
    print("Error")
