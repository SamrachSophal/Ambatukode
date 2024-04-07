def remove_all_after(numbers, n):
    if n not in numbers:
        return "invalid input"
    else:
        removed_list = []
        for i in numbers:
            removed_list.append(i)
            if n == i:
                return removed_list

numbers = range(0, 101)
print("The list is from 0 - 100")
n = int(input("Enter removing number: "))
try:
    print(remove_all_after(numbers, n))
except ValueError:
     print('invalid input')