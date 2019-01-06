#first attempt


#optimized

student_marks = {}
n = int(input())
for _ in range(n):
        name, *line = input().split()
        scores = list(map(int,line))
        student_marks[name] = scores

query_name = input()

average = 0
for x in list(map(int, student_marks[query_name])):
     average += x
print(average / len(list(map(int, student_marks[query_name]))))
