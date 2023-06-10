--acho que nada funciona lol

    --ex 1 precisa ser alterado
SELECT name, cust_no
FROM(
    (SELECT cust_no, SUM(qty * price)
     FROM (customer
           NATURAL JOIN "order"
           NATURAL JOIN pay
           NATURAL JOIN contains
           JOIN product p ON contains.sku = p.sku)
     GROUP BY cust_no
     HAVING SUM(qty * price) >= ALL
          (SELECT SUM(qty * price) as total_value
           FROM (customer
               NATURAL JOIN "order"
               NATURAL JOIN pay
               NATURAL JOIN contains
               JOIN product p ON contains.sku = p.sku) as custOrders
           GROUP BY custOrders.cust_no)
     ) AS maxSalesPerCust NATURAL JOIN customer);

    --ex2
SELECT DISTINCT name
    FROM employee EF
    WHERE NOT EXISTS(
        SELECT date
        FROM "order"
        WHERE date BETWEEN '01/01/2022' AND '31/12/2022'
        EXCEPT
        SELECT date
        FROM (employee e NATURAL JOIN process NATURAL JOIN "order") PR
        WHERE PR.name = EF.name
                  AND date BETWEEN '01/01/2022' AND '31/12/2022'
    );

    --ex3 seems done
SELECT EXTRACT(MONTH FROM date) as month,COUNT(*) FROM (
        (SELECT order_no, date
           FROM "order"
        )
        EXCEPT
        (SELECT order_no, date
           FROM pay NATURAL JOIN "order"
        )
    ) AS paidOrders
    GROUP BY month;
