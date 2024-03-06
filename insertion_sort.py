import random
import time


def insertion_sort(unsorted_list):
    sorted_list = []

    for i in range(len(unsorted_list)):        
        if i == 0:
            sorted_list.append(unsorted_list[i])
        else:
            insert_idx = 0
            for sorted_i in range(len(sorted_list)):                
                if unsorted_list[i] >= sorted_list[sorted_i]:
                    insert_idx = sorted_i + 1
            sorted_list.insert(insert_idx, unsorted_list[i])
    return sorted_list



if __name__ == "__main__":
    unsorted_list = []
    for i in range(999):
        unsorted_list.append(random.randint(0, 999))
    
    start = time.time()
    unsorted_list = insertion_sort(unsorted_list)
    end = time.time()
    for i in range(len(unsorted_list)-1):
        assert unsorted_list[i] <= unsorted_list[i + 1]

    print(end-start)
