def arrayIntersection(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    intersectedArray = []
    while(i < n1 and j < n2):
        if(arr1[i] == arr2[j]):
            intersectedArray.append(arr1[i])
            i += 1
            j += 1
        elif(arr1[i] > arr2[j]):
            j += 1
        else:
            i += 1
    return intersectedArray

arr1 = [1,2,2,2,3,4]
arr2 = [2,2,3,3]
print("INTERSECTION OF ARRAY => ", arrayIntersection(arr1, arr2))