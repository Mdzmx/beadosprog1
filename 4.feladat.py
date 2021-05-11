lista =[]
while len(lista) != 16:
    szo = input("Adj meg egy szót: ")
    if szo == "":
        break
    else:
        lista.append(szo)
print(lista)
lista2 = []
for i in range(0, len(lista)):
    for j in range(len(lista[i]+1)):
        for k in range(j,len(lista[i])+1):
            if lista[i][j:k] == "":
                k += 1
            print(i,j,k)





