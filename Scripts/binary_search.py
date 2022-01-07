primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
primes2 = [67]



def find_middle_index(index_start, index_end):
    middle_index = (index_start+index_end)/2
    return int(middle_index)


def binary_search_fun(data_set: list, x: int):
    index_start = 0
    index_end = len(data_set) - 1
    while True:

        if index_start == index_end:
            if data_set[index_start] == x:
                return index_start #zwraca indeks szukanego elementu
            else:
                return -1 #zwraca -1 (indeks nie może być <0)
        
        middle_index = find_middle_index(index_start, index_end)

        if data_set[middle_index] == x:
            return middle_index #zwraca indeks szukanego elementu

        elif x < data_set[middle_index]:
            #index_start = index_start
            index_end = middle_index - 1

        elif x > data_set[middle_index]:
            #index_end = index_end
            index_start = middle_index + 1


print (binary_search_fun(primes,67))
print (binary_search_fun(primes2,67))
print (binary_search_fun(primes,101))


