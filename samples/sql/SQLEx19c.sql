SELECT EmployeeId, OrderId, OrderDate
FROM Orders o
WHERE o.OrderDate = (SELECT MAX(OrderDate)
					 FROM Orders o2
					 WHERE o2.EmployeeID = o.EmployeeID)

SELECT OrderId, OrderDate
FROM Orders
WHERE EmployeeId = 9
