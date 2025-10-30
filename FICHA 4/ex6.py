dias=["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"]
vis=[]
i=0
while i<7:
    try:
        n=int(input(f"Nº visitantes {dias[i]}: "))
        vis.append(n); i+=1
    except:
        print("Entrada inválida")
desc=sorted(vis,reverse=True)
media=sum(vis)/7
mais_proximo=min(range(7), key=lambda i: abs(vis[i]-media))
print("Visitantes (decrescente):",desc)
print(f"Média: {media:.2f}")
print("Dia mais próximo da média:",dias[mais_proximo])
