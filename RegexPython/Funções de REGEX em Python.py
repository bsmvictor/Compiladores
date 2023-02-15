# -------------------1.Importando o módulo “re”no Python----------------------------

# Importar biblioteca de REGEX
import re

#variável que guarda um texto
texto = 'Os melhores engenheiros são do Brasil'

#Teste que verifica se o texto começa com "Os" e termina com "Brasil"
x = re.search("^Os.*Brasil$", texto)

#Verificando x: ou x==TRUE
if x:
    print('\nPERFEITO! Tivemos um match no Teste :)\n')
else:
    print('\nNão tivemos um match no Teste :(\n')

# -------------------------2.A função findall()--------------------------------

#Exemplo com findall()
txt = ('oi! teu pai tem boi? Foi o que pensei.')
    
#retorna uma lista contendo cada ocorrência de "oi" dentro de um texto.
x = re.findall('oi',txt)

# Matches Encontrados
print('\n\tMatches:', x)

# Quantidade de Matches len = tamanho de
print('\n\tQuantidade:', len(x))

# --------------------------3.A função search()-------------------------------

# Texto para realizarmos o teste
txt = "O rato roeu a roupa do rei de roma. Que rato danado!"

# Este teste retorna um "Match Object" se a String rato for encontrada
x = re.search("rato", txt)

# Se o "Match Object" nao for nulo (None)
if x:
    print("PERFEITO! Tivemos um match no Teste :)")
    print("O primeiro rato foi encontrado na posição:", x.start())
    
# ---------------------------3.1. .span()------------------------------------

# Este teste retorna um "Match Object" se uma palavra começar com r e terminar com o
x = re.finditer("r[a-z]+o", txt):
print (x.span():)

# Retornando a posição inicial e final de todos os matches
for match in re.finditer("r[a-z]+o", txt):
    print(match.span())

# -----------------------------3.2. .group()-------------------------------

# Este teste retorna um "Match Object" se uma palavra possuir a no meio
x = re.search("[a-z]*a[a-z]*", txt)
print(x.group())

# Retornando as Strings de todos os matches
for match in re.finditer("[a-z]*a[a-z]*", txt):
    print(match.group())

# -------------------------------4.A função split()-------------------------------

# Texto para realizarmos o teste
txt = "Eu gosto de sorvete de chocolate; meu pai, de creme; meu irmão, de morango"

# Quebra (splits) o texto a cada ; encontrado
x = re.split(";", txt)
print(x)

# Quebra (splits) o texto a cada espaço encontrado
y = re.split("\s", txt)
print(y) 

# -----------------------------5.A função sub()-------------------------------

# Texto para realizarmos o teste
txt = "Quando chover, busque pelo arco-íris. Quando escurecer, busque pelas estrelas."

# Este teste substitui cada palavra "Quando" por "Sempre que"
x = re.sub("Quando", "Sempre que", txt)
print(x) 
