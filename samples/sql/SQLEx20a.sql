SELECT o.CustomerId
FROM Orders o JOIN [Order Details] od
     ON o.OrderID = od.OrderID
	 JOIN Products p
	 ON od.ProductID = p.ProductID
WHERE p.UnitPrice < 5
GROUP BY o.CustomerID
HAVING Count(Distinct od.ProductID) = (SELECT Count(*)
									   FROM Products
									   WHERE UnitPrice < 5)

-- Option B
SELECT c.CustomerId
FROM Customers c
WHERE NOT EXISTS (SELECT p.ProductId
				  FROM Products p
				  WHERE UnitPrice < 5 AND p.ProductID NOT IN 
								(SELECT od.ProductID
								 FROM [Order Details] od JOIN Orders o
									ON o.OrderID = od.OrderID
								 	WHERE o.CustomerID = c.CustomerID
								))