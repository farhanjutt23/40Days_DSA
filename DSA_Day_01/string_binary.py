def search(string, target):
    # Check if the string is empty
    if len(string) == 0:
        return False
    
    # Run a for loop
    for char in string:
        # Check for the character in the string if it is equal to target
        if target == char:
            return True
    
    # Return False if the character is not found
    return False

# Main code
name = "Kunal"
target = ''
print(search(name, target))
