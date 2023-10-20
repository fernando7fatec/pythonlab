count = 0

A = [1,2,3,4]
B = ['X','Y','Z']

for a in (A):
    for b in (B):
        print("(",a,",",b,")")
        count += 1

print(" Total de combinacoes entre conjunto A e B ")
print(count)
