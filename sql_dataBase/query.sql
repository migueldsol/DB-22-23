--acho que nada funciona lol

    --ex 1 precisa ser alterado

SELECT cust_no, name FROM (SELECT cust_no, MAX(total_value) FROM (
    SELECT cust_no, SUM(qty * price)
        FROM (customer
            NATURAL JOIN "order"
            NATURAL JOIN pay
            NATURAL JOIN contains
            JOIN product p on contains.sku = p.sku
   )
    GROUP BY cust_no)
                NATURAL JOIN customer);


    --ex2
SELECT DISTINCT name
    FROM employee EF
    WHERE NOT EXISTS(
        SELECT date
        FROM "order"
        WHERE date BETWEEN '01/01/2022' AND '31/12/2022'
        EXCEPT
        SELECT date
        FROM ("order" O NATURAL JOIN employee e) PR
        WHERE PR.name = EF.name
                  AND date BETWEEN '01/01/2022' AND '31/12/2022'
    );

    --ex3 seems done
SELECT EXTRACT(MONTH FROM date),COUNT(*) FROM (
        (SELECT order_no, date
           FROM "order"
        )
        EXCEPT
        (SELECT order_no, date
           FROM pay NATURAL JOIN "order"
        )
    )
    GROUP BY EXTRACT(MONTH FROM date);
