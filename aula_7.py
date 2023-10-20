A = [0,3,-2,7,9,11,15,0,0,0,0]
B = [0,4,0,7,9,11,15,0,1,0,1]
soma = 0

for a in range(len(A)):
   soma += (A[a] - B[a]) ** 2

print(" ")
print(" -------- ")
print(" ",soma)
print(" -------- ")

