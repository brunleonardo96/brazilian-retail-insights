-- PROGETTO: Geospatial Spending Analysis
-- OBIETTIVO: Identificare le regioni con il maggior valore economico (GMV)


SELECT 
    c.customer_state,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(SUM(i.price), 2) AS total_revenue,
    ROUND(AVG(i.price), 2) AS avg_order_value,
    -- % di ogni stato su tot
    ROUND(SUM(i.price) / SUM(SUM(i.price)) OVER() * 100, 2) AS pct_revenue
FROM 
    `brazilian-ecommerce-483110.Olist_dataset.olist_orders_dataset` o
JOIN 
    `brazilian-ecommerce-483110.Olist_dataset.olist_customers_dataset` c ON o.customer_id = c.customer_id
JOIN 
    `brazilian-ecommerce-483110.Olist_dataset.olist_order_items_dataset` i ON o.order_id = i.order_id
WHERE 
    o.order_status = 'delivered'
GROUP BY 
    1
ORDER BY 
    total_revenue DESC;
