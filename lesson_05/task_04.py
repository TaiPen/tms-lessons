def my_round (numb: float, digits: int = 0):
    # numb = input('Введите число:')
    ten_pow = 10 ** digits
    numb = numb * ten_pow
    if numb - int(numb) > 0.5:
        numb = int(numb)
    else:
        numb = int(numb) + 1
    numb = numb / ten_pow
    return numb


print(my_round(10.4))
print(my_round(12.55, 1))
print(my_round(12.759, 2))
print(my_round(12.759, 20))