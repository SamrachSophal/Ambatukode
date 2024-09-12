def chunking_by(numbers, chunk):
    result = []
    if not numbers:
        return result
    if chunk < 1:
        return 'invalid input'
    
    num_chunks = -(-len(numbers) // chunk)
    
    for i in range(num_chunks):
        start = i * chunk
        end = (i + 1) * chunk
        result.append(numbers[start:end])
    
    return result        

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
chunk = int(input("Enter number of chunk: "))
print(chunking_by(numbers, chunk))

