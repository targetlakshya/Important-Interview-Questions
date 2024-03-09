# We have a array of n elements and we have to find Position of first infinite element in the array

# Method 1: Using Linear Search
arr = [20,-30,10,5,7,0,29,float('inf')]

for i in range(len(arr)):
    if arr[i] == float('inf'):
        print("Position of first infinite element is ",i)
        break


# Method 2: Using Binary Search
    
def binarySearch(arr, x, i, j):
    while i <= j:
        mid = i + (j - i) // 2
        if arr[mid] == float('inf'):
            if mid == 0 or arr[mid - 1] != float('inf'):
                return mid
            else:
                j = mid - 1
        elif arr[mid] < x:
            i = mid + 1
        else:
            j = mid - 1
    return -1

arr = [20, -30, 10, 5, 7, 0, 29, 55, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
x = float('inf')    
result = binarySearch(arr, x, 0, len(arr) - 1)
print("Position of first infinite element is", result)

