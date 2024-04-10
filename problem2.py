def array_division(arr):
    result = []
    n = len(arr)
    
    for i in range(n):
        try:
            # Divide the current element by the next element in the array
            if i == n - 1:
                division_result = arr[i] / arr[0]  # For the last element, divide by the first element
            else:
                division_result = arr[i] / arr[i + 1]
            
            result.append(division_result)
        except ZeroDivisionError:
            # Handle division by zero
            print(f"Warning: Division by zero encountered at index {i}. Skipping operation.")
            result.append(None)  # Setting None as the result for the division
            
    return result

arr = [9,33,0,7,2,82,77];
result = array_division(arr)
print("Results:", result)
