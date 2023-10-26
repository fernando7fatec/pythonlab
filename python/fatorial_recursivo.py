contador = 0
resultado = 0

def fatorial_recursivo(n):
    global contador
    global resultado

    if contador <= n:
        resultado += n*(n-1)
        contador += 1
        n = n - 1
        print(resultado)
        fatorial_recursivo(n)
    return resultado
        
# Resultado fatorial 
fator = 5 #int(input(" Digite o Fator : "))
i = fatorial_recursivo(fator)

print("O Fatorial de ",fator, "é ", i)