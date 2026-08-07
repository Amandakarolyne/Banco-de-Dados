SELECT
    Clientes.nomeCliente,
    Compras.NomeLivro
FROM Clientes
LEFT JOIN Compras ON Clientes.ID = Compras.ClienteID;

SELECT
    Clientes.nomeCliente,
    Compras.NomeLivro
FROM Clientes
RIGHT JOIN Compras ON Clientes.ID = Compras.ClienteID;
