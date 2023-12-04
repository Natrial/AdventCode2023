winning = []
mine = []
import os

absolute_path = os.path.dirname(__file__)
with open(absolute_path+"/day4.txt") as my_file:
    for line in my_file:
        data1= line[line.index(': ') +2:line.index('| ')-1].split(" ")
        data2 = line[line.index('| ')+2:-1].split(" ")
        if '' in data1:
            data1 = list(filter(len, data1))

        if '' in data2:
            data2 = list(filter(len, data2))
        winning.append(list(map(int, data1)))
        mine.append(list(map(int, data2)))

sol1 = 0
sol2 = [1]*(len(winning))

for i in range(len(winning)):
    exp = -1
    for j in mine[i]:
        if j in winning[i]:
            exp+=1
            sol2[i+exp+1]+=1*sol2[i]
            

    
    if exp >-1:
        sol1+=2**exp

print('part 1: ',sol1)
print('part2: ', sum(sol2))

