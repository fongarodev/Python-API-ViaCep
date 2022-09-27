from os import link
import requests

print('~' * 40)
print("API Viacep")
print('~' * 40)

cep = input("Digite o cep para busca: ")

try:
    cep = cep.replace("-", "").replace(".", "").replace(" ", "")
    int(cep)
except:
    print("Cep invalido")
    exit()

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'
    r = requests.get(link)
    dic_end = r.json()
    if 'erro' in dic_end:
        print("Cep não encontrado")
        exit()
    
    print(f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
Cep: {dic_end['cep']}
Cidade: {dic_end['localidade']}, {dic_end['uf']}
Bairro: {dic_end['bairro']}
Rua: {dic_end['logradouro']}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

else:
    print("Cep Invalido")