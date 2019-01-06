#Given a nested list
#Print all the names that have the second lowest score
#My solution works but does not satisfy HackerRanks check system
#Sample Data
lis = [["Timmy", -50], ["John", -50]]

lis.append(["Mark", -50])
lis.append(["Bob", 51])

lis.sort(key = lambda lis: lis[1])
for x in lis:
    if x[1] == lis[1][1]:
        print(x[0])

#This code works for the HackerRank check system
#Got it from the discussion board and is elegant

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
