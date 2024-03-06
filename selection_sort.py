import random


def selection_sort(unsorted_list):

    for i in range(len(unsorted_list)):
        smallest_index = i

        for index in range(smallest_index + 1, len(unsorted_list)):
            if unsorted_list[index] < unsorted_list[smallest_index]:
                smallest_index = index
        
        unsorted_list[i], unsorted_list[smallest_index] = unsorted_list[smallest_index], unsorted_list[i]
    return unsorted_list

if __name__ == "__main__":
    unsorted_list = []
    for i in range(9):
        unsorted_list.append(random.randint(0, 5))
    print(unsorted_list)
    unsorted_list = selection_sort(unsorted_list)
    print(unsorted_list)