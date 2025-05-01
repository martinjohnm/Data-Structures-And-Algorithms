



def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        innerLoopLen = size - 1 - i
        for j in range(innerLoopLen):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp

if __name__ == "__main__":
    elements = [5,6,4,2342,5,34,5,0,4,5,8,10]

    # elements = [1,2,3,4,5]
    bubble_sort(elements)
    print(elements)