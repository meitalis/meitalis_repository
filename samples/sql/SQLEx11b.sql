SELECT e.FirstName, e.LastName, c.CompanyName
FROM Orders o JOIN Customers c
     ON o.CustomerID = c.CustomerID
	 JOIN Employees e 
	 ON o.EmployeeID = e.EmployeeID
	 JOIN Shippers s
	 ON o.ShipVia = s.ShipperID
WHERE s.CompanyName = 'Speedy Express' AND c.City = 'Bruxelles'