SELECT Name AS Customers
FROM 
    (SELECT Name, CustomerId
     FROM Customers 
     LEFT JOIN Orders
     ON Customers.Id = Orders.CustomerId
    ) Temp
WHERE Temp.CustomerId IS NULL