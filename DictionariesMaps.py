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
