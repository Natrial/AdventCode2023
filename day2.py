input = []
import os, numpy

absolute_path = os.path.dirname(__file__)
with open(absolute_path+"/day2.txt") as my_file:
    for line in my_file:
        input.append(line[line.index(':')+ 2:-1].replace(';', ',').split(", "))

#only 12 red cubes, 13 green cubes, and 14 blue cubes
contador =0
contador2=0
for i in input:
    #print(i)
    colors=[0,0,0]
    for j in i:
        if 'red' in j and int(j[:j.index(' ')])>colors[0]:
            colors[0]=int(j[:j.index(' ')])
        elif 'green' in j and int(j[:j.index(' ')])>colors[1]:
            colors[1]=int(j[:j.index(' ')])
        elif 'blue' in j and int(j[:j.index(' ')])>colors[2]:
            colors[2]=int(j[:j.index(' ')])

    contador2 += numpy.prod(colors)
    if colors[0]<=12 and colors[1]<=13 and colors[2]<=14:
        contador+=input.index(i)+1

print('part 1:'+str(contador))
print('part 2:'+str(contador2))


            


   