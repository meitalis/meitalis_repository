SELECT DISTINCT o.CustomerId, od.UnitPrice, p.ProductID, p.ProductName
FROM Orders o
	 JOIN [Order Details] od
	 ON o.OrderID = od.OrderID
	 JOIN Products p
	 ON od.ProductID = p.ProductID
WHERE od.UnitPrice = (SELECT MAX(od2.UnitPrice)
					  FROM Orders o2 
						   JOIN [Order Details] od2
						   ON o2.OrderID = od2.OrderID
					  WHERE o2.CustomerID = o.CustomerID)






