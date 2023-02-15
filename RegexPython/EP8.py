# Importar biblioteca de REGEX
import re

#Texto usado para os testes
txt = 'Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz'

# Quebra (splits) o texto a cada espaço encontrado
x = re.split("\s", txt)

# Quantidade de Matches
print('Total de palavras:', len(x)) 