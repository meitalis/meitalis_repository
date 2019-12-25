SELECT DISTINCT e.FirstName, e.LastName
FROM Employees e, Employees e2
WHERE e.BirthDate < e2.BirthDate AND e2.City = 'London'