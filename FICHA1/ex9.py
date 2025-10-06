altura = float(input("Altura em m: "))
peso = float(input("Peso em kgs: "))
imc = float( peso / ((altura)**2))
print ("O seu IMC é:",imc)

if imc < 18.5:
    print(f"Abaixo do peso")
elif imc < 25:
    print(f"Peso normal")
elif imc < 30:
    print(f"Excesso de peso")
elif imc < 35:
    print(f"Obesidade grau I")
elif imc < 40:
    print(f"Obesidade grau II")
else:
    print(f"Obesidade grau III")