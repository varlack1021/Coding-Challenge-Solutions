#first attempt
student_marks = {}
n = int(input())
for _ in range(n):
    name, *line = input().split()
    scores = list(map(int, line))
    student_marks[name] = scores
query_name = input()

average = student_marks[query_name]
print(average)
sum = 0
count = 0
for x in average:
    sum += x
    count +=1
print(sum/count)

#optimized

student_marks = {}
n = int(input())
for _ in range(n):
        name, *line = input().split()
        scores = list(map(int,line))
        student_marks[name] = scores

query_name = input()
average = student_marks[query_name]
print(sum(average) / len(average))
