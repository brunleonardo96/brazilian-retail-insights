-- PROGETTO: Analisi della Retention per Coorti - Olist Retail
-- OBIETTIVO: Misurare la fedeltà dei clienti calcolando quanti mesi restano attivi dopo il primo acquisto.


WITH first_purchase AS (
    SELECT
        c.customer_unique_id,
        MIN(DATE_TRUNC(DATE(o.order_purchase_timestamp), MONTH)) AS cohort_month
    FROM
        `brazilian-ecommerce-483110.Olist_dataset.olist_orders_dataset` o
    JOIN
        `brazilian-ecommerce-483110.Olist_dataset.olist_customers_dataset` c
        ON o.customer_id = c.customer_id
    WHERE
        o.order_status = 'delivered' -- Solo ordini completati
    GROUP BY
        1
),

activity AS (
    -- Prendo tutti i mesi in cui i clienti hanno effettuato ordini
    SELECT
        c.customer_unique_id,
        DATE_TRUNC(DATE(o.order_purchase_timestamp), MONTH) AS order_month
    FROM
        `brazilian-ecommerce-483110.Olist_dataset.olist_orders_dataset` o
    JOIN
        `brazilian-ecommerce-483110.Olist_dataset.olist_customers_dataset` c
        ON o.customer_id = c.customer_id
    WHERE
        o.order_status = 'delivered'
    GROUP BY
        1, 2
),

cohort_retention AS (
    -- Calcolo delta primo acquisto - data acquisto attuale
    SELECT
        f.cohort_month,
        a.order_month,
        DATE_DIFF(a.order_month, f.cohort_month, MONTH) AS month_number,
        COUNT(DISTINCT f.customer_unique_id) AS active_customers
    FROM
        first_purchase f
    JOIN
        activity a ON f.customer_unique_id = a.customer_unique_id
    GROUP BY
        1, 2, 3
)


SELECT
    cohort_month,
    month_number,
    active_customers,
    -- %retention
    SAFE_DIVIDE(active_customers, FIRST_VALUE(active_customers) OVER (PARTITION BY cohort_month ORDER BY month_number)) * 100 AS retention_rate
FROM
    cohort_retention
WHERE
    month_number <= 12
ORDER BY
    cohort_month, month_number;