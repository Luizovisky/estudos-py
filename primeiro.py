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

# ---------------------POO------------------------
# ---------Classes e Objetos------------

# Definição de uma classe:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# -----------Criar e usar um objeto------------
# Criar um objeto de classe Pessoa
pessoa1 = Pessoa("João", -1)

# Usar o método do objeto
print(pessoa1.apresentar())

# ---------- Exceções e Erros ----------------
# Tratamento de exceções

# Capturar Exceções:
try:
    resultado = 10/0
except ZeroDivisionError:
    print("Não é possível dividir por zero.")

# ----------- Exceções Personalziadas --------------
# Definir e usar exceções personalizadas
class ErroPersonalizado(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
    
def verificar_idade(idade):
    if idade < 0:
        raise ErroPersonalizado("A idade não pode ser negativa.")
    
try:
    verificar_idade(-5) 
except ErroPersonalizado as e:
    print(e)

# ------------ Manipulação de Dados --------------------
# Listas e Dicionários

# Criar uma lista
frutas = ["maçã", "banana", "laranja"]

# Adicionar um item à lista
frutas.append("uva")

# Acessar um item da lista
print(frutas[1]) # Imprime "banana"

# Dicionários
# Criar um dicionário
aluno = {
    "nome": "Pedro",
    "idade": 20
}

# Adicionar um item ao dicionário
aluno["curso"] = "Python"

# Acessar um item do dicionário
print(aluno["nome"]) # Imprime "Pedro"

# ---------- Trabalhando com Bibliotecas Externas ------------
# Instalando Bibliotecas com Pip

# Usar a Biblioteca Requests
import requests

resposta = requests.get("https://api.github.com")
print(resposta.status.code)