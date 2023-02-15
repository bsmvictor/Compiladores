# Importar biblioteca de REGEX
import re

#Texto usado para os testes
txt = 'Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz'

#Buscando a palavra 'sonhos'
x = re.search('sonhos',txt)

#Condicional para o match caso não seja nulo
if x:
    print('Encontrado!')