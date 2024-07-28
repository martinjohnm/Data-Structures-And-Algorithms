


def merge_sort(arr) :
    
    if len(arr) <= 1:
        return 
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    return merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(leftArr,rightArr, arr) : 

    leftIdx = rightIdx = arrIdx = 0

    while leftIdx < len(leftArr) and rightIdx < len(rightArr) : 

        if leftArr[leftIdx] <= rightArr[rightIdx] : 

            arr[arrIdx] = leftArr[leftIdx]
            leftIdx += 1

        else :

            arr[arrIdx] = rightArr[rightIdx]
            rightIdx += 1

        arrIdx += 1

    while leftIdx < len(leftArr) : 

        arr[arrIdx] = leftArr[leftIdx]
        leftIdx += 1
        arrIdx += 1
    
    while rightIdx < len(rightArr) : 

        arr[arrIdx] = rightArr[rightIdx]
        rightIdx += 1
        arrIdx += 1
    


if __name__ == "__main__" :

    arr = [10,3,4,5,22,3,121,5]
    merge_sort(arr)
    print(arr)