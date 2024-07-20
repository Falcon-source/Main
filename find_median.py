# Author: Wendy Y. Falcon Kuffel
# GitHub username: falcon-source
# Date: 7/ 19/2024
# Description: Return statistical median of numbers

def find_median(numbers):

    sorted_numbers = sorted(numbers)

    n = len(sorted_numbers)

    if n % 2 == 1:

        median = sorted_numbers[n // 2]
    else:

        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    return median


some_nums = [13, 7, -3, 82, 4]
result = find_median(some_nums)
print(result)
