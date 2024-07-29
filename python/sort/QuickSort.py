


def partition(elements): 
    pivot_index = 0
    pivot_element = elements[pivot_index]

    start = pivot_index + 1
    end = len(elements) - 1

    while start < end:
        while elements[start] <= pivot_element:
            start +=1

        while elements[end] > pivot_element:
            end -= 1
        
        if start < end:
            elements[start], elements[end] = elements[end], elements[start]

    elements[pivot_index], elements[end] = elements[end], elements[pivot_index]

def quick_sort(elements):
    pass



if __name__ == "__main__" :

    arr = [11,9,29,7,2,15,28]
    partition(elements=arr)
    print(arr)