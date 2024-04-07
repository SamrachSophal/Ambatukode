def replace_last(numbers):
    
    if len(numbers) <= 1:
        return numbers
    else:
        last_element = numbers.pop()
        numbers.insert(0, last_element)
        numbers = [2, 3, 4, 1]
    
        return numbers
    
print(replace_last([2, 3, 4, 1]))


        
    
