from os import link
import requests
import tkinter as tk

# Criação de uma Janela
win=tk.Tk()
win.geometry('400x400')
# Criação de uma caixa de texto para inserção de valores
inputtext=tk.Entry(win, width=20, font=('Arial 14'))
inputtext.pack(pady=5)
# Função para buscar um CEP
def buscar_cep():

    try:
        cep=inputtext.get()
        cep = cep.replace("-", "").replace(".", "").replace(" ", "")
        int(cep)
    except:
        tk.Label(win, text="Cep não encontrado", font=("Arial 10")).pack()
    if len(cep) == 8:
        link = f'https://viacep.com.br/ws/{cep}/json/'
        r = requests.get(link)
        dic_end = r.json()
        if 'erro' in dic_end:
            exit()
        
        tk.Label(win, text=(f"""    
    Cep: {dic_end['cep']}
    Cidade: {dic_end['localidade']}, {dic_end['uf']}
    Bairro: {dic_end['bairro']}
    Rua: {dic_end['logradouro']}
        """), font=('Arial 10')).pack()
        
# Botão que chama a função de busca
botao_busca=tk.Button(win, text="Buscar CEP", command=buscar_cep)
botao_busca.pack()

win.mainloop()

