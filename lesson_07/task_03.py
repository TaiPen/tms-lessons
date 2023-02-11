my_list = [63, 25, 9]
s = 0
for num in my_list:
    s = s + num
print(s)

from functools import reduce
print(reduce(lambda  a, b: a + b, my_list))