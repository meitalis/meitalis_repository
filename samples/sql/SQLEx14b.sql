SELECT ProductID, ProductName
FROM Products
EXCEPT
SELECT p.ProductID, p.ProductName
FROM Orders o JOIN [Order Details] od 
	ON 	o.OrderId = od.OrderID 
	JOIN Products p 
	ON p.ProductID = od.ProductID
WHERE o.CustomerID = 'QUEEN'




