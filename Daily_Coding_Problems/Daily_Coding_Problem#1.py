'''
Given a list of number k, return whether any two numbers from the list add up to k.
'''

import random

randList = []
k = 10
for _ in range(20):
    randList.append(random.randint(-11,10))

print(randList)
for x in range( len(randList) - 1):

        for y in range( x + 1, len(randList) ):

            if randList[x] + randList[y] == k:
                print(str(randList[x]) + " " + str(randList[y])   + " is equal to " + str(k))
