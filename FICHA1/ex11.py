idade = int(input("Idade: "))

match idade:
    case idade if 0 <= idade <= 1:
        etapa = "Primeira infância"
    case idade if 2 <= idade <= 4:
        etapa = "Infância"
    case idade if 5 <= idade <= 11:
        etapa = "Segunda infância"
    case idade if 12 <= idade <= 18:
        etapa = "Adolescência"
    case idade if 19 <= idade <= 29:
        etapa = "Adulto – Jovem adulto"
    case idade if 30 <= idade <= 59:
        etapa = "Adulto – Meia idade"
    case idade if 60 <= idade <= 74:
        etapa = "Idoso – Idade madura"
    case idade if 75 <= idade <= 90:
        etapa = "Velhice"
    case _:
        etapa = "Longevidade (acima de 90 anos)"

print(etapa)

