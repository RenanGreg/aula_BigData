import pandas as pd
import tkinter as tk
from tkinter import messagebox
import os

pasta_dados = r'D:\dados'
nome_arquivo = os.path.join(pasta_dados, 'dados.csv')


def salvar_dados():

    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    cidade = entry_cidade.get()


    if nome and idade and email and cidade:
        try:
            idade = int(idade)  # Tenta converter a idade para inteiro para garantir que seja um número


            df = pd.DataFrame([[nome, idade, email, cidade]], columns=["Nome", "Idade", "E-mail", "Cidade"])

            df.to_csv('dados.csv', mode='a', header=not pd.io.common.file_exists('dados.csv'), index=False)

            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")


            entry_nome.delete(0, tk.END)
            entry_idade.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_cidade.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser um número inteiro.")
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos antes de salvar.")


def sair():
    root.destroy()



root = tk.Tk()
root.title("Formulário de Entrada de Dados")


tk.Label(root, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Idade").grid(row=1, column=0)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1)

tk.Label(root, text="E-mail").grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

tk.Label(root, text="Cidade").grid(row=3, column=0)
entry_cidade = tk.Entry(root)
entry_cidade.grid(row=3, column=1)


botao_salvar = tk.Button(root, text="Salvar", command=salvar_dados)
botao_salvar.grid(row=4, column=0, pady=10)

botao_sair = tk.Button(root, text="Sair", command=sair)
botao_sair.grid(row=4, column=1, pady=10)


root.mainloop()
