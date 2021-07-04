# Verificar se um número é menor que vinte e par
val = 55

if val % 2 == 0 and val < 20:
    print("O numero eh par e menor que 20!")
elif val % 2 == 0:
    print("O numero eh par, mas nao eh menor que 20!")
elif val < 20:
    print("O numero eh menor que 20, mas nao eh par!")
else:
    print("O numero nao eh par, nem eh menor que 20!")
