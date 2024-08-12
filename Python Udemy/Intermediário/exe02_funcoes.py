


#total = 1

def multiplica(*args):
    total = 1
    for num in args:
        total *= num 
    
    return total
        
res_multiplicação = multiplica(2, 4, 6)
#print(res_multiplicação)


def par_inpa(valor):
    res = valor % 2 == 0
    if res:
        return f'O número {valor} é par.'
    
    return f'O número {valor} é inpa.'

par_ou_impa = par_inpa(11)
print(par_ou_impa)    
