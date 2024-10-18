# Example array
arr = [3, 5, 1, 9, 2]

# Initialize max_value to the first element of the array
max_value = arr[0]

# Loop through the array to find the maximum value
for num in arr:
    if num > max_value:
        max_value = num

# Display the result
print("The maximum value in the array is:", max_value)
