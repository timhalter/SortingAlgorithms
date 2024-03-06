import random
import time

def bubble_sort(unsorted_list):
    
    for count in range(len(unsorted_list)):
        for i in range(len(unsorted_list) - 1 - count):
            if unsorted_list[i] > unsorted_list[i+1]:
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
    return unsorted_list

if __name__ == "__main__":
    unsorted_list = []
    for i in range(9999):
        unsorted_list.append(random.randint(0, 999))
    
    start = time.time()
    unsorted_list = bubble_sort(unsorted_list)
    end = time.time()
    for i in range(len(unsorted_list)-1):
        assert unsorted_list[i] <= unsorted_list[i + 1]

    print(end-start)