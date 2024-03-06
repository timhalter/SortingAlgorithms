import random
import time

def quick_sort(unsorted_list, low, high):
    pivot = ...



if __name__ == "__main__":
    unsorted_list = []

    for i in range(30):
        unsorted_list.append(random.randint(0, 5))

    print(unsorted_list)

    start = time.time()
    quick_sort(unsorted_list)
    end = time.time()

    for i in range(len(unsorted_list)-1):
        assert unsorted_list[i] <= unsorted_list[i + 1]

    print(end-start)
    print(unsorted_list)    