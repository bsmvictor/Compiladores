# Importar biblioteca de REGEX
import re

#Texto usado para os testes
txt = 'Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz'

# Retornando a posição inicial e final de todos os matches
for match in re.finditer("inspiração", txt):
    print(match.span())