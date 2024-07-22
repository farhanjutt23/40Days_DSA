pos = -1

def search(lst, n):
    global pos
    i = 0
    while i < len(lst):
        if lst[i] == n:
            pos = i
            return True
        i += 1
    return False

lst = [5, 6, 4, 3, 8, 7, 9]
n = 6

if search(lst, n):
    print("Found at", pos + 1)
else:
    print("Not found")