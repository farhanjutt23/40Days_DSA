def find_minimum(arr):

    # Assume the first element is the minimum
    min_val = arr[0]
    
    # Traverse the list to find the minimum element
    for num in arr:
        if num < min_val:
            min_val = num
    
    return min_val

# Main code
nums = [23, 45, 1, 2, 8, 19, -3, 16, -11]
min_number = find_minimum(nums)
print(f"The minimum number in the list is {min_number}")

