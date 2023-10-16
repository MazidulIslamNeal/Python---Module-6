def remove_odd_numbers(input_list):
    return [x for x in input_list if x % 2 == 0]

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cut_down_list = remove_odd_numbers(original_list)

print(f"Original list: {original_list}")
print(f"Cut-down list (odd numbers removed): {cut_down_list}")
