CREATE VIEW product_sales(
    sku,
    order_no,
    qty,
    total_price,
    year,
    month,
    day_of_month,
    day_of_week,
    city
    )
AS
SELECT  cont.sku,
        order_no,
        qty,
        qty * price as total_price,
        EXTRACT(YEAR from date) as year,
        EXTRACT(MONTH from date) as month,
        EXTRACT(DAY from date) as day_of_month,
        TO_CHAR(date, 'DAY') as day_of_week,
        SUBSTRING(address FROM '\d{4}-\d{3}\s(.+)') AS city
FROM customer NATURAL JOIN "order" NATURAL JOIN pay NATURAL JOIN contains as cont JOIN product ON cont.sku = product.sku