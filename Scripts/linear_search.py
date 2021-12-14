primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#print (len(primes))
#middle_index = (len(primes) - 1)/2
#print (middle_index)

#for item in primes:
#    print(item)


#   list contains primes from the range 0-100
#   1) is 67 a prime?
#       67 is lower than 100
#       if 67 is the element of the list, it is a prime
#   2) how many primes are smaller than 67?


# Linear search

def LinearSearch (input_list: list, element: int):
    list_len = len(input_list)
    for i in range(list_len):
        if input_list[i] == element:
            return i
    return -1

print ("Given list of primes from the range 0-100 is:", primes)

x = 6

position = LinearSearch(primes, x)

print("The variable type is", type(position))

position_int = int(position)

if position_int >=0 and position_int < len(primes):
    print ("Element %d is at the position:" %(x), position, ", so it is lower than 100 and it is a prime")
elif position_int == -1:
     print ("%d is not a prime lower than 100" %(x)) 
else:
    print ("Error")

