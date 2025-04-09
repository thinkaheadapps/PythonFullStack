list_of_amounts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
list_of_amounts_gr = []
list_of_amounts_ls = []

for amount in list_of_amounts:
    if amount > 500:
        list_of_amounts_gr.append(amount)
print(list_of_amounts_gr)

list_of_amounts_ls = [amount for amount in list_of_amounts if amount < 500]
print(list_of_amounts_ls)

first_10_integer_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sq_of_first_10_integer_number = [i**2 for i in first_10_integer_number]
print(sq_of_first_10_integer_number)
