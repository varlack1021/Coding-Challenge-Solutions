'''
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for. 
For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
if an entry for name is not found, print Not found instead.
Note: Your phone book should be a Dictionary/Map/HashMap data structure.
'''
#My version
n = int(input())
student_marks = {}
for _ in range(n):
    name, score = input().split()
    student_marks[name] = score
query = []
for _ in range(n):
    query.append(input())

try:
    for name in query:
        if name in student_marks:
            print(name + "=" + student_marks[name])

        else:
            print("Not found")
except:
        break

#Optimzed and accepted by HackerRank

n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break
