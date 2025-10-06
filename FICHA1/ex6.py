seg = int(input("Insira o tempo em seg: "))

horas = seg // 3600
seg %= 3600
min = seg // 60
seg%= 60

print(f"{horas} horas, {min} minutos, {seg} segundos")