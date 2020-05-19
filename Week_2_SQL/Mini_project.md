# Mini Project

## Friday 15/05/2020
### Practical Example

``` SQL
-- ############## 1.1
/*Write a query that lists all Customers in either Paris or London.
Include Customer ID, Company Name and all address fields.*/

-- the whole adress
SELECT * FROM CUSTOMERS
WHERE city = 'Paris' OR city ='London'

-- with just address
SELECT CustomerID, CompanyName, Address
FROM CUSTOMERS
WHERE city = 'Paris' OR city ='London'

-- ############## 1.2
-- List all products stored in bottles.


SELECT * FROM PRODUCTS -- checking to see how the table looks

--List all products stored in bottles.
SELECT QuantityPerUnit, productName
FROM PRODUCTS
WHERE QuantityPerUnit LIKE '%bottle%'

-- ############## 1.3
-- list all products stored in bottles with supplier name and country

SELECT * FROM Suppliers -- checking to see how the table looks


SELECT  p.c CompanyName, Country, QuantityPerUnit, productName --select all the columns you want
FROM PRODUCTS p --from which table, left join
INNER JOIN Suppliers s -- whats the other table, right join
ON p.SupplierID = s.SupplierID -- whats connecting connecting tables together, primary and foreign key
WHERE QuantityPerUnit -- what are you limits
LIKE '%bottle%' -- back to the question

-- ############## 1.4
/*Write an SQL Statement that shows how many products there are in each category.
Include Category Name in result set and list the highest number first.*/

SELECT * FROM CATEGORIES

SELECT count(CategoryName) AS "Number of products in each category" --this is sum
FROM Categories

-- ############## 1.5

/*List all UK employees using concatenation to join their title of courtesy,
first name and last name together. Also include their city of residence.*/

SELECT TitleOfCourtesy + ' ' + FirstName + ' ' + LastName AS "Employee Name", City
FROM Employees
WHERE Country = 'UK'

-- ############## 1.6

/*List Sales Totals for all Sales Regions (via the Territories table using 4 joins)
with a Sales Total greater than 1,000,000. Use rounding or FORMAT to present the numbers.*/

SELECT r.RegionID, FORMAT(SUM(od.UnitPrice * (1-od.Discount) * od.Quantity), 'C') "Total Discounted Price"
FROM [Order Details] od
INNER JOIN Orders o  ON o.OrderID = od.OrderID
INNER JOIN EmployeeTerritories e ON o.EmployeeID = e.EmployeeID
INNER JOIN Territories t  ON e.TerritoryID = t.TerritoryID
INNER JOIN Region r ON  t.RegionID = r.RegionID
GROUP BY r.RegionID
HAVING  (SUM(od.UnitPrice * (1-od.Discount) * od.Quantity)) > 1000000


-- ############## 1.7
/*Count how many Orders have a Freight amount greater than 100.00
and either USA or UK as Ship Country */


SELECT COUNT(OrderID) AS "Total Freight"
FROM Orders o
WHERE Freight > 100.00 AND (ShipCountry = 'UK' OR ShipCountry = 'USA')

-- ############## 1.8
/* Write an SQL Statement to identify the Order Number of the Order
with the highest amount of discount applied to that order. */

SELECT TOP 1 OrderID, (Quantity * UnitPrice * Discount) AS "Highest Amount Of Discounts"
FROM [Order Details]
ORDER BY "Highest Amount of Discounts" DESC


-- ############## 2.1
/* Write the correct SQL statement to create the following table:
Spartans Table – include details about all the Spartans on this course.
Separate Title, First Name and Last Name into separate columns,
and include University attended, course taken and mark achieved. */

CREATE TABLE spartans_table
(
    -- spartanid INT IDENTITY(1,1),
    title CHAR(2),
    firstname VARCHAR(20),
    lastname VARCHAR(20),
    university_attended VARCHAR(30),
    course_taken VARCHAR(30),
    mark_achieved INT


)

-- ############## 2.2
/*Write SQL statements to add the details of the Spartans in
your course to the table you have created.*/

INSERT INTO spartans_table
VALUES
(
    'ms', 'kate', 'winslett', 'university of sheffield', 'business', 88
),

(
    'mr', 'mike', 'lolson', 'university of nottingam', 'maths', 40
);

-- TO THE VALUE OF n

SP_HELP spartans_table -- Checking informattion after creating the table
SELECT * FROM spartans_table -- checking info after inserting the values

DROP TABLE spartans_table -- to drop the table afterwards



-- ############## 3.1
-- List all Employees from the Employees table and who they report to

SELECT * FROM EMPLOYEES -- checking to see how the table looks

SELECT Firstname, Lastname, Reportsto
FROM EMPLOYEES

-- ############## 3.2
/*List all Suppliers with total sales over $10,000 in the Order Details table.
Include the Company Name from the Suppliers Table and present as a bar chart as below */

SELECT * FROM Orders
SELECT * FROM [ORDER details]

-- ############## 3.3
-- List the Top 10 Customers YTD for the latest year in the Orders file. Based on total value of orders shipped.

SELECT TOP 10 o.CustomerID, -- top 10 customers
SUM(od.UnitPrice * Quantity) AS "Gross Total"
FROM [Order Details] od
INNER JOIN Orders o
ON od.OrderID=o.OrderID
INNER JOIN Customers c
ON o.CustomerID=c.CustomerID
GROUP BY o.CustomerID, o.ShippedDate
HAVING YEAR(o.ShippedDate) = '1998'
-- identifying the highest net total in the order details table
ORDER BY "Gross Total" DESC

-- ############## 3.4
--Plot the Average Ship Time by month for all data in the Orders Table

SELECT DISTINCT MONTH(OrderDate) as "Shipped Month", AVG(DATEDIFF(d, OrderDate, ShippedDate)) AS "Average Ship Time"
FROM Orders Date
GROUP BY MONTH(OrderDate)
ORDER BY MONTH(OrderDate)




--SELECT DISTINCT MONTH(Order_Date) AVG(ShippedDate - RequiredDate(DATE))
--FROM Orders

-- use Northwind
--SELECT * FROM Orders
--SELECT * FROM Shippers
--SELECT * FROM Suppliers
--SELECT * FROM [ORDER details]
