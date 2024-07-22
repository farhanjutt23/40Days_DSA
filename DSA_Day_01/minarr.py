'''find the minimum nummber '''
def linear_search(arr):
    val=arr[0]
    for num in arr:
        if num<val:
            val=num
    return val

# Main code
nums = [23, 45,1,4,2]
print("The minimum number is the in list is",linear_search(nums))