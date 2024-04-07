def reverse_ascending(numbers):
    result = []
    start = 0
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            result.extend(reversed(numbers[start:i]))
            start = i
    result.extend(reversed(numbers[start:]))
    return result

numbers = [5, 7, 2, 1, 10, 4, 2, 7, 8, 3, 1]
print(reverse_ascending(numbers))