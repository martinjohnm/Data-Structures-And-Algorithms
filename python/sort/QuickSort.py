
def swap (a,b,arr) : 
    arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end): 
    
    # pivot index is always start(hoare partition scheme)
    pivot_index = start
    pivot_element = elements[pivot_index]

    while start < end:
        # ride this loop until found an element which is greater than or equal to the pivot element
        while start < len(elements) and elements[start] <= pivot_element:
            start +=1
        # ride this loop until found an element which is lesser than than the pivot element
        while elements[end] > pivot_element:
            end -= 1
        
        # if the two pointers not crossed after the above two while loop that means 
        # the given elements are at wrong position. Then swap both values(not pointers)
        if start < end:
            swap(start, end, elements)
        # continue the outer while loop until the start cross end

    # after the first while loop the end will just cross the start that is the correct postion for the pivot element
    # , swap end pointer array value with the pivot element 
    swap(pivot_index, end, elements)

    # return the end pointer which can be used to call the quick sort recursively
    return end

def quick_sort(elements, start, end):
    
    if start < end:
        pi = partition(elements, start, end)
        # left recurtion call (this recursion keeps on calling until the start === end 
        # which means single element array which is already sorted)
        quick_sort(elements, start, pi - 1)
        # right recursion call (this function call paused in the call stack
        #  until the left recursion call (above call succeeds) after that is resumes)
        quick_sort(elements, pi + 1, end)



if __name__ == "__main__" :

    arr = [20,11,9,29,7,2,15,28,5,5,5,5343,23,234,4,4,4,4,4,4,4,4,4,4,4]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)