SELECT COUNT(*) AS total_customers FROM churn;

SELECT Churn, COUNT(*) AS count
FROM churn
GROUP BY Churn;

SELECT Contract, COUNT(*) AS count
FROM churn
GROUP BY Contract;

SELECT AVG(MonthlyCharges) AS avg_charges FROM churn;