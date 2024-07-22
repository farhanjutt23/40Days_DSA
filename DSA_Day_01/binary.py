def linear_search(arr, target):
    # Check if the array is empty
    if len(arr) == 0:
        return -1
    
    # Run a for loop
    for index in range(len(arr)):
        # Check for the element at every index if it is equal to target
        if arr[index] == target:
            return index
    
    # Return -1 if the element is not found
    return -1

# Main code
nums = [23, 45, 1, 2, 8, 19, -3, 16, -11]
target = 19
ans = linear_search(nums, target)
print(ans)
