file = open('o_x.txt', 'r') 
  
valido = True
countX = 0
countO = 0

while 1: 
    char = file.read(1)           
    if not char:  
        break
    else:
        if (char != 'X' and char != 'O'):
            valido = False
            break
        else:
            if char == 'X':
                countX += 1
            else:
                countO += 1

if not valido:
    print("Ficheiro inválido")
else:
    print("Count X: ", countX)
    print("Count O: ", countO)