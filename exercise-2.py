def index_power(numbers, n):
    if n < 0 or n >= len(numbers):
        return -1
    else:
        return numbers[n] ** n
    
print(index_power([1, 2, 3, 4], 2))  
print(index_power([1, 2, 3], 3))     

    
    
