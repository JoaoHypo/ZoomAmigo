'''
ZoomAmigo
Projeto ZoomAmigo | Incluir - UFRGS
Este projeto visa desenvolver um aplicativo que auxilie pessoas com
baixa visão a interagirem com planílhas excel de forma mais prática e acessível
'''

#Código base, interagindo com 1 planílha

import pandas as pd
from tkinter import *

root = Tk()
root.title('Zoom Amigo')


filename = input("Digite o nome do arquivo: ")

# Lê o arquivo Excel
df = pd.read_excel(filename)

print(df)

# Pede para o usuário digitar a linha e coluna da célula desejada
linha = (int(input('Digite a linha da célula: '))-1)
coluna = input('Digite a coluna da célula: ')

# Imprime o conteúdo da célula
print(df.at[linha, coluna])

root.mainloop()