#Dicionários em Python
#dict
#coleção não ordenada, mutável e indexada declarada com chaves e têm chaves e valores.

dict_regiao_norte = {
    "id":1,
    "sigla":"N",
    "nome":"Norte"
    }
print(dict_regiao_norte)

x = dict_regiao_norte.get("nome", "Não encontrei")
print(x)


#MUDAR VALORES
dict_regiao_norte = {
    "id":1,
    "sigla":"N",
    "nome":"Norte"}

print(dict_regiao_norte)   

dict_regiao_norte["id"] = 20

print(dict_regiao_norte)
