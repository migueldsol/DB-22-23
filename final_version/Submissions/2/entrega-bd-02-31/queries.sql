---exercicio 1
SELECT DISTINCT c.name
FROM customer c
         JOIN order_ o ON c.cust_no = o.placed_by_cust_no
         JOIN contains ct ON o.order_no = ct.order_no
         JOIN product p ON ct.sku = p.sku
WHERE p.price > 50 AND date BETWEEN '2023-01-01' AND '2023-12-31';

---exercicio 2
(
    SELECT DISTINCT e.name
    FROM employee e
             JOIN works w ON e.ssn = w.ssn
             JOIN workplace ON w.address = workplace.address
             JOIN warehouse ON workplace.address = warehouse.address
    EXCEPT
    SELECT DISTINCT e.name
    FROM employee e
             JOIN works w ON e.ssn = w.ssn
             JOIN workplace ON w.address = workplace.address
             JOIN office ON workplace.address = office.address
)
INTERSECT
SELECT DISTINCT e.name
FROM employee e
         JOIN process ON e.ssn = process.ssn
         JOIN order_ ON process.order_no = order_.order_no
WHERE date BETWEEN '2023-01-01' AND '2023-01-31';

---exercicio 3
SELECT product.name FROM
    (
        SELECT product.sku, SUM(qty)
        FROM sale JOIN contains ON sale.order_no = contains.order_no JOIN product ON contains.sku = product.sku
        GROUP BY product.sku
        HAVING SUM(qty) >= ALL
               (
                   SELECT SUM(qty)
                   FROM sale JOIN contains ON sale.order_no = contains.order_no JOIN product ON contains.sku = product.sku
                   GROUP BY product.sku
               )
    ) AS big JOIN product ON product.sku = big.sku;

--exercicio 4
SELECT o.order_no, SUM(p.price * c.qty) AS total_value
FROM sale s
         JOIN order_ o ON s.order_no = o.order_no
         JOIN contains c ON o.order_no = c.order_no
         JOIN product p ON c.sku = p.sku
GROUP BY o.order_no;

--