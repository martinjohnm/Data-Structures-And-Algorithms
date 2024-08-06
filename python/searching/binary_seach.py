



def binary_search(arr, element) :

    # Initialize start and end pointers
    start, end = 0, len(arr) -1

    while start <= end:

        # Modifiy middle index as the current middle of start and end in this iteration
        middle = start + (end-start)//2

        # If current middle value is same as the element we found the result return it immediately
        if arr[middle] == element:

            return middle
        
        # If current middle value less than search element shift the search to right portion of the array by assiging start pointer as below
        elif arr[middle] < element:

            start = middle + 1

        # If current middle value greater than search element shift the search to left portion of the array by assiging end pointer as below
        else:

            end = middle - 1

    # If the function not returned yet the value is not present in the array
    return -1


if __name__ == "__main__" :

    # Binary search only work with sorted array
    result = binary_search([1,2,3,4,5,6,7,8,9,12,13,22,33,], 60)

    if (result != -1):
        print("value present at index :", result)
    else :
        print("value not present")