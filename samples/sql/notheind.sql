--select Customers.CustomerID,
--		(Customers.Address + ' ' + Customers.City) as FullAddress
--from Customers

--select Products.ProductName,Products.UnitPrice,
--		(Products.UnitPrice - (Products.UnitPrice * 0.165)) as "Unit Price After Discount",
--		(Products.UnitsInStock - Products.UnitsOnOrder) as Diff
--from Products


--select distinct title from Employees

--select * from Employees
--order by HireDate

--select  * from Customers
--order by substring(Customers.CompanyName,2,1)

--select top 3 * from Products
--order by UnitsInStock asc

--select * from Products
--select * from Categories
--select productname, unitprice, categoryname
--from Products,Categories

--select productname, unitprice, categoryname
--from Products join Categories
--on Products.CategoryID = Categories.CategoryID

--select p.productname, p.unitprice, c.CategoryName
--from Products p join Categories c
--on p.CategoryID = c.CategoryID

--select p.productname, p.unitprice, c.CategoryName
--from Products as p inner join Categories as c
--on p.CategoryID = c.CategoryID



--select distinct  e.FirstName, e.LastName,e.Address,e.City,e.Region
--from Employees as e ,Orders as o
--where e.EmployeeID = o.EmployeeID
--and o.ShipCountry='Belgium'
--order by e.FirstName

--select distinct e.FirstName, e.LastName,e.Address,e.City,e.Region
--from Employees as e inner join Orders as o
--	on e.EmployeeID = o.EmployeeID
--where o.ShipCountry='Belgium'
--order by e.FirstName

select distinct e.FirstName, e.LastName,e.Address,e.City,e.Region
from Employees as e ,Orders as o
where Employees.EmployeeID *= Orders.EmployeeID

--select e.FirstName,e.LastName,c.CompanyName
--from Orders o join Customers c
--	on o.CustomerID = c.CustomerID
--	join Employees e
--	on e.EmployeeID = o.EmployeeID
--	join Shippers s
--	on o.ShipVia = s.ShipperID
--where s.CompanyName='Speedy Express'
--and c.City = 'Bruxelles' 