meses=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
vendas=[]
i=0
while i<12:
    try:
        v=float(input(f"Vendas de {meses[i]}: "))
        vendas.append(v); i+=1
    except:
        print("Entrada inválida")
def mes_max(v):
    return meses[v.index(max(v))]
def mes_min(v):
    return meses[v.index(min(v))]
def media(v):
    return sum(v)/len(v)
print("Mês com maior vendas:",mes_max(vendas))
print("Mês com menor vendas:",mes_min(vendas))
print("Média mensal:",media(vendas))
