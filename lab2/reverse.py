
import re

main_list = input()

# search for numbers
temp = re.findall(r'[-+]?\d+', main_list)
    # creat a list of these numbers
num_list = list(map(int, temp))

num_list.reverse()
#print(rev)
print(num_list)
