# -*- coding: utf-8 -*-
soma = 0 
for x in range(1, 1000001):
    soma+=(x**(1/2) + 1/x)    
somatorio = soma /5
print(somatorio)

x=1
soma=0
while x <= 1000000:
    soma+=(x**(1/2) + 1/x)    
    x+=1
somatorio = soma /5
print(somatorio)
