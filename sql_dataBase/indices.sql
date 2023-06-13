CREATE INDEX price_index ON product(price);

DROP INDEX price_index;

SELECT order_no
FROM "order"
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2022;