SELECT stats_date AS date, 
customer_id, 
COUNT(*) AS nb_orders,
SUM(price+freight_value) AS money_spent
FROM e_commerce.orders
INNER JOIN 
e_commerce.items
ON e_commerce.items.order_id = e_commerce.orders.order_id 
WHERE DATE(order_purchase_timestamp) 