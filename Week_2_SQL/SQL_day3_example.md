# Week 2  SQL Day 3
## Wednesday 13/05/2020
### Practical Example

##### MORE will be added soon

``` SQL
--ARITHMETIC OPERATORS
-- % is modular is reminder. 12/4 = 0

-- 20 oranges were bought at £1 each . With a 20% Discount

--Gross total  = 1 * 20 =2
--Net Total = 1 * 20 * (1-0.2)
--Net Total = 1 * 20 * 0.8 = 16



SELECT * FROM [Order Details]



-- selects the top 2 order ID's
SELECT TOP 2 OrderID,
UnitPrice * Quantity * (1- Discount) AS "Net Total"
FROM [Order Details]
-- identifying the highest net total in the order details table
ORDER BY "Net Total" DESC

-- If you are using SUM, you will need to put the variables in SELECT and in GROUP BY as well

SELECT OrderID, UnitPrice, Quantity, Discount,
--COUNT(OrderID) AS "Total"
SUM(UnitPrice * Quantity) AS "Gross Total",
SUM(UnitPrice * Quantity * (1- Discount)) AS "Net Total"
FROM [Order Details]
GROUP BY OrderID, UnitPrice, Quantity, Discount
ORDER BY "Gross Total" DESC

SELECT * FROM Customers

SELECT postalcode "post code",
LEFT(postalcode, CHARINDEX(' ', postalcode)-1) AS "postal code region",
CHARINDEX(' ', postalcode) AS "space found", Country
FROM Customers
WHERE Country = 'UK'


-- We use like because we are using a wild card charcter
-- Below, we can see all the products with a space name

SELECT * FROM Products
SELECT p.ProductName
FROM Products p
WHERE ProductName LIKE '%''%'


-- charindex by itself is 0 because of apostrophe. So it will need to greater than 0
SELECT * FROM Products
SELECT p.ProductName
FROM Products p
WHERE CHARINDEX('''', p.ProductName)>0


SELECT DATEADD(d,5,orderdate) AS "due date"
DATEDIFF(d,orderdate,shippeddate) AS "ship days"
FROM orders

SELECT * FROM Employees

SELECT Firstname + ' ' + lastname AS "Name",
DATEDIFF(yy, Birthdate, GETDATE()) AS "AGE"
FROM Employees

SELECT Firstname + ' ' + lastname AS "Name",
DATEDIFF(yy, Birthdate, GETDATE())/365.25 AS "AGE"
FROM Employees

SELECT CASE
WHEN DATEDIFF(d,orderdate,shippeddate)<10,
THEN 'ON TIME'


-- see what we are dealing with
SELECT * FROM Products

-- calculates the total units in regards to the aggrevates in each order
SELECT
SUM(unitsonorder) AS "total on order",
AVG(unitsonorder) AS "AVG on order",
MIN(unitsonorder) AS "min on order",
MAX(unitsonorder) AS "MAX on order"
FROM Products

-- Similar but this time, it groups by supplier ID, which avoids duplicates on suppplier ID
SELECT SupplierID,
SUM(unitsonorder) AS "total on order",
AVG(unitsonorder) AS "AVG on order",
MAX(unitsonorder) AS "MAX on order"
FROM Products
GROUP BY SupplierID

-- GROUP BY to calculate the average recorder level for all prodicts by CategoryID
-- the SELECT clause must match the GROUP BY clause

SELECT TOP 1 CategoryID,
AVG(reorderlevel) AS "AVG on reorder level"
FROM Products
GROUP BY CategoryID
ORDER BY "AVG on reorder level" DESC
-- find the highest average reorder level?

SELECT SupplierID,
SUM(unitsonorder) AS "total on order",
AVG(unitsonorder) AS "AVG on order"
FROM Products
GROUP BY SupplierID
HAVING AVG(unitsonorder)>5


SELECT SupplierID, AVG(P.UnitsOnOrder) AS "Average units on order"
FROM Products p
GROUP BY SupplierID

SELECT SupplierID, s.CompanyName AS "Supplier Name"
AVG(P.UnitsOnOrder) AS "Average units on order"
FROM Products p INNER JOIN Suppliers s
ON p.SupplierID=s,SupplierID
GROUP BY SupplierID


SELECT productname, unitprice, companyname AS "Supplier",
categoryname AS "category"
FROM products p
INNER JOIN Suppliers ON p.SupplierID = s.SupplierID
INNER JOIN Categories ON p.CategoryID = p.CategoryID




SELECT * FROM Products
select * from suppliers

SELECT p.SupplierID,CompanyName AS "Supplier Name",
AVG(UnitsOnOrder) AS "average units on orders"
FROM Products p
inner join Suppliers s
on p.SupplierID=s.SupplierID
group by p.SupplierID, s.CompanyName
