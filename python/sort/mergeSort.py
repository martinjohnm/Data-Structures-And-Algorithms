


def merge_sort(arr) :
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)

def merge_two_sorted_lists(leftArr,rightArr) : 

    sorted_list = []
    leftIdx = rightIdx = 0

    while leftIdx < len(leftArr) and rightIdx < len(rightArr) : 

        if leftArr[leftIdx] <= rightArr[rightIdx] : 
            sorted_list.append(leftArr[leftIdx])
            leftIdx += 1
        else :
            sorted_list.append(rightArr[rightIdx])
            rightIdx += 1

    while leftIdx < len(leftArr) : 
        sorted_list.append(leftArr[leftIdx])
        leftIdx += 1
    
    while rightIdx < len(rightArr) : 
        sorted_list.append(rightArr[rightIdx])
        rightIdx += 1
    
    return sorted_list


if __name__ == "__main__" :

    print(merge_sort([10,3,4,5,22,3,121,5]))