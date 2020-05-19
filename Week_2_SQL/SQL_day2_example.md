# Week 2  SQL Day 2
## Tuesday 12/05/2020
### Practical Example

``` SQL

-- ALWAYS CHECK THE TABLE BEFORE WRITE THE QUERY
SELECT * FROM table_name

-- The asterisk means to select alll columns
SELECT * FROM Customers

-- WHERE is used to filter the data
SELECT * FROM Customers
WHERE City= 'Paris';

-- how many employees have home city of 'london'?
SELECT * FROM Employees
WHERE City = 'London';

-- which employee is a doctor?
SELECT * FROM Employees
WHERE TitleOfCourtesy = 'Dr.';

--checking the product table for reference
SELECT * FROM Products

-- using aggreviation such as COUNT, avg, sum, min , max. Clears the column name
-- so you will need to use AS to add a column name

-- ALWAYS CHECK THE TABLES FOR INFORMATION

-- how many products are discontinued?
-- you can give the name to a column using the AS function
-- the 1 is used becuase of BIT. Either 0 or 1. In this case 1
SELECT COUNT(Discontinued) AS "Products Discontinued" FROM Products WHERE Discontinued = '1'

-- use primary keys for counting rows
-- counting the number of employer ID
SELECT COUNT(EmployeeID) AS "Number Of Employees" FROM Employees

-- we can limit the amount of columns by naming them instead of using *
-- we can limit the amount of rows by using where
SELECT companyname, city, country, Region
FROM Customers
WHERE region ='BC'

-- have a look, how many rows are returned when you run this query
SELECT customerid, city FROM Customers
WHERE Country = 'France'

-- Selects the top 100 from  very large tables and doesn't affect performance issues
SELECT TOP 100 Companyname, city FROM Customers
WHERE Country = 'France'

-- AND + OR only works with WHERE
--AND operator displays a record if all the conditions separated by AND are TRUE
SELECT productname, unitprice FROM Products
WHERE CategoryID = 1 AND Discontinued ='0'

-- how many rows does using AND bring back?
--AND is both conditions
SELECT productname, unitprice FROM Products
WHERE UnitsInStock > 0 AND UnitPrice > 29.99

-- how many rows does using OR bring back?
--OR is both conditions
SELECT productname, unitprice FROM Products
WHERE UnitsInStock > 0 OR UnitPrice > 29.99

-- use DISTINCT if you want to remove duplicates from your data
SELECT DISTINCT country FROM Customers
WHERE ContactTitle = 'owner'


SELECT DISTINCT country FROM Customers
WHERE ContactTitle = 'owner' AND country LIKE '_e%'

--using the LIKE operator
-- underscore substitutes 1 charchter.
-- Percentage sign means any number of characters can be used
-- '__i%' = 2 underscore, i, % = this means anything with the 3rd letter
--  'i' and anything else after
-- [charlist] =
-- '[msd]%' = all the items starting with M, S, D
-- [^msd]%' = all items not starting with M, S, D
-- The above are called wildcard characters

--brings back any products starting with ch
SELECT Productname
FROM Products WHERE ProductName LIKE 'Ch%'


-- select regions that end in A and has just 2 characters
SELECT *
FROM Customers
WHERE Region LIKE '_A'

-- shows two specific named region of 'wa' and 'sp'
-- ALWAYS CHECK THE TABLE if you are confused
SELECT * FROM Customers
WHERE Region IN ('wa','sp')

-- use BETWEEN to find a range of two numbers
SELECT * FROM EmployeeTerritories
WHERE TerritoryID BETWEEN 06800 AND 09999

-- whata are the names and product IDs of the
-- products with a unit price below 5.00?
SELECT productname, productid
FROM Products
WHERE unitprice <5.00

-- which categories have a category name with initals
-- beginning with B or S?
SELECT * FROM Categories
WHERE CategoryName LIKE '[bs]%'

-- how many orders are there for EmployeeIDs 5 & 7 together?
SELECT COUNT(employeeid) AS "number of orders"
FROM Orders
WHERE EmployeeID IN (5,7)

-- how many orders are there for EmployeeIDs 5 & 7 seperately?
SELECT EmployeeID, COUNT(*) AS "number of orders"
FROM Orders
GROUP BY EmployeeID
HAVING EmployeeID IN (5,7)

-- CONCATENATION is using +
-- to add a space or comma in apostrophe

-- in this example, we concatenate the comma between city and country
SELECT c.CompanyName AS 'Company name', City + ',' + Country AS 'City'
FROM Customers c

-- write a SELECT using the employees table and concatenate First name
-- and last name togther. Use a column alias to rename the column to
-- Employee Name
SELECT c.FirstName + ' ' + c.LastName AS "Employee Name"
FROM Employees c

-- filtering based on data where region is NULL
SELECT Region, c.CompanyName AS 'Company name', City + ', ' + Country AS 'City'
FROM Customers c
WHERE Region IS NULL

-- filtering based on data where region IS NOT NULL
SELECT Region, c.CompanyName AS 'Company name', City + ', ' + Country AS 'City'
FROM Customers c
WHERE Region IS NOT NULL

-- write a SELECT statement to list the six countires that have
-- region codes in the Customers Table?
-- statement that lists 6 countries in regions from customer table
-- DISTINCT was used to avid duplicates.
SELECT DISTINCT c.Country
FROM Customers c
WHERE Region IS NOT NULL
