import math
total = 0
list_of_nums = []

amt_of_nums = int(input("Enter the amounts of values you would like to input into your list: "))

for num in range(amt_of_nums):
    num = int(input("Enter your value: "))
    list_of_nums.append(num)

print(f"Are your values correct?\n{list_of_nums}")
#need help - want to make it go back to correct log

selection = input("Enter desired calculation:\nMean\nMedian\nMode\nRange\nMaximum and Minimum\nSum\nMidrange\nVariance\nStandard Deviation\nMean Absolute Deviation\nThird Quartile, First Quartile, and Interquartile Ranges\nZ-Scores\n").strip().lower()

if selection != "mean" or "median" or "mode" or "range" or "maximum and minimum" or "sum" or "midrange" or "variance" or "standard deviation" or "mean absolute deviation" or "third quartile, first quartile, and interquartile ranges" or "z-scores":
    print("Please enter a valid calculation.")
#need help - always prints

if selection == "mean":
    for num in list_of_nums:
        total += num
        mean = total / len(list_of_nums)
    print(mean)

if selection == "median":
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
    print(found_median)

