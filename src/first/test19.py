"""
列表操作案例
"""

age_list = [21, 25, 21, 23, 22, 20]

age_list.append(31)
print(age_list)

age_list.extend([29, 33, 30])
print(age_list)

# one = age_list[0]
one = age_list.pop(0)
print(one)

# last = age_list[-1]
last = age_list.pop(-1)
print(last)

num_index = age_list.index(31)
print(num_index)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for x in my_list:
    if x % 2 == 0:
        new_list.append(x)
print(new_list)

new_list2 = []
index = 0
while index < len(my_list):
    if my_list[index] % 2 == 0:
        new_list2.append(my_list[index])
    index += 1
print(new_list2)

new_list3 = [x for x in my_list if x % 2 == 0]
print(new_list2)
