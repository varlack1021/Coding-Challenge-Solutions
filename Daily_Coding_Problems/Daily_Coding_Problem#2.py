'''

Daily Coding Problem: Problem #2

Given an array of integers, return a new array
such that each element at index i of the new array
is the product of all the numbers of the original array
except the one at i.

For example, if our input was [1,2,3,4,5], the expected output
would be [120, 60, 40, 30, 24]. If our input was [3, 2 ,1], the expected
output would be [2, 3, 6]

'''

#Non division solution

list1 = [1, 2, 3, 4, 5]
list2 = [ ]


print(list1)

#Multiplies all numbers in a list
def multiply(list):
    result = 1

    for x in list:
        result = result * x

    return result

#Removes an element at each index and multiplies the rest of the list
for x in range(len(list1)):
    temp = list1[x]
    del list1[x]

#adds the result to the second list
    list2.append(multiply(list1))

#Re inserts the value that was removed from the list
    list1.insert(x, temp)

print(list2)
