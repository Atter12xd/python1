contador = 0
numero = 0
while contador <10:
    cubo = numero **3
    print("cubo de",numero,"es",cubo)
    contador +=1
    numero +=2

altura = 10
for i in range(1 , altura +1):
    print("*"*i)
for i in range(altura -1,0,-1):
    print("*"*i)