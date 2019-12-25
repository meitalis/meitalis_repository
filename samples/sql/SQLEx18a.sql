SELECT p.ProductId, p.ProductName
FROM Products p JOIN [Order Details] od
     ON p.ProductID = od.ProductID
GROUP BY p.ProductID, p.ProductName
HAVING Sum(od.Quantity) >= ALL(SELECT Sum(Quantity)
							   FROM [Order Details] 
							   GROUP BY ProductID)
