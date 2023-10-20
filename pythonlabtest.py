import random

tamanho_senha = 2

senha=[]
senha_temp=[]

print("\n\n\n Gera a senha: \n\n")
for x in range(1,tamanho_senha+1):
    senha.append(random.randrange(1,4))

print(" Senha criada: ")
print(" =>",senha)
print(" ======= \n")

print("Descobrir a senha : ")
print(" ======= \n\n\n")

for a in range(1,tamanho_senha+1):
    for b in range(len(senha)):
        senha_temp.append(senha[b])
        print(a,b)
   
print("**** senha temp")
print(senha_temp)