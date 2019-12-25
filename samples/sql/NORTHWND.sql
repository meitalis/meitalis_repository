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


--** Ex 11 **
------------
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

--select e.FirstName,e.LastName,c.CompanyName
--from Orders o join Customers c
--	on o.CustomerID = c.CustomerID
--	join Employees e
--	on e.EmployeeID = o.EmployeeID
--	join Shippers s
--	on o.ShipVia = s.ShipperID
--where s.CompanyName='Speedy Express'
--and c.City = 'Bruxelles' 

--** Ex 12 **
------------
select * from Customers c


select distinct e.FirstName,e.LastName
from Employees e, Employees e2
where e.BirthDate < e2.BirthDate and e2.City = 'London'

--** Ex 14 **
------------
select ProductName
from Products p
except 
select p2.ProductName
from Orders o JOIN [Order Details] od ON
	o.OrderID = od.OrderID 
	JOIN Products p2 ON
	p2.ProductID = od.ProductID
where o.CustomerID = 'QUEEN'



--** Ex 15 **
------------
select c.CategoryName,avg(p1.UnitPrice) as avg_price
from Products p1, Categories c
where p1.CategoryID = c.CategoryID
group by c.CategoryName



select o.OrderID, od.UnitPrice,od.Discount
from Orders o , [Order Details] od
where o.OrderID = od.OrderID
and o.OrderID = 10250


select o.OrderID, sum(od.UnitPrice * (1-od.Discount)) as new_price
from Orders o , [Order Details] od
where o.OrderID = od.OrderID
group by o.OrderID
order by o.OrderID

select *
from Orders o
where year(o.OrderDate) = 1997 and month(o.OrderDate) = 7

select year(o.OrderDate) as year,month(o.OrderDate) as month, count(*)
from Orders o
group by year(o.OrderDate),month(o.OrderDate)

--** Ex 18 **
------------
select p.ProductID,p.ProductName, count (*)
from Products p
group by p.ProductID,p.ProductName

--sol1
select p2.ProductID, p2.ProductName
from Products p2
where p2.ProductID = 
	(select top 1 p.ProductID
	from [Order Details] od, Products p
	where od.ProductID = p.ProductID
	group by p.ProductID, p.ProductName
	order by count(*) desc)

--sol1.1
select p.ProductID, p.ProductName
from Products p JOIN [Order Details] od
	ON p.ProductID = od.ProductID
group by p.ProductID,p.ProductName
having sum(od.Quantity) >= all(select sum(od2.Quantity)
								from [Order Details] od2
								group by od2.ProductID)


--sol2
select distinct e.EmployeeID,e.FirstName,e.LastName
from Orders o,[Order Details] od,Employees e
where o.OrderID = od.OrderID
and e.EmployeeID = o.EmployeeID
and od.UnitPrice > all (select od1.UnitPrice
					from Orders o1,[Order Details] od1,Employees e1
					where o1.OrderID = od1.OrderID
					and e1.EmployeeID = o1.EmployeeID
					and e1.FirstName='Steven' and e1.LastName = 'Buchanan')

--** Ex 19 **
------------		

select distinct c.CustomerID,od.UnitPrice,p.ProductID,p.ProductName
from Customers c,Orders o,[Order Details] od, Products p
where c.CustomerID = o.CustomerID
and o.OrderID = od.OrderID
and od.ProductID = p.ProductID
and od.UnitPrice = (select max(od2.UnitPrice)
			from Customers c2,Orders o2,[Order Details] od2, Products p2
			where c2.CustomerID = o2.CustomerID
			and o2.OrderID = od2.OrderID
			and od2.ProductID = p2.ProductID
			and c2.CustomerID = c.CustomerID)
order by c.CustomerID


select e2.EmployeeID ,o2.OrderID,o2.OrderDate
from Employees e2,Orders o2
where e2.EmployeeID = o2.EmployeeID
and o2.OrderDate = (select max(o.OrderDate)
				from Employees e,Orders o
				where e.EmployeeID = o.EmployeeID
				and e.EmployeeID = e2.EmployeeID)
				



--** Ex 20 **
------------	
select p.ProductID
from Products p
where p.UnitPrice < 5 

select od.OrderID
from [Order Details] od
where exists (select p.ProductID
						  from Products p
						  where p.UnitPrice < 5 )

select o.CustomerID
from Orders o
where o.OrderID in (select od.OrderID
from [Order Details] od
where od.ProductID in (select p.ProductID
						  from Products p
						  where p.UnitPrice < 5))
group by o.CustomerID

select c.CustomerID,p.UnitPrice
from Customers c,Products p,[Order Details] od,Orders o 
where c.CustomerID = o.CustomerID
and p.ProductID = od.ProductID
and od.OrderID = o.OrderID
order by c.CustomerID,p.UnitPrice


