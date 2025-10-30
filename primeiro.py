print("Olá, mundo!")

#------------Estrutura condicional------------
# Condição IF - ELIF - ELSE
idade = 18
if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem 18 anos.")
else:
    print("Você é maior de idade.")

pais = "Brasil"
if pais == "Brasil":
    print("O país é Brasil.")
else:
    print("O país não é Brasil.")

# Loop FOR que itera sobre uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# Loop WHILE (Enquanto)
contador = 0
while contador <= 5:
    print(contador)
    contador += 1

#-----------Funções------------
# Definindo a função
def saudacao(nome):
    return "Olá, " + nome + "!"

# Chamando a função
mensagem = saudacao("Maria")
print(mensagem)

# Função com valor padrão
def saudacao2(nome="Visitante"):
    return "Olá, " + nome + "!"

# Chamando a função sem argumento
print(saudacao2())
# Chamando a função com argumento
print(saudacao2("Ana"))

# ----------Manipulação de arquivos-----------
# Abrindo (ou criando) um arquivo para escrita
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Olá, Mundo!\n")
    arquivo.write("Segunda Linha.")

# Abrindo o arquivo para leitura
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# --------- Bibliotecas e Módulos -------------
# Importando módulos
import math

# Usar uma função do módulo MATH
raiz = math.sqrt(16)
print(raiz)

# ----------Criando e Usando Módulos -------------

# Usar o módulo
import meu_modulo

mensagem = meu_modulo.saudacao3("Carlos")
print(mensagem)

