# ----------------------------------------
# Função recursiva
# Conta até 100 chamando a própria 
# função recursivamente. 
# ----------------------------------------

contador = 0;

def r(contador):

   contador += 1

   print(contador)

   if contador < 100:
    r(contador)

r(contador)


