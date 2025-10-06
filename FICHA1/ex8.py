sexo=input("Sexo (M/F): ").upper()
altura = int(input("Altura em cm: "))

if sexo=="M":
    pesoid = (altura-100)-(altura-150)/4
elif sexo=="F":
    pesoid = (altura-100)-(altura-150)/2
else:
    pesoid=None

if pesoid:
    print(f"Peso Ideal: {pesoid}")
else:
    print("Algo correu mal.")
