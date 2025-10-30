def searchNumber(lst,val):
    pos=[i+1 for i,x in enumerate(lst) if x==val]
    return pos

lst=[]
while len(lst)<10:
    try:
        x=int(input(f"Insira inteiro {len(lst)+1}: "))
        lst.append(x)
    except:
        print("Entrada inválida")
try:
    s=int(input("Valor a procurar: "))
    pos=searchNumber(lst,s)
    if pos:
        print("Encontrado nas posições:",pos)
    else:
        print("Valor não encontrado na lista")
except:
    print("Entrada inválida")
