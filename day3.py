input = []
import os

absolute_path = os.path.dirname(__file__)
with open(absolute_path+"/day3.txt") as my_file:
    for line in my_file:
        val =[]
        for i in range(len(line)):
            if line[i].isdigit():
                val.append(int(line[i]))
            
            else:
                val.append(line[i])
        input.append(val[:-1])
        val=[]



def nav(fila, columna, input):
    sol = 0
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        nx = fila + dx[i]
        ny = columna + dy[i]
        if nx >= 0 and nx < len(input[0]) and ny >= 0 and ny < len(input) and type(input[nx][ny])==int:
            #izq
            number=str(input[nx][ny])
            input[nx][ny]=number
            posy=ny-1
            while posy>-1 and type(input[nx][posy])==int:
                number =str(input[nx][posy])+number
                input[nx][posy]=str(input[nx][posy])
                posy-=1
            
            #der
            posy=ny+1
            while posy<len(input[nx]) and type(input[nx][posy])==int:
                number +=str(input[nx][posy])
                input[nx][posy]=str(input[nx][posy])
                posy+=1
            sol+=int(number)
            number=''
    return sol, input
    
def gear(fila, columna, input):
    sol = 1
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    count = 0

    for i in range(8):
        nx = fila + dx[i]
        ny = columna + dy[i]
        if nx >= 0 and nx < len(input[0]) and ny >= 0 and ny < len(input) and type(input[nx][ny])==int:
            count+=1
            #izq
            number=str(input[nx][ny])
            input[nx][ny]=number
            posy=ny-1
            while posy>-1 and type(input[nx][posy])==int:
                number =str(input[nx][posy])+number
                input[nx][posy]=str(input[nx][posy])
                posy-=1
            
            #der
            posy=ny+1
            while posy<len(input[nx]) and type(input[nx][posy])==int:
                number +=str(input[nx][posy])
                input[nx][posy]=str(input[nx][posy])
                posy+=1
            sol*=int(number)
            number=''
    
    if count ==2:
        return sol,input
    return 0, input
                


sol = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == '*':
            fun = gear(i,j, input)
            sol+=fun[0]
            input=fun[1]
        """if type(input[i][j])==str and input[i][j] != '.':
            fun=nav(i,j, input)
            sol+=fun[0]
            input=fun[1]"""
        

#print("part 1: ", sol)
print("part 2: ", sol)




