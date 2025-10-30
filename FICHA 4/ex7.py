import re
texto=input("Texto: ")
palavra=input("Palavra de procura: ")
padrao=re.compile(r"\b"+re.escape(palavra)+r"\b",flags=re.IGNORECASE)
ocorrencias=len(padrao.findall(texto))
print("Ocorrências:",ocorrencias)
