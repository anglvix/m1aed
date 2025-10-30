def dataGrades(grades):
    maior = max(grades)
    menor = min(grades)
    media = sum(grades)/len(grades)
    acima = sum(1 for g in grades if g>media)
    return maior, menor, acima

grades=[]
while len(grades)<10:
    try:
        g=float(input(f"Nota do aluno {len(grades)+1}: "))
        if 0<=g<=20:
            grades.append(g)
        else:
            print("Valor fora do intervalo 0-20")
    except:
        print("Entrada inválida")
maior,menor,acima = dataGrades(grades)
print("Maior:",maior)
print("Menor:",menor)
print("Nº acima da média:",acima)
