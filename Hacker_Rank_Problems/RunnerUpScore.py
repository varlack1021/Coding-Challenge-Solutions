#First attempt brute force Solution
#Finds the max and min
#Finds the second biggest by comparing each index to the min and max
lis = [50, 100, 50]
list = [57, 57, -57, 57]

min = lis[0]
max = lis[0]
for x in lis:
    if max < x:
        max = x

for x in lis:
    if min > x:
        min = x

for x in lis:
    if x > min and x < max:
        min = x
print(max)
print(min)

#Efficient Solution
#Creates a second list without duplicates
#Reverses the list
arr = list(map(int, input().split()))

listnew=[]
for i in arr:

    if i not in listnew:
        listnew.append(i)

listnew.sort(reverse=True)

print(listnew[1])
