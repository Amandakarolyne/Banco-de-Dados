CREATE TABLE Itens_Venda (
    Codigo_Item INT PRIMARY KEY,
    Nome_Item VARCHAR(100) NOT NULL,
    Preco_Unitario DECIMAL(10, 2) NOT NULL,
    Observacoes TEXT
);
SELECT * FROM Itens_Venda;
