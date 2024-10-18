def find_maximum(arr, return_index=False):
    """
    Finds the maximum element in an array.
    
    Parameters:
    arr (list): The input array of numbers.
    return_index (bool): If True, return the index of the maximum element; otherwise, return its value.

    Returns:
    int/float or int: The maximum value or its index in the array.
    
    Raises:
    ValueError: If the input array is empty or contains non-numeric values.
    """
    
    if not arr:
        raise ValueError("Input array cannot be empty.")
    
    maximum = arr[0]
    max_index = 0
    
    for index, value in enumerate(arr):
        if not isinstance(value, (int, float)):
            raise ValueError("All elements in the array must be numeric.")
        
        if value > maximum:
            maximum = value
            max_index = index

    return max_index if return_index else maximum

# Example usage
arr = [1, 3, 5, 2, 8, 7]
max_value = find_maximum(arr)
max_index = find_maximum(arr, return_index=True)

print(f"Maximum value: {max_value}")  # Output: 8
print(f"Index of maximum value: {max_index}")  # Output: 4
