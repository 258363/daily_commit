num_list = [2, 4, 6, 9]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)