import random
print("Sorteador :D")
q = str(input("Iten 1: "))
w = str(input("Iten 2: "))
e = str(input("Iten 3: "))
r = str(input("Iten 4: "))
queue = [q, w, e, r]
selected = random.choice(queue)

print("A opção escolhida foi: {}" .format(selected))
