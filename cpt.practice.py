import math
list_of_nums = []

def calc_mean(list_of_numbers):
    total = 0
    for num in list_of_nums:
        total += num
        mean = total / len(list_of_nums)
    return mean

def calc_median(list_of_numbers):
    sorted_list = sorted(list_of_nums)
    if len(sorted_list) % 2 == 0:
        in_list = False
    else:
        in_list = True
    if in_list == True:
        mid = len(list_of_nums) // 2
        print(sorted_list[mid])
    elif in_list == False:
        mid = len(sorted_list) // 2
        bottom = sorted_list[mid - 1]
        top = sorted_list[mid]
        found_median = (bottom + top) / 2
        return found_median

def calc_mode(list_of_numbers):
    frequency = {}
    for num in list_of_numbers:
        frequency[num] = frequency.get(num, 0) + 1
        max_nums = max(frequency.values())
        modes = [key for key, count in frequency.items() if count == max_nums]
    return modes, max_nums

while True:
    amt_of_nums = int(input("Enter the amounts of values you would like to input into your list: "))

    for num in range(amt_of_nums):
        num = int(input("Enter your value: "))
        list_of_nums.append(num)

    confirm = input(f"Are your values correct? (yes/no)\n{list_of_nums}\n").strip().lower()
    if confirm == "yes":
        break

print("Enter desired calculation:")
while True:
    selection = input("Mean\nMedian\nMode\nRange\n").strip().lower()

    valid_options = ["mean", "median", "mode", "range"]

    if selection in valid_options:
        break
    if selection not in valid_options:
        print("Please enter a valid calculation.")


if selection == "mean":
    result = calc_mean(list_of_nums)
    print(result)

if selection == "median":
    result = calc_median(list_of_nums)
    print(result)

if selection == "mode":
    result = calc_mode(list_of_nums)
    print(result)