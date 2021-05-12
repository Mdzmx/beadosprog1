s = input("adj meg egy sztringet: ")
kereso = input("adj meg egy karakter sorozatot: ")

lista = []
lista2 = []
lista3 = []
a = (-1)+len(s)
b = len(s)
megvan = ""

for i in range(0, len(s) + 1):
    if s[a:b] == s:
        break

    elif s[i] in kereso:
        lista3.append(s[a:b])
        a  -=1

    else:
        a -= 1
for j in range(0,len(kereso)+1):
    for k in range(0,len(lista3)+1):
        if  j == k:
            megvan = k


print(lista3[1],lista3[2])
