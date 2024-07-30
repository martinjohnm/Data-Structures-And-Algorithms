

import random


def randomArray(lim) :

    arr = []

    for i in range(lim):
        arr.append(random.randint(1,lim))

    return arr


