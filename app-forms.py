#Código1
import tkinter as tk
from tkinter import messagebox
import sqlite3
conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL
)
""")
conexao.commit()
def salvar_cliente():
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos antes de salvar!"
        )
        return
    try:
        cursor.execute("""
            INSERT INTO clientes (nome, email, telefone)
            VALUES (?, ?, ?)
        """, (nome, email, telefone))
        conexao.commit()
        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )
        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível salvar o cliente:\n{erro}"
        )
def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_nome.focus()
def fechar_aplicacao():
    conexao.close()
    janela.destroy()
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("400x350")
janela.resizable(False, False)
titulo = tk.Label(
    janela,
    text="CADASTRO DE CLIENTES",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=20)
tk.Label(janela, text="Nome:").pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack(pady=5)
tk.Label(janela, text="E-mail:").pack()
entrada_email = tk.Entry(janela, width=40)
entrada_email.pack(pady=5)
tk.Label(janela, text="Telefone:").pack()
entrada_telefone = tk.Entry(janela, width=40)
entrada_telefone.pack(pady=5)
botao_salvar = tk.Button(
    janela,
    text="Salvar Cliente",
    width=20,
    bg="green",
    fg="white",
    command=salvar_cliente
)
botao_salvar.pack(pady=10)
botao_limpar = tk.Button(
    janela,
    text="Limpar Formulário",
    width=20,
    command=limpar_formulario
)
botao_limpar.pack(pady=5)
janela.protocol("WM_DELETE_WINDOW", fechar_aplicacao)
janela.mainloop()

#Código2

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL
)
""")
conexao.commit()
def salvar_cliente():
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos antes de salvar!"
        )
        return
    try:
        cursor.execute("""
            INSERT INTO clientes (nome, email, telefone)
            VALUES (?, ?, ?)
        """, (nome, email, telefone))
        conexao.commit()
        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )
        limpar_formulario()
    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível salvar o cliente:\n{erro}"
        )
def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_nome.focus()
def visualizar_clientes():
    janela_clientes = tk.Toplevel(janela)
    janela_clientes.title("Clientes Cadastrados")
    janela_clientes.geometry("700x350")
    janela_clientes.resizable(True, True)
    titulo_lista = tk.Label(
        janela_clientes,
        text="CLIENTES CADASTRADOS",
        font=("Arial", 16, "bold")
    )
    titulo_lista.pack(pady=15)
    colunas = ("ID", "Nome", "E-mail", "Telefone")
    tabela = ttk.Treeview(
        janela_clientes,
        columns=colunas,
        show="headings"
    )
    tabela.heading("ID", text="ID")
    tabela.heading("Nome", text="Nome")
    tabela.heading("E-mail", text="E-mail")
    tabela.heading("Telefone", text="Telefone")
    tabela.column("ID", width=50, anchor="center")
    tabela.column("Nome", width=200)
    tabela.column("E-mail", width=220)
    tabela.column("Telefone", width=150)
    tabela.pack(fill="both", expand=True, padx=10, pady=10)
    try:
        cursor.execute("""
            SELECT id, nome, email, telefone
            FROM clientes
            ORDER BY id
        """)
        clientes = cursor.fetchall()
        if not clientes:
            messagebox.showinfo(
                "Informação",
                "Não existem clientes cadastrados!",
                parent=janela_clientes
            )
        else:
            for cliente in clientes:
                tabela.insert("", tk.END, values=cliente)
    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível consultar os clientes:\n{erro}",
            parent=janela_clientes
        )
def fechar_aplicacao():
    conexao.close()
    janela.destroy()
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("400x420")
janela.resizable(False, False)
titulo = tk.Label(
    janela,
    text="CADASTRO DE CLIENTES",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=20)
tk.Label(janela, text="Nome:").pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack(pady=5)
tk.Label(janela, text="E-mail:").pack()
entrada_email = tk.Entry(janela, width=40)
entrada_email.pack(pady=5)
tk.Label(janela, text="Telefone:").pack()
entrada_telefone = tk.Entry(janela, width=40)
entrada_telefone.pack(pady=5)
botao_salvar = tk.Button(
    janela,
    text="Salvar Cliente",
    width=20,
    bg="green",
    fg="white",
    command=salvar_cliente
)
botao_salvar.pack(pady=10)
botao_limpar = tk.Button(
    janela,
    text="Limpar Formulário",
    width=20,
    command=limpar_formulario
)
botao_limpar.pack(pady=5)
botao_visualizar = tk.Button(
    janela,
    text="Visualizar Clientes",
    width=20,
    bg="blue",
    fg="white",
    command=visualizar_clientes
)
botao_visualizar.pack(pady=5)
janela.protocol("WM_DELETE_WINDOW", fechar_aplicacao)
janela.mainloop()
