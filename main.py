numbers_list = []
numbers_div_5_list = []
numbers_div_5_square_3_list = []
for i in range(0,101):
    numbers_list.append(i)
for number in numbers_list:
    if number%5 == 0:
        numbers_div_5_list.append(number)
for number in numbers_div_5_list:
    numbers_div_5_square_3_list.append(number**3)
print(numbers_div_5_list)
print(numbers_div_5_square_3_list)
