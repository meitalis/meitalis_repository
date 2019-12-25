SELECT o.CustomerId
FROM Orders o
JOIN [Order Details] od
ON o.OrderID = od.OrderID
WHERE o.CustomerId NOT IN (SELECT o2.CustomerId
                           FROM Orders o2
						   JOIN [Order Details] od2
						   ON o2.OrderID = od2.OrderID
						   JOIN Products p2
						   ON od2.ProductID = p2.ProductID
						   GROUP BY o2.CustomerID, p2.CategoryID
						   HAVING COUNT(Distinct p2.ProductID) >= 2 
						   )
GROUP BY o.CustomerID
HAVING Count(Distinct od.ProductID) >= 3

