my_list = [63.8, 25.89, 9.987]
rounded_list = []
for num in my_list:
    rounded_list.append(round(num))
print(rounded_list)

print([round(num) for num in my_list])

print(list(map(lambda num: round(num), my_list)))

print(my_list)