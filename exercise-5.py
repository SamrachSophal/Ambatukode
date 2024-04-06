def reverse_ascending(numbers):
    numbers.sort(reverse=True)
    return numbers

numbers = [5, 7, 10, 4, 2, 7, 8, 1, 3]
result = reverse_ascending(numbers)
print(result)