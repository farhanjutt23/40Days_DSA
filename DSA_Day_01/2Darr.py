def linear_search_2d(array, target):
    """
    Performs a linear search on a 2D array.
    
    param array: List of lists (2D array) to search within
    param target: The value to search for
    return: A tuple (row, col) of the target's position if found, otherwise (-1, -1)
    """
    for row_index in range(len(array)):
        for col_index in range(len(array[row_index])):
            if array[row_index][col_index] == target:
                return (row_index, col_index)
    return (-1, -1)  # Target not found

# Example usage
if __name__ == "__main__":
    # Define a 2D array
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Define the target value
    target_value = 5
    
    # Perform linear search
    result = linear_search_2d(matrix, target_value)
    
    if result != (-1, -1):
        print(f"Target {target_value} found at position: {result}")
    else:
        print(f"Target {target_value} not found in the array.")
