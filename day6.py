input = []
input2 =[]
import os, math

absolute_path = os.path.dirname(__file__)
with open(absolute_path+"/day5.txt") as my_file:
    for line in my_file:
        linea = line[line.index(':')+1:-1].split(' ')
        races = []
        for i in linea:
            if i != '':
                races.append(i)
        input2.append(int(line[line.index(':')+1:-1].replace(" ","")))
        input.append(races)

data=[]
for i in range (len(input[0])):
    val = []
    for j in range(len(input)):
        val.append(int(input[j][i]))
    data.append(val)


sol = 1
for i in data:
    count = 0
    numOut=0
    for j in range(math.ceil(i[0]/2)):
        if j*(i[0]-j)>i[1]:
            count = (i[0]+1-numOut*2)
            break
        numOut+=1
    sol*=count
print('part1: ', sol)

count = 0
numOut=0
for i in range(math.ceil(input2[0]/2)):
    if i*(input2[0]-i)>input2[1]:
        count = (input2[0]+1-numOut*2)
        break
    numOut+=1


print('part2: ', count)