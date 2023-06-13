	--ex1
DROP INDEX price_index_product;
CREATE INDEX price_index_product ON product(price);
DROP INDEX date_index_product;
CREATE INDEX date_index_product ON order(date);

SELECT order_no
FROM "order"
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2023;

	--ex2
DROP INDEX name_index_product;
CREATE INDEX name_index_product ON product(name);

SELECT order_no, SUM(qty*price)
FROM contains
JOIN product USING (SKU)
WHERE name LIKE 'A%'
GROUP BY order_no;
