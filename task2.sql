SELECT 
	customer_id, 
	value_date,
	amount,
	COALESCE(amount + LAG(amount) OVER(PARTITION BY date_trunc('month', value_date), customer_id), amount) AS cumulative_sum,
	SUM(amount) over(partition by customer_id) AS total_amount
FROM transaction
ORDER BY  customer_id, value_date, amount
