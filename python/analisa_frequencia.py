# --------------------------------------------------------------
# Analisa a frequencia que aparece uma letra em um texto/String
# --------------------------------------------------------------
# 
# 1 - Iniciar um Array
# 2 - Iniciar um Dict vazio
# 3 - Iterar a lista 
#   3.1 - Se a letra não existe, defina o valor 1
#   3.2 - Else, incrementar o valor em 1 
# 4 - Imprimir a frequencia de cada letra iterando o Dict
# --------------------------------------------------------------
# Iniciar a lista 
# letras = ['a','b','c','c','a','z','a','b','c']

# Trima a string e converte em lowercase
texto = " O Reio Liar e um rei soberano aaaaa aaaaaa aaaaaa dddddddd dddd ddd nas terras altas da escocia".replace(" ","").lower()

# converter o texto em um array de char. 
letras = [letra for letra in texto]

# Iniciar o Dict
contador_letras = {}

for l in letras:
    if l in contador_letras:
        contador_letras[l] += 1
    else:
        contador_letras[l] = 1

# Ordena um Dic por valores. 
for key, value in sorted(contador_letras.items(),key=lambda x:x[1],reverse=True):
    print(f"{key}: {value}")