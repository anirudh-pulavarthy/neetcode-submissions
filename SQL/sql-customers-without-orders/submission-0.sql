-- Write your query below
SELECT name
FROM Customers
WHERE id NOT IN (SELECT customer_id FROM orders)