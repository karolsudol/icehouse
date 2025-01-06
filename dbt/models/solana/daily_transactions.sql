{{ config(materialized='table') }}

SELECT 
    date_trunc('day', block_time) as date,
    count(*) as tx_count,
    sum(fee) as total_fees,
    count(distinct signer) as unique_signers
FROM {{ source('solana', 'transactions') }}
WHERE block_time >= current_date - interval '1' day
GROUP BY 1
ORDER BY 1 DESC 