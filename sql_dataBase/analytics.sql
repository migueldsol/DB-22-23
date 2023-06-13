--product_sales(sku, order_no, qty, total_price, year,
--month, day_of_month, day_of_week, city)

	--ex1 sem ROLLUP (acho que é o certo)
SELECT SUM(qty), SUM(total_price), sku, month, day_of_month, day_of_week, city
FROM product_sales
WHERE year = '2022'
GROUP BY GROUPING SETS ((sku), (sku, city), (sku, city, month, day_of_month, day_of_week))

	--ex2
SELECT AVG(sales_daily_price), month, day_of_week
FROM	(
				SELECT SUM(total_price) AS sales_daily_price, month, day_of_month, day_of_week
				FROM product_sales
				WHERE year = '2022'
				GROUP BY month, day_of_month, day_of_week
			) as FOO
GROUP BY ROLLUP(month, day_of_week);


