
input = []
data =['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
import os

absolute_path = os.path.dirname(__file__)
with open(absolute_path+"/day1.txt") as my_file:
    for line in my_file:
        line = line.replace('one','o1e')
        line = line.replace('two','t2o')
        line = line.replace('three','t3t')
        line = line.replace('four','f4r')
        line = line.replace('five','f5e')
        line = line.replace('six','s6x')
        line = line.replace('seven','s7n')
        line = line.replace('eight','e8t')
        line = line.replace('nine','n9e')
        input.append(line[:-1])

sol = 0

for i in input:
    cadena  = ''
    for j in range(0,len(i)):
        if i[j].isdigit():
            cadena+=i[j]
        
    if len(cadena)>1:
        sol += int(cadena[:1]+cadena[-1:])
    else:sol += int(cadena+cadena)

print(sol)



