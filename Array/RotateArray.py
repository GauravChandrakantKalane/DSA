# def rotateArray(arr,m):
#     n = len(arr)
#     rotate = [0] * n
#     for i in range(0,n):
#         pos = (i + m) % n
#         rotate[pos] = arr[i]
#     return rotate

# arr = [1,2,3,4,5,6,7]
# m = 3
# print("ROTATED ARRAY => ", rotateArray(arr,m))

def reverseArray(arr,start,end):
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    return arr

def rotateArray(arr,m):
    n = len(arr)
    arr = reverseArray(arr,0,n-1)
    arr = reverseArray(arr,0,(m%n)-1)
    arr = reverseArray(arr,(m%n), n-1)
    return arr

arr = [1,2,3,4,5,6,7]
m = 4
print("ROTATED ARRAY => ", rotateArray(arr,m))