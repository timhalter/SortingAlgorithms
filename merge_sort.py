import random
import time

def merge_sort(unsorted_list):
    if len(unsorted_list) > 1:
        mid = len(unsorted_list) // 2

        L = unsorted_list[:mid]
        R = unsorted_list[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while (i < len(L) and j < len(R)):
            if L[i] <= R[j]:
                unsorted_list[k] = L[i]
                i+=1
            else:
                unsorted_list[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            unsorted_list[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            unsorted_list[k] = R[j]
            j += 1
            k += 1

if __name__ == "__main__":
    unsorted_list = []
    for i in range(30):
        unsorted_list.append(random.randint(0, 5))
    #print(unsorted_list)
    start = time.time()
    merge_sort(unsorted_list)
    end = time.time()

    for i in range(len(unsorted_list)-1):
        assert unsorted_list[i] <= unsorted_list[i + 1]

    print(end-start)
    #print(unsorted_list)