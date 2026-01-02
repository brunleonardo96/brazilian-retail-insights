-- PROGETTO: Analisi dei Metodi di Pagamento
-- OBIETTIVO: Capire l'impatto dei metodi di pagamento sul valore degli ordini

SELECT 
    payment_type,
    COUNT(order_id) AS total_transactions,
    ROUND(SUM(payment_value), 2) AS total_revenue,
    ROUND(AVG(payment_value), 2) AS avg_ticket,
    -- Quante rate vengono usate in media per metodo
    ROUND(AVG(payment_installments), 1) AS avg_installments
FROM 
    `brazilian-ecommerce-483110.Olist_dataset.olist_order_payments_dataset`
GROUP BY 
    1
ORDER BY 
    total_revenue DESC;
