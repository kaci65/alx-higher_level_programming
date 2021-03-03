-- lists the number of records with the same score (table =  second_table, database hbtn_0c_0)
SELECT score, count(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
