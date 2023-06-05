CREATE VIEW product_sales(
    sku,
    order_no,
    qty,
    total_price,
    year, month,
    day_of_month,
    day_of_week,
    city
    )
AS
SELECT  sku,
        order_no,
        qty * price as total_price,
        EXTRACT(YEAR from date),
        EXTRACT(MONTH from date),
        TO_CHAR(date, 'DAY') as day_of_week,
        SUBSTRING(your_address_column FROM '\d{4}-\d{3}\s(.+)') AS city
FROM pay NATURAL JOIN "order" NATURAL JOIN product NATURAL JOIN contains