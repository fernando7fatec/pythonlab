A = [[2,9],[3,8],[2,7]]



# Fator deve ser um número inteiro maior que 1 , x E Z , x >= 1
fator=5
r = 1

for a in range(fator):
    print(" Fator ",fator," resultado ! = ",r)

    # Calcula o valor fatorial de um numero inteiro
    r += r * (fator - 1)
    fator -= 1
    #print(r)
print(" ==== ")
print(r)
    
    