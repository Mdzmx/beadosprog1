szo = input("Adj  meg egy szót: ")
lista = []
lista2 = []

for i in range(0,len(szo)+1):
    for j in range(i,len(szo)+1):
        if szo[i:j] == "":
             j += 1
        else:
            lista.append(szo[i:j])
            j += 1
    i += 1
for i in range(0,len(lista)):
    if lista[i] == lista[i][::-1]:
        lista2.append(lista[i])
        i += 1
    else:
        i += 1

print(lista)
print(lista2)
