USE World_bank;

-- 1. The World Bank's international debt data
SELECT * from World_bank.international_debt limit 10;

-- 2. Finding the number of distinct countries
SELECT COUNT(DISTINCT(country_name)) as Total_Distinct_Countries from World_bank.international_debt; 

-- 3. Finding out the distinct debt indicators
SELECT DISTINCT(indicator_name) as Distinct_debt_indicator from World_bank.international_debt;

-- 4. Totaling the amount of debt owed by the countries
SELECT ROUND(SUM(debt)/1000000, 2) as Total_debt_in_USD FROM World_bank.international_debt;

-- 5. Country with the highest debt
SELECT country_name, SUM(debt) as Total_debt FROM World_bank.international_debt GROUP BY country_name ORDER BY Total_debt DESC LIMIT 1;

-- 6. Average amount of debt across indicators
SELECT indicator_code as Debt_Indicator, indicator_name, AVG(debt) as Average_debt 
FROM World_bank.international_debt 
GROUP BY Debt_Indicator, indicator_name 
ORDER BY Average_debt DESC 
LIMIT 10;

-- 7. The highest amount of principal repayments
SELECT country_name, indicator_name
FROM World_bank.international_debt
WHERE debt = (SELECT MAX(debt)
             FROM international_debt
             WHERE indicator_code = 'DT.AMT.DLXF.CD');
             
-- 8. The most common debt indicator
SELECT indicator_code, COUNT(indicator_code) as Indicator_count
FROM World_bank.international_debt
GROUP BY indicator_code
ORDER BY Indicator_count DESC, indicator_code DESC
LIMIT 20;