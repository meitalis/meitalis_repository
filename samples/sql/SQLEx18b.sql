SELECT DISTINCT e.EmployeeID, e.FirstName, e.LastName
FROM Employees e JOIN Orders o
	 ON e.EmployeeID = o.EmployeeID
	 JOIN [Order Details] od
	 ON o.OrderID = od.OrderID
WHERE od.UnitPrice > (SELECT Max(UnitPrice)
					  FROM [Order Details] od2 JOIN Orders o2
						ON od2.OrderID = o2.OrderID
						JOIN Employees e2
						ON o2.EmployeeID = e2.EmployeeID
					  WHERE e2.FirstName = 'Steven' AND e2.LastName = 'Buchanan')

-- Solution B
SELECT DISTINCT e.EmployeeID, e.FirstName, e.LastName
FROM Employees e JOIN Orders o
	 ON e.EmployeeID = o.EmployeeID
	 JOIN [Order Details] od
	 ON o.OrderID = od.OrderID
WHERE od.UnitPrice > ALL (SELECT UnitPrice
						  FROM [Order Details] od2 JOIN Orders o2
							ON od2.OrderID = o2.OrderID
							JOIN Employees e2
							ON o2.EmployeeID = e2.EmployeeID
						  WHERE e2.FirstName = 'Steven' AND e2.LastName = 'Buchanan')		  