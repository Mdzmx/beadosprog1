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
    for j in range(len(lista[i])+1):
        for k in range(j,len(lista[i])+1):
            if lista[i][j:k] == "":
                k += 1
            elif len(lista[i][j:k]) > 3 and lista[i][j:k] == lista[i][j:k][::-1]:
                lista2.append('{} {}'.format(lista[i][j:k],i))
print(lista2)

listasorted = sorted(lista2)
vegso = sorted(lista,key=len)
for i in range(len(vegso)):
    print(vegso[i])



