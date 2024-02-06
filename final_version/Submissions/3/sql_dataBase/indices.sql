	--ex1
DROP INDEX price_and_sku_index_product;
CREATE INDEX price_and_sku_index_product ON product(sku, price);

CREATE INDEX date_hash_index_order ON "order" USING HASH(EXTRACT(YEAR FROM date));
DROP INDEX date_hash_index_order;

SELECT order_no
FROM "order"
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2023;

--O indice (sku, price) vai facilitar a procura do sku quando o indice é maior que 50 para dar join a contains e order fazendo apenas um index scan
--	Funciona melhor se houver poucos prices > 50
--O indice hash(EXTRACT(YEAR FROM date)) melhora imenso o hash join com contains usando um bitmap head scan -> bitmap index scan da data
--	Funciona melhor se houver poucas date com 2023

	--ex2
DROP INDEX name_index_product;
CREATE INDEX name_index_product ON product(name);

DROP INDEX order_no_index_contains;
CREATE INDEX order_no_index_contains ON contains(sku);

SELECT order_no, SUM(qty*price)
FROM contains
JOIN product USING (SKU)
WHERE name LIKE 'A%'
GROUP BY order_no;

--O indice (name) vai facilitar a procurar produtos que começem por A desde que não haja muitos com esta condição

--O indice (sku) vai facilitar o join entre o contains e o order_no visto apenas ter um composite index (order_no, sku)
--	este vai ajudar no join por já terá os contains ordenados por sku, facilitando o join com product