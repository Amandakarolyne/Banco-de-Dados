-- Ativar suporte a chaves estrangeiras no SQLite
PRAGMA foreign_keys = ON;

-- Criação da tabela Clientes
CREATE TABLE Clientes (
    ID INTEGER PRIMARY KEY,
    nomeCliente VARCHAR(100) NOT NULL,
    emailCliente VARCHAR(100) UNIQUE
);

-- Criação da tabela Compras
CREATE TABLE Compras (
    CompraID INTEGER PRIMARY KEY,
    ClienteID INTEGER,
    NomeLivro VARCHAR(150) NOT NULL,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
);

SELECT 
    clientes.nome AS NomeCliente,
    livros.titulo AS NomeLivro
FROM compras
INNER JOIN clientes ON compras.cliente_id = clientes.id
INNER JOIN livros ON compras.livro_id = livros.id;
