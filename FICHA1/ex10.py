print("=== Simulador de Peso noutro Planeta ===")

planetas = {
    1: ("Mercúrio", 0.37),
    2: ("Vénus", 0.90),
    3: ("Marte", 0.37),
    4: ("Júpiter", 2.53),
    5: ("Saturno", 1.06),
    6: ("Urano", 0.91)
}

print("\nLista de planetas disponíveis:")
for codigo, (nome, gravidade) in planetas.items():
    print(f"{codigo} - {nome} (gravidade relativa = {gravidade})")

peso_terra = float(input("\nDigite o seu peso na Terra (kg): "))
codigo = int(input("Escolha o código do planeta (1-6): "))

if codigo in planetas:
    nome_planeta, gravidade = planetas[codigo]
    peso_planeta = peso_terra * gravidade / 0.98
    print(f"\nNo planeta {nome_planeta}, o seu peso seria de {peso_planeta:.2f} kg.")
else:
    print("\nCódigo inválido! Escolha um número entre 1 e 6.")
