# -*- coding: utf-8 -*-
def somatorio(i, j):
    soma=0
    for x in range(i, j+1):
        soma+=(x**(1/2) + 1/x)    
        somat = soma /5
    return somat

print(somatorio(100,150))

var_som = somatorio(1000, 20000)
print(var_som)