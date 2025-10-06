idade = int(input("Idade: "))

if 0 <= idade <= 1:
    etapa = "Primeira infância"
elif 2 <= idade <= 4:
    etapa = "Infância"
elif 5 <= idade <= 11:
    etapa = "Segunda infância"
elif 12 <= idade <= 18:
    etapa = "Adolescência"
elif 19 <= idade <= 29:
    etapa = "Adulto – Jovem adulto"
elif 30 <= idade <= 59:
    etapa = "Adulto – Meia idade"
elif 60 <= idade <= 74:
    etapa = "Idoso – Idade madura"
elif 75 <= idade <= 90:
    etapa = "Velhice"
else:
    etapa = "Longevidade (acima de 90 anos)"

print(etapa)
