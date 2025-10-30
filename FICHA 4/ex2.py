import random

def generateEuromillionKeys():
    numeros=sorted(random.sample(range(1,51),5))
    estrelas=sorted(random.sample(range(1,13),2))
    return numeros,estrelas

while True:
    nums,stars=generateEuromillionKeys()
    print("Números:",nums,"Estrelas:",stars)
    r=input("Gerar nova chave (S/N)? ").strip().upper()
    if r!="S":
        break
