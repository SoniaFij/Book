primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
primes2 = [67]



def find_middle_index(index_start, index_end):
    middle_index = index_end-index_start/2
    return int(middle_index)


def binary_search(data_set: list, x: int):
    index_start = 0
    index_end = len(data_set) - 1
    while True:

        if index_start == index_end:
            if data_set[index_start] == x:
                return "%d is the element of the list. Its index is %d." %(x,index_start)
            else:
                return "%d is not an element of the list." %(x)
        
        middle_index = find_middle_index(index_start, index_end)

        if data_set[middle_index] == x:
            return "%d is the element of the list. Its index is %d." %(x,middle_index)

        elif x < data_set[middle_index]:
            #index_start = index_start
            index_end = middle_index - 1

        elif x > data_set[middle_index]:
            #index_end = index_end
            index_start = middle_index + 1


print (binary_search(primes,67))
print (binary_search(primes2,67))
print (binary_search(primes,101))