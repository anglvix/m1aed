sexo=input("Sexo (M/F): ").upper()
idade=int(input("Idade: "))

if sexo=="M":
    fcm=220-idade
elif sexo=="F":
    fcm=226-idade
else:
    fcm=None

if fcm:
    print(f"Frequência Cardíaca Máxima: {fcm} bpm")
else:
    print("Sexo inválido.")
