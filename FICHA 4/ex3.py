import random

gerados=[]
usados=set()
n=random.randint(1,100)
gerados.append(n); usados.add(n)
print("Gerado:",n)
while True:
    if n==100:
        break
    r=input("Gerar novo número (S/N)? ").strip().upper()
    if r!="S":
        break
    poss=[x for x in range(n+1,101) if x not in usados]
    if not poss:
        print("Não é possível gerar mais números.")
        break
    n=random.choice(poss)
    gerados.append(n); usados.add(n)
    print("Gerado:",n)
    if n==100:
        break
print("Números gerados (decrescente):",sorted(gerados,reverse=True))
