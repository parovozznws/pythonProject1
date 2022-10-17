my_array = [465, 12, 1024, 554, 7]

my_dict = {}
i = 0

while i < len(my_array):
    amount = 0
    current_i = my_array[i]
    while (current_i != 0):
        amount += current_i % 10
        current_i = current_i // 10
    my_dict[my_array[i]] = amount
    i += 1

sorted_dict = {}
sorted_keys = sorted(my_dict, key=my_dict.get)
for n in sorted_keys:
    sorted_dict[n] = my_dict[n]

print(list(sorted_dict.keys()))