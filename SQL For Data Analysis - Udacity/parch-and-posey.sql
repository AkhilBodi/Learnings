-- show global variables like 'local_infile';
-- set global local_infile=true;
-- LOAD DATA LOCAL INFILE
-- 'Documents/Data Science/Courses/Udacity/SQL/web_events.csv'
-- INTO TABLE parch_posey.web_events
-- FIELDS TERMINATED BY ','
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 LINES;
-- select * from parch_posey.web_events;
-- SET @@local.net_read_timeout=360;

USE parch_posey;
SELECT id, account_id, occurred_at
FROM orders;

SELECT * FROM web_events
LIMIT 10;

SELECT occurred_at, account_id, channel
FROM web_events
LIMIT 10;

SELECT *
FROM orders
ORDER BY occurred_at 
LIMIT 10;

SELECT id, occurred_at, total_amt_usd
FROM orders 
LIMIT 10;

SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY total_amt_usd DESC
LIMIT 5;

SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY total_amt_usd
LIMIT 20;

-- Write a query that displays the order ID, account ID, and total dollar amount for all the orders, 
-- sorted first by the account ID (in ascending order), and then by the total dollar amount (in descending order). 
SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY account_id, total_amt_usd DESC;

-- Now write a query that again displays order ID, account ID, and total dollar amount for each order,
-- but this time sorted first by total dollar amount (in descending order), and then by account ID (in ascending order). 
SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY  total_amt_usd DESC,account_id;

-- Pulls the first 5 rows and all columns from the orders table that have a dollar amount of gloss_amt_usd greater than or equal to 1000.
SELECT *
FROM orders
WHERE gloss_amt_usd >=1000
LIMIT 5;

-- Pulls the first 10 rows and all columns from the orders table that have a total_amt_usd less than 500.
SELECT *
FROM orders
WHERE gloss_amt_usd <500
LIMIT 10;

-- Filter the accounts table to include the company name, website, and the primary point of contact (primary_poc) just for the Exxon Mobil company in the accounts table. 

SELECT name, website, primary_poc
FROM accounts
WHERE name = 'Exxon Mobil';

-- Create a column that divides the standard_amt_usd by the standard_qty to find the unit price for standard paper for each order.
-- Limit the results to the first 10 orders, and include the id and account_id fields. 
SELECT id, account_id, (standard_amt_usd/standard_qty) AS unit_price_per_paper
FROM orders
LIMIT 10;

-- Write a query that finds the percentage of revenue that comes from poster paper for each order. You will need to use only the columns that end with _usd. 
-- (Try to do this without using the total column.) Display the id and account_id fields also
SELECT id, account_id, poster_amt_usd/(standard_amt_usd + gloss_amt_usd + poster_amt_usd) AS revenue_per_poster
FROM orders;

DESC orders;

-- All the companies whose names start with 'C'
SELECT name FROM accounts
WHERE name LIKE 'C%';

-- All companies whose names contain the string 'one' somewhere in the name
SELECT name FROM accounts
WHERE name LIKE 'one%';

-- All companies whose names end with 's'
SELECT name FROM accounts
WHERE name LIKE '%s';

-- Use the accounts table to find the account name, primary_poc, and sales_rep_id for Walmart, Target, and Nordstrom.
SELECT name, primary_poc, sales_rep_id FROM accounts
WHERE name IN ('Walmart','Target','Nordstrom');

-- Use the web_events table to find all information regarding individuals who were contacted via the channel of organic or adwords.
SELECT * FROM web_events
WHERE channel IN('organic','adwords');

-- Use the accounts table to find the account name, primary poc, and sales rep id for all stores except Walmart, Target, and Nordstrom.
SELECT name,primary_poc,sales_rep_id FROM accounts
WHERE name NOT IN ('Walmart','Target','Nordstrom');

-- Use the web_events table to find all information regarding individuals who were contacted via any method except using organic or adwords methods.
SELECT * FROM web_events
WHERE channel NOT IN('organic','adwords');

-- Use the accounts table to find:
--    All the companies whose names do not start with 'C'.
SELECT name FROM accounts
WHERE name NOT LIKE 'C%';
--    All companies whose names do not contain the string 'one' somewhere in the name.
SELECT name FROM accounts
WHERE name NOT LIKE 'one%';
--    All companies whose names do not end with 's'.
SELECT name FROM accounts
WHERE name NOT LIKE '%s';

-- Write a query that returns all the orders where the standard_qty is over 1000, the poster_qty is 0, and the gloss_qty is 0.
SELECT * FROM orders
WHERE standard_qty > 1000 AND poster_qty = 0 AND gloss_qty = 0;

-- Using the accounts table, find all the companies whose names do not start with 'C' and end with 's'.
SELECT name FROM accounts
WHERE name NOT LIKE 'C%' AND name NOT LIKE '%s';

-- Write a query that displays the order date and gloss_qty data for all orders where gloss_qty is between 24 and 29.
SELECT occurred_at, gloss_qty FROM orders
WHERE gloss_qty BETWEEN 24 AND 29;

-- Use the web_events table to find all information regarding individuals who were contacted via the organic or adwords channels,
-- and started their account at any point in 2016, sorted from newest to oldest.
SELECT * FROM web_events
WHERE channel IN('organic','adwords') AND occurred_at LIKE '%2016%'
ORDER BY occurred_at DESC;

-- Find list of orders ids where either gloss_qty or poster_qty is greater than 4000. Only include the id field in the resulting table.
SELECT id FROM orders
WHERE gloss_qty > 4000 OR poster_qty > 4000;

-- Write a query that returns a list of orders where the standard_qty is zero and either the gloss_qty or poster_qty is over 1000.
SELECT * FROM orders
WHERE standard_qty = 0 AND (gloss_qty > 1000 OR poster_qty > 1000);

-- Find all the company names that start with a 'C' or 'W', and the primary contact contains 'ana' or 'Ana', but it doesn't contain 'eana'.
SELECT * FROM accounts
WHERE (name LIKE 'C%' OR name LIKE '%W') AND ((primary_poc LIKE '%ana%' OR '%Ana%') AND (primary_poc NOT LIKE '%eana%'));

-- Statement		How to Use It					Other Details
-- SELECT			SELECT Col1, Col2, ...			Provide the columns you want
-- FROM	     		FROM Table						Provide the table where the columns exist
-- LIMIT			LIMIT 10						Limits based number of rows returned
-- ORDER BY			ORDER BY Col					Orders table based on the column. Used with DESC.
-- WHERE			WHERE Col > 5					A conditional statement to filter your results
-- LIKE				WHERE Col LIKE '%me%'			Only pulls rows where column has 'me' within the text
-- IN				WHERE Col IN ('Y', 'N')			A filter for only rows with column of 'Y' or 'N'
-- NOT				WHERE Col NOT IN ('Y', 'N')		NOT is frequently used with LIKE and IN
-- AND				WHERE Col1 > 5 AND Col2 < 3		Filter rows where two or more conditions must be true
-- OR				WHERE Col1 > 5 OR Col2 < 3		Filter rows where at least one condition must be true
-- BETWEEN			WHERE Col BETWEEN 3 AND 5		Often easier syntax than using an AND

SELECT * FROM accounts
JOIN orders
ON orders.id = accounts.id;

-- Provide a table for all web_events associated with account name of Walmart. There should be three columns.
-- Be sure to include the primary_poc, time of the event, and the channel for each event. 
-- Additionally, you might choose to add a fourth column to assure only Walmart events were chosen. 

SELECT accounts.primary_poc, web_events.occurred_at, web_events.channel, accounts.name
FROM web_events
JOIN accounts
ON accounts.id = web_events.account_id
WHERE accounts.name = 'Walmart';

-- Provide a table that provides the region for each sales_rep along with their associated accounts. 
-- Your final table should include three columns: the region name, the sales rep name, and the account name. 
-- Sort the accounts alphabetically (A-Z) according to account name.
SELECT region.name region_name, sales_reps.name sales_rep_name, accounts.name account_name 
FROM region
JOIN sales_reps
ON sales_reps.region_id = region.id
JOIN accounts
ON accounts.sales_rep_id = sales_reps.id
ORDER BY account_name;

-- Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order.
-- Your final table should have 3 columns: region name, account name, and unit price.
-- A few accounts have 0 for total, so I divided by (total + 0.01) to assure not dividing by zero.
SELECT region.name region_name, accounts.name account_name, (orders.total_amt_usd/orders.total+0.01) unit_price
FROM region
JOIN sales_reps
ON sales_reps.region_id = region.id
JOIN accounts
ON accounts.sales_rep_id = sales_reps.id
JOIN orders 
ON orders.account_id = accounts.id;

-- Provide a table that provides the region for each sales_rep along with their associated accounts. This time only for the Midwest region. 
-- Your final table should include three columns: the region name, the sales rep name, and the account name. 
-- Sort the accounts alphabetically (A-Z) according to account name.

SELECT r.name region_name, s.name sales_rep_name, a.name account_name
FROM region r
JOIN sales_reps s
ON s.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = s.id
WHERE r.name LIKE '%Midwest%'
ORDER BY account_name;

-- Provide a table that provides the region for each sales_rep along with their associated accounts. 
-- This time only for accounts where the sales rep has a first name starting with S and in the Midwest region. 
-- Your final table should include three columns: the region name, the sales rep name, and the account name. 
-- Sort the accounts alphabetically (A-Z) according to account name. 
SELECT r.name region_name, s.name sales_rep_name, a.name account_name
FROM region r
JOIN sales_reps s
ON s.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = s.id
WHERE s.name LIKE 'S%' AND r.name LIKE '%Midwest%'
ORDER BY account_name;

-- Provide a table that provides the region for each sales_rep along with their associated accounts.
-- This time only for accounts where the sales rep has a last name starting with K and in the Midwest region.
-- Your final table should include three columns: the region name, the sales rep name, and the account name.
-- Sort the accounts alphabetically (A-Z) according to account name.
SELECT r.name region_name, s.name sales_rep_name, a.name account_name
FROM region r
JOIN sales_reps s
ON s.region_id = r.id
JOIN accounts a 
ON a.sales_rep_id = s.id
WHERE s.name LIKE '% K%' AND r.name LIKE '%Midwest%'
ORDER BY account_name;

-- Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order.
-- However, you should only provide the results if the standard order quantity exceeds 100.
-- Your final table should have 3 columns: region name, account name, and unit price. 
-- In order to avoid a division by zero error, adding .01 to the denominator here is helpful total_amt_usd/(total+0.01). 
SELECT r.name region_name, a.name account_name, (o.total_amt_usd/o.total+0.01) unit_price
FROM region r 
JOIN sales_reps s
ON s.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN orders o
ON o.account_id = a.id
WHERE o.standard_qty > 100;

-- Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order.
-- However, you should only provide the results if the standard order quantity exceeds 100 and the poster order quantity exceeds 50. 
-- Your final table should have 3 columns: region name, account name, and unit price.
-- Sort for the smallest unit price first. In order to avoid a division by zero error, adding .01 to the denominator here is helpful (total_amt_usd/(total+0.01).
SELECT r.name region_name, a.name account_name, (o.total_amt_usd/o.total+0.01) unit_price
FROM region r 
JOIN sales_reps s
ON s.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN orders o
ON o.account_id = a.id
WHERE o.standard_qty > 100 AND o.poster_qty > 50
ORDER BY unit_price;

-- Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order.
-- However, you should only provide the results if the standard order quantity exceeds 100 and the poster order quantity exceeds 50.
-- Your final table should have 3 columns: region name, account name, and unit price. Sort for the largest unit price first.
-- In order to avoid a division by zero error, adding .01 to the denominator here is helpful (total_amt_usd/(total+0.01). 
SELECT r.name region_name, a.name account_name, (o.total_amt_usd/o.total+0.01) unit_price
FROM region r 
JOIN sales_reps s
ON s.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN orders o
ON o.account_id = a.id
WHERE o.standard_qty > 100 AND o.poster_qty > 50
ORDER BY unit_price DESC;

-- What are the different channels used by account id 1001? 
-- Your final table should have only 2 columns: account name and the different channels. You can try SELECT DISTINCT to narrow down the results to only the unique values.

SELECT DISTINCT a.name, w.channel 
FROM accounts a 
JOIN web_events w
ON w.account_id = a.id
WHERE a.id = 1001;

-- Find all the orders that occurred in 2015. Your final table should have 4 columns: occurred_at, account name, order total, and order total_amt_usd.

SELECT o.occurred_at,a.name,o.total,o.total_amt_usd
FROM orders o
JOIN accounts a -- ?????????????
ON a.id = o.account_id
WHERE o.occurred_at BETWEEN '2015-01-01' AND '2016-01-01'
ORDER BY o.occurred_at;
-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SELECT COUNT(*) FROM accounts;
SELECT COUNT(primary_poc) FROM accounts;
SELECT * FROM accounts
WHERE primary_poc IS NULL;

-- Aggregation Questions

-- Find the total amount of poster_qty paper ordered in the orders table.
SELECT SUM(poster_qty) From orders;
-- Find the total amount of standard_qty paper ordered in the orders table.
SELECT SUM(standard_qty) From orders;
-- Find the total dollar amount of sales using the total_amt_usd in the orders table.
SELECT SUM(total_amt_usd) From orders;
-- Find the total amount spent on standard_amt_usd and gloss_amt_usd paper for each order in the orders table. This should give a dollar amount for each order in the table.
SELECT SUM(standard_amt_usd + gloss_amt_usd) AS sum_gloss_total FROM orders
GROUP BY id;
-- Find the standard_amt_usd per unit of standard_qty paper. Your solution should use both an aggregation and a mathematical operator.
SELECT SUM(standard_amt_usd)/SUM(standard_qty) FROM orders;

-- Questions: MIN, MAX, & AVERAGE
-- When was the earliest order ever placed? You only need to return the date.
SELECT MIN(occurred_at) FROM orders;
-- Try performing the same query as in question 1 without using an aggregation function. 
SELECT occurred_at FROM orders
ORDER BY occurred_at
LIMIT 1;
-- When did the most recent (latest) web_event occur?
SELECT MAX(occurred_at) FROM web_events;
-- Try to perform the result of the previous query without using an aggregation function.
SELECT occurred_at FROM web_events
ORDER BY occurred_at DESC
LIMIT 1;
-- Find the mean (AVERAGE) amount spent per order on each paper type, as well as the mean amount of each paper type purchased per order. 
-- Your final answer should have 6 values - one for each paper type for the average number of sales, as well as the average amount.
SELECT AVG(standard_qty) standard_qty_mean, AVG(gloss_qty) gloss_qty_mean, AVG(poster_qty) poster_qty_mean,
AVG(standard_amt_usd) standard_amt_mean, AVG(gloss_amt_usd) gloss_amt_mean, AVG(poster_amt_usd) poster_amt_mean
FROM orders;

-- Via the video, you might be interested in how to calculate the MEDIAN. 
-- Though this is more advanced than what we have covered so far try finding - what is the MEDIAN total_usd spent on all orders?
SELECT *
FROM (SELECT total_amt_usd
         FROM orders
         ORDER BY total_amt_usd
         LIMIT 3457) AS Table1
ORDER BY total_amt_usd DESC
LIMIT 2;                   -- Given Answer

-- Questions: GROUP BY

-- Which account (by name) placed the earliest order? Your solution should have the account name and the date of the order.
SELECT accounts.name, orders.occurred_at FROM accounts
JOIN orders ON orders.id = accounts.id
ORDER BY orders.occurred_at
LIMIT 1;
-- Find the total sales in usd for each account. You should include two columns - the total sales for each company's orders in usd and the company name.
SELECT accounts.name, SUM(orders.total_amt_usd) FROM accounts
JOIN orders ON orders.id = accounts.id
GROUP BY accounts.name;
-- Via what channel did the most recent (latest) web_event occur, 
-- which account was associated with this web_event? Your query should return only three values - the date, channel, and account name.
SELECT w.occurred_at AS date, w.channel, a.name
FROM web_events w
JOIN accounts a
ON a.id = w.account_id
ORDER BY date DESC
LIMIT 1;
-- Find the total number of times each type of channel from the web_events was used.
-- Your final table should have two columns - the channel and the number of times the channel was used.
SELECT channel, COUNT(*) times_used FROM web_events
GROUP BY channel;
-- Who was the primary contact associated with the earliest web_event? 
SELECT a.primary_poc AS primary_contact
FROM accounts a
JOIN web_events w
ON w.account_id = a.id
ORDER BY w.occurred_at
LIMIT 1;
-- What was the smallest order placed by each account in terms of total usd.
-- Provide only two columns - the account name and the total usd. Order from smallest dollar amounts to largest.
SELECT a.name AS name, MIN(o.total_amt_usd) AS smallest_order
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY name
ORDER BY smallest_order;
-- Find the number of sales reps in each region. Your final table should have two columns - the region and the number of sales_reps. Order from fewest reps to most reps.
SELECT r.name AS region_name, COUNT(*) AS count
FROM region r
JOIN sales_reps s
ON s.region_id = r.id
GROUP BY region_name
ORDER BY count;

-- Questions: GROUP BY Part II

-- For each account, determine the average amount of each type of paper they purchased across their orders. 
-- Your result should have four columns - one for the account name and one for the average quantity purchased for each of the paper types for each account. 
SELECT a.name AS name, AVG(o.standard_qty) AS standard_qty, AVG(o.gloss_qty) AS gloss_qty, AVG(o.poster_qty) AS poster_qty
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY name;
-- For each account, determine the average amount spent per order on each paper type.
-- Your result should have four columns - one for the account name and one for the average amount spent on each paper type.
SELECT a.name AS name, AVG(o.standard_amt_usd) AS standard_amt, AVG(o.gloss_amt_usd) AS gloss_amt, AVG(o.poster_amt_usd) AS poster_amt
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY name;
-- Determine the number of times a particular channel was used in the web_events table for each sales rep. 
-- Your final table should have three columns - the name of the sales rep, the channel, and the number of occurrences. 
-- Order your table with the highest number of occurrences first.

SELECT s.name name, w.channel channel, COUNT(*) AS count
FROM sales_reps s
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN web_events w 
ON w.account_id = a.id
GROUP BY name, channel
ORDER BY count DESC;
-- Determine the number of times a particular channel was used in the web_events table for each region. 
-- Your final table should have three columns - the region name, the channel, and the number of occurrences. 
-- Order your table with the highest number of occurrences first.
SELECT r.name name, w.channel channel, COUNT(*) AS count
FROM region r
JOIN sales_reps s
ON s.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN web_events w 
ON w.account_id = a.id
GROUP BY name, channel
ORDER BY count DESC;

-- Questions: DISTINCT

-- Use DISTINCT to test if there are any accounts associated with more than one region.
SELECT DISTINCT a.name, r.name
FROM region r
JOIN sales_reps s
ON s.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = s.id;

-- Have any sales reps worked on more than one account?
SELECT DISTINCT s.name, COUNT(*) AS count
FROM sales_reps s
JOIN accounts a
ON a.sales_rep_id = s.id
GROUP BY s.name
ORDER BY count;

-- Questions: HAVING

-- How many of the sales reps have more than 5 accounts that they manage?
SELECT s.id, s.name, COUNT(*) AS count
FROM sales_reps s
JOIN accounts a
ON a.sales_rep_id = s.id
GROUP BY s.id,s.name
HAVING count > 5
ORDER BY count;

-- How many accounts have more than 20 orders?
SELECT a.id, a.name, COUNT(*) AS count
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY a.id, a.name
HAVING count > 20
ORDER BY count;

-- Which account has the most orders?
SELECT a.id, a.name, COUNT(*) AS count
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY a.id, a.name
ORDER BY count DESC
LIMIT 1;

-- How many accounts spent more than 30,000 usd total across all orders?
SELECT a.id, a.name, SUM(o.total_amt_usd) AS total_money_spent
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY a.id, a.name
HAVING total_money_spent > 30000
ORDER BY total_money_spent;

-- How many accounts spent less than 1,000 usd total across all orders?
SELECT a.id, a.name, SUM(o.total_amt_usd) AS total_money_spent
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY a.id, a.name
HAVING total_money_spent < 1000
ORDER BY total_money_spent;

-- Which account has spent the most with us?
SELECT a.id, a.name, SUM(o.total_amt_usd) AS total_money_spent
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY a.id, a.name
ORDER BY total_money_spent DESC
LIMIT 1;

-- Which account has spent the least with us?
SELECT a.id, a.name, SUM(o.total_amt_usd) AS total_money_spent
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY a.id, a.name
ORDER BY total_money_spent
LIMIT 1;

-- Which accounts used facebook as a channel to contact customers more than 6 times?
SELECT  a.name, COUNT(*) AS count
FROM accounts a
JOIN web_events w
ON w.account_id = a.id
WHERE w.channel = 'facebook'
GROUP BY a.name
HAVING count > 6
ORDER BY count;

-- Which account used facebook most as a channel?
SELECT a.name, COUNT(*) AS count
FROM accounts a
JOIN web_events w
ON w.account_id = a.id
WHERE w.channel = 'facebook'
GROUP BY a.name
ORDER BY count DESC
LIMIT 1;

-- Which channel was most frequently used by most accounts?
SELECT a.name, w.channel, COUNT(*) AS count
FROM accounts a
JOIN web_events w
ON w.account_id = a.id
GROUP BY a.name, w.channel
ORDER BY count DESC
LIMIT 1;

-- Questions: Working With DATEs

-- Find the sales in terms of total dollars for all orders in each year, ordered from greatest to least. Do you notice any trends in the yearly sales totals?
SELECT YEAR(occurred_at) as year, SUM(total_amt_usd) as total_sum_usd
FROM orders
GROUP BY 1
ORDER BY 2 DESC;
 -- Which month did Parch & Posey have the greatest sales in terms of total dollars? Are all months evenly represented by the dataset?
SELECT MONTHNAME(occurred_at) as year, SUM(total_amt_usd) as total_sum_usd
FROM orders
WHERE occurred_at BETWEEN '2014-01-01' AND '2017-01-01'
GROUP BY 1
ORDER BY 2 DESC;

-- Which year did Parch & Posey have the greatest sales in terms of total number of orders? Are all years evenly represented by the dataset?
SELECT YEAR(occurred_at) as year, COUNT(*) as total
FROM orders
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

-- Which month did Parch & Posey have the greatest sales in terms of total number of orders? Are all months evenly represented by the dataset?
SELECT MONTHNAME(occurred_at) as year, COUNT(*) as total
FROM orders
WHERE occurred_at BETWEEN '2014-01-01' AND '2017-01-01'
GROUP BY 1
ORDER BY 2 DESC;

--  In which month of which year did Walmart spend the most on gloss paper in terms of dollars?
SELECT YEAR(o.occurred_at), SUM(o.gloss_amt_usd) as gloss_amount
FROM orders	o
JOIN accounts a
ON a.id = o.account_id
WHERE a.name = 'Walmart'
GROUP BY 1
ORDER BY 2 DESC;

-- Questions: CASE

-- Write a query to display for each order, the account ID, total amount of the order,
-- and the level of the order - ‘Large’ or ’Small’ - depending on if the order is $3000 or more, or smaller than $3000.

SELECT o.account_id,o.total_amt_usd AS total,
CASE WHEN total >= 3000 THEN 'Large' ELSE 'Small' END AS order_level
FROM orders	o
JOIN accounts a
ON a.id = o.account_id;

-- Write a query to display the number of orders in each of three categories, based on the total number of items in each order.
-- The three categories are: 'At Least 2000', 'Between 1000 and 2000' and 'Less than 1000'.
SELECT
CASE WHEN total >= 2000 THEN 'At least 2000'
	WHEN total >=1000 AND total< 2000 THEN 'BETWEEN 1000 AND 2000'
    ELSE 'Less than 1000' END AS order_category,
COUNT(*) AS COUNT
FROM orders	o
GROUP BY 1;
-- We would like to understand 3 different branches of customers based on the amount associated with their purchases.
--  The top branch includes anyone with a Lifetime Value (total sales of all orders) greater than 200,000 usd. 
--  The second branch is between 200,000 and 100,000 usd. The lowest branch is anyone under 100,000 usd. Provide a table that includes the level associated with each account. 
--  You should provide the account name, the total sales of all orders for the customer, and the level. Order with the top spending customers listed first.
SELECT a.name,SUM(o.total_amt_usd) AS lifetime_value,
CASE WHEN SUM(o.total_amt_usd) > 200000 THEN 'Top'
	WHEN SUM(o.total_amt_usd) >= 100000 THEN 'Middle'
    ELSE 'Low' END AS amt_level
FROM orders	o
JOIN accounts a
ON a.id = o.account_id
GROUP BY 1
ORDER BY 2 DESC; 

-- We would like to identify top performing sales reps, which are sales reps associated with more than 200 orders. Create a table with the sales rep name, 
-- the total number of orders, and a column with top or not depending on if they have more than 200 orders. Place the top sales people first in your final table.
SELECT s.name, COUNT(*) as total_orders,
CASE WHEN COUNT(*) > 200 THEN 'Top'
ELSE 'low' END AS sales_level
FROM orders o
JOIN accounts a
ON a.id = o.account_id
JOIN sales_reps s
ON s.id = a.sales_rep_id
GROUP BY 1
ORDER BY 2 DESC;

-- We would like to identify top performing sales reps, which are sales reps associated with more than 200 orders or more than 750000 in total sales.
-- The middle group has any rep with more than 150 orders or 500000 in sales. Create a table with the sales rep name, the total number of orders, 
-- total sales across all orders, and a column with top, middle, or low depending on this criteria.
-- Place the top sales people based on dollar amount of sales first in your final table. You might see a few upset sales people by this criteria!
SELECT s.name, COUNT(*) as total_orders, SUM(total_amt_usd) as total_amt_spent,
CASE WHEN COUNT(*) > 200 OR SUM(total_amt_usd) > 750000 THEN 'Top'
	WHEN COUNT(*) > 150 OR SUM(total_amt_usd) > 500000 THEN 'middle'
ELSE 'low' END AS sales_level
FROM orders o
JOIN accounts a
ON a.id = o.account_id
JOIN sales_reps s
ON s.id = a.sales_rep_id
GROUP BY 1
ORDER BY 3 DESC;

-- Sub Queries
SELECT channel, AVG(event_count) AS avg_count
FROM
(SELECT DATE(occurred_at) as date, channel, COUNT(*) AS event_count
	FROM web_events
	GROUP BY 1,2
	ORDER BY event_count DESC) sub
GROUP BY 1
ORDER BY 1;

SELECT SUM(total_amt_usd),AVG(standard_qty), AVG(gloss_qty), AVG(poster_qty)
FROM orders
WHERE MONTH(occurred_at) =
(SELECT MONTH(MIN(occurred_at))
	FROM orders
    ORDER BY 1)
ORDER BY 1;
 
 
 -- More Subqueries Quizzes
 -- Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.
 
 SELECT sub3.sales_rep_name, sub3.region_name,sub3.total
FROM(SELECT region_name, MAX(total) AS total
	FROM(SELECT s.name sales_rep_name,r.name region_name, SUM(o.total_amt_usd) AS total
			FROM orders o
			JOIN accounts a
			ON o.account_id = a.id
			JOIN sales_reps s
			ON s.id = a.sales_rep_id
			JOIN region r
			ON r.id = s.region_id
			GROUP BY 1,2) sub	
	GROUP BY 1) sub2
JOIN (SELECT s.name sales_rep_name,r.name region_name, SUM(o.total_amt_usd) AS total
			FROM orders o
			JOIN accounts a
			ON o.account_id = a.id
			JOIN sales_reps s
			ON s.id = a.sales_rep_id
			JOIN region r
			ON r.id = s.region_id
			GROUP BY 1,2
            ORDER BY 3 DESC) sub3
ON sub3.region_name = sub2.region_name AND sub3.total = sub2.total;

-- For the region with the largest sales total_amt_usd, how many total orders were placed?
SELECT r.name AS region_name, COUNT(o.total) AS count
FROM orders o
JOIN accounts a
ON o.account_id = a.id
JOIN sales_reps s
ON s.id = a.sales_rep_id
JOIN region r
ON r.id = s.region_id
GROUP BY 1
HAVING SUM(o.total_amt_usd) = (
SELECT MAX(total)
FROM (SELECT r.name AS region_name, SUM(total_amt_usd) AS total
FROM orders o
JOIN accounts a
ON o.account_id = a.id
JOIN sales_reps s
ON s.id = a.sales_rep_id
JOIN region r
ON r.id = s.region_id
GROUP BY 1
ORDER BY 2 DESC) sub);

-- How many accounts had more total purchases than the account name which has bought the most standard_qty paper throughout their lifetime as a customer? 
SELECT COUNT(*)
FROM (SELECT a.name
FROM orders o
JOIN accounts a
ON o.account_id = a.id
GROUP BY 1
HAVING SUM(o.total) > (SELECT total 
						FROM (SELECT a.name, SUM(o.standard_qty) AS std_qty_total, SUM(o.total) AS total
							FROM orders o
							JOIN accounts a
							ON o.account_id = a.id
							GROUP BY 1
							ORDER BY 2 DESC
							LIMIT 1)sub)) count_sub;

-- For the customer that spent the most (in total over their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel?
SELECT a.name, w.channel, COUNT(*) AS count
FROM accounts a
JOIN web_events w
ON a.id = w.account_id AND a.name = (SELECT account_name
									FROM (SELECT a.name AS account_name, SUM(o.total_amt_usd)
											FROM orders o
											JOIN accounts a
											ON o.account_id = a.id
											GROUP BY 1
											ORDER BY 2 DESC
											LIMIT 1)sub) 
GROUP BY 1,2
ORDER BY 3 DESC;

-- What is the lifetime average amount spent in terms of total_amt_usd for the top 10 total spending accounts?
SELECT AVG(total_amt_spent) AS avg_amt_spent
FROM(SELECT a.name, SUM(o.total_amt_usd) as total_amt_spent
		FROM orders o
		JOIN accounts a
		ON o.account_id = a.id
		GROUP BY 1
		ORDER BY 2 DESC
		LIMIT 10) sub;
        
-- What is the lifetime average amount spent in terms of **total_amt_usd**, including only the companies that spent more per order, on average,
-- than the average of all orders.
SELECT AVG(average)
FROM (SELECT a.name, AVG(o.total_amt_usd) AS average
FROM orders o
		JOIN accounts a
		ON o.account_id = a.id
        GROUP BY 1
HAVING AVG(o.total_amt_usd) > 
(SELECT AVG(o.total_amt_usd) As total_avg
FROM orders o)) sub;

-- Quiz: LEFT & RIGHT

-- In the accounts table, there is a column holding the website for each company. The last three digits specify what type of web address they are using.
-- Pull these extensions and provide how many of each website type exist in the accounts table.
SELECT RIGHT(website,3) AS website_type, COUNT(*) AS count FROM accounts
GROUP BY 1
ORDER BY 2;

SELECT DISTINCT RIGHT(website,3) AS website_type
FROM accounts;

-- Use the accounts table to pull the first letter of each company name to see the distribution of company names that begin with each letter (or number). 
SELECT LEFT(name,1) AS first_letter, COUNT(*) AS count
FROM accounts
GROUP BY 1
ORDER BY 2 DESC;

-- Use the accounts table and a CASE statement to create two groups: one group of company names that start with a number 
-- and a second group of those company names that start with a letter. What proportion of company names start with a letter?
SELECT SUM(num) as num_count, SUM(letter) AS letter_count, SUM(letter)/(SUM(num)+SUM(letter)) * 100 AS letter_proportion
FROM (SELECT name,
	CASE WHEN LEFT(name,1) IN ('0','1','2','3','4','5','6','7','8','9') 
	THEN 1 ELSE 0 END AS num,
	CASE WHEN LEFT(name,1) NOT IN ('0','1','2','3','4','5','6','7','8','9')
	THEN 1 ELSE 0 END AS letter
FROM accounts) AS table1;

-- Consider vowels as a, e, i, o, and u. What proportion of company names start with a vowel, and what percent start with anything else?
SELECT SUM(vowels) AS vowel_count, SUM(rest) AS rest_count, SUM(vowels)/(SUM(vowels)+SUM(rest)) * 100 AS vowels_proportion
FROM (SELECT name, CASE WHEN LEFT(name, 1) IN ('A','E','I','O','U') 
			THEN 1 ELSE 0 END AS vowels, 
	CASE WHEN LEFT(name, 1) NOT IN ('A','E','I','O','U') 
		THEN 1 ELSE 0 END AS rest
FROM accounts) table1;

-- Quizzes POSITION & STRPOS
-- Use the accounts table to create first and last name columns that hold the first and last names for the primary_poc. 
SELECT LEFT(primary_poc,POSITION(' ' IN primary_poc)-1) AS first_name,
RIGHT(primary_poc, LENGTH(primary_poc) - POSITION(' ' IN primary_poc)) AS last_name
FROM accounts;

-- Now see if you can do the same thing for every rep name in the sales_reps table. Again provide first and last name columns.
SELECT LEFT(name,POSITION(' ' IN name)-1) AS first_name,
RIGHT(name,LENGTH(name)-POSITION(' ' IN name)) AS last_name
FROM sales_reps;

-- Quizzes CONCAT

-- Each company in the accounts table wants to create an email address for each primary_poc. 
-- The email address should be the first name of the primary_poc . last name primary_poc @ company name .com.
SELECT
CONCAT(LEFT(primary_poc,POSITION(' ' IN primary_poc)-1),'.',RIGHT(primary_poc, LENGTH(primary_poc) - POSITION(' ' IN primary_poc)),'@',name,'.com')
FROM accounts;

-- You may have noticed that in the previous solution some of the company names include spaces, 
-- which will certainly not work in an email address. See if you can create an email address that will work by removing all of the spaces in the account name
SELECT
CONCAT(LEFT(primary_poc,POSITION(' ' IN primary_poc)-1),'.',RIGHT(primary_poc, LENGTH(primary_poc) - POSITION(' ' IN primary_poc)),'@',REPLACE(name,' ',''),'.com')
FROM accounts;

-- Writing the above two queries using temp table
WITH temp1 AS 
(SELECT LEFT(primary_poc,POSITION(' ' IN primary_poc)-1) AS first_name,
RIGHT(primary_poc, LENGTH(primary_poc) - POSITION(' ' IN primary_poc)) AS last_name, name
FROM accounts)
SELECT first_name, last_name, CONCAT(first_name,'.',last_name,'@',name,'.com') AS work_email_address
FROM temp1;

WITH temp1 AS 
(SELECT LEFT(primary_poc,POSITION(' ' IN primary_poc)-1) AS first_name,
RIGHT(primary_poc, LENGTH(primary_poc) - POSITION(' ' IN primary_poc)) AS last_name, name
FROM accounts)
SELECT first_name, last_name, CONCAT(first_name,'.',last_name,'@',REPLACE(name,' ',''),'.com') AS work_email_address
FROM temp1;

-- We would also like to create an initial password, which they will change after their first log in. 
-- The first password will be the first letter of the primary_poc's first name (lowercase), then the last letter of their first name (lowercase),
-- the first letter of their last name (lowercase), the last letter of their last name (lowercase), the number of letters in their first name, 
-- the number of letters in their last name, and then the name of the company they are working with, all capitalized with no spaces.
WITH temp1 AS 
(SELECT LEFT(primary_poc,POSITION(' ' IN primary_poc)-1) AS first_name,
RIGHT(primary_poc, LENGTH(primary_poc) - POSITION(' ' IN primary_poc)) AS last_name, name
FROM accounts)
SELECT first_name, last_name,
CONCAT(LOWER(LEFT(first_name,1)),LOWER(RIGHT(first_name,1)),LOWER(LEFT(last_name,1)),LOWER(RIGHT(last_name,1)),LENGTH(first_name),LENGTH(last_name),UPPER(REPLACE(name,' ','')))
FROM temp1;

-- COALESCE Quizzes
SELECT *
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id
WHERE o.total IS NULL; 

SELECT COALESCE(o.id, a.id) modified_id
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id
WHERE o.total IS NULL; 

SELECT COALESCE(a.id,o.account_id) modified_id 
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id
WHERE o.total IS NULL; 

SELECT COALESCE(o.id, a.id) modified_id, a.name, a.website, a.lat, a.long, a.primary_poc, a.sales_rep_id,
COALESCE(standard_qty,0) standard_qty,COALESCE(gloss_qty,0) gloss_qty,COALESCE(poster_qty,0) poster_qty,
COALESCE(standard_amt_usd,0) standard_amt_usd, COALESCE(gloss_amt_usd,0) gloss_amt_usd,COALESCE(poster_amt_usd,0) poster_amt_usd,COALESCE(total_amt_usd,0) total_amt_usd
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id
WHERE o.total IS NULL;

SELECT COUNT(*)
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id;

SELECT COALESCE(o.id, a.id) modified_id, a.name, a.website, a.lat, a.long, a.primary_poc, a.sales_rep_id,
COALESCE(standard_qty,0) standard_qty,COALESCE(gloss_qty,0) gloss_qty,COALESCE(poster_qty,0) poster_qty,
COALESCE(standard_amt_usd,0) standard_amt_usd, COALESCE(gloss_amt_usd,0) gloss_amt_usd,COALESCE(poster_amt_usd,0) poster_amt_usd,COALESCE(total_amt_usd,0) total_amt_usd
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id;

--  SQL Window Functions

SELECT standard_amt_usd, SUM(standard_amt_usd)
OVER (ORDER BY occurred_at) AS running_total
FROM orders;

SELECT standard_amt_usd, YEAR(occurred_at) AS year, SUM(standard_amt_usd)
OVER (PARTITION BY YEAR(occurred_at) ORDER BY occurred_at) AS running_total
FROM orders;

SELECT id, account_id, total,
RANK() OVER(PARTITION BY account_id ORDER BY total DESC) AS total_rank
FROM orders;

-- Aggregates in window functions
SELECT id,
       account_id,
       standard_qty,
       month(occurred_at) AS month,
       DENSE_RANK() OVER (PARTITION BY account_id ORDER BY month(occurred_at)) AS denserank,
       SUM(standard_qty) OVER (PARTITION BY account_id ORDER BY month(occurred_at)) AS sum_std_qty,
       COUNT(standard_qty) OVER (PARTITION BY account_id ORDER BY month(occurred_at)) AS count_std_qty,
       AVG(standard_qty) OVER (PARTITION BY account_id ORDER BY month(occurred_at)) AS avg_std_qty,
       MIN(standard_qty) OVER (PARTITION BY account_id ORDER BY month(occurred_at)) AS min_std_qty,
       MAX(standard_qty) OVER (PARTITION BY account_id ORDER BY month(occurred_at)) AS max_std_qty
FROM orders;

-- Same as the above query but without the order by statement
SELECT id,
       account_id,
       standard_qty,
       month(occurred_at) AS month,
       DENSE_RANK() OVER (PARTITION BY account_id) AS denserank,
       SUM(standard_qty) OVER (PARTITION BY account_id) AS sum_std_qty,
       COUNT(standard_qty) OVER (PARTITION BY account_id) AS count_std_qty,
       AVG(standard_qty) OVER (PARTITION BY account_id) AS avg_std_qty,
       MIN(standard_qty) OVER (PARTITION BY account_id) AS min_std_qty,
       MAX(standard_qty) OVER (PARTITION BY account_id) AS max_std_qty
FROM orders;

-- Shorten Your Window Function Queries by Aliasing
SELECT id,
       account_id,
       standard_qty,
       month(occurred_at) AS month,
       DENSE_RANK() OVER main_window AS denserank,
       SUM(standard_qty) OVER main_window AS sum_std_qty,
       COUNT(standard_qty) OVER main_window AS count_std_qty,
       AVG(standard_qty) OVER main_window AS avg_std_qty,	
       MIN(standard_qty) OVER main_window AS min_std_qty,
       MAX(standard_qty) OVER main_window AS max_std_qty
FROM orders
WINDOW main_window AS (PARTITION BY account_id ORDER BY month(occurred_at));

SELECT occurred_at,total_amt_usd,
LEAD(total_amt_usd) OVER (ORDER BY occurred_at) AS the_lead,
LEAD(total_amt_usd) OVER (ORDER BY occurred_at) - total_amt_usd AS lead_difference
FROM (
SELECT occurred_at,
       SUM(total_amt_usd) AS total_amt_usd
  FROM orders 
 GROUP BY 1
) sub1;

-- Percentiles with Partitions

-- Use the NTILE functionality to divide the accounts into 4 levels in terms of the amount of standard_qty for their orders. 
-- Your resulting table should have the account_id, the occurred_at time for each order, the total amount of standard_qty paper purchased, 
-- and one of four levels in a standard_quartile column.
SELECT account_id, occurred_at, standard_qty,
NTILE(4) OVER(PARTITION BY account_id ORDER BY standard_qty) AS standard_quartile
FROM orders
ORDER BY account_id;

-- Use the NTILE functionality to divide the accounts into two levels in terms of the amount of gloss_qty for their orders. 
-- Your resulting table should have the account_id, the occurred_at time for each order, the total amount of gloss_qty paper purchased, 
-- and one of two levels in a gloss_half column.
SELECT account_id, occurred_at, gloss_qty,
NTILE(2) OVER(PARTITION BY account_id ORDER BY gloss_qty) as gloss_half
FROM orders
ORDER BY account_id;

-- Use the NTILE functionality to divide the orders for each account into 100 levels in terms of the amount of total_amt_usd for their orders. 
-- Your resulting table should have the account_id, the occurred_at time for each order, the total amount of total_amt_usd paper purchased, 
-- and one of 100 levels in a total_percentile column.
SELECT account_id, occurred_at, total_amt_usd,
NTILE(100) OVER(PARTITION BY account_id ORDER BY total_amt_usd) AS total_percentile
FROM orders
ORDER BY account_id;

-- Quiz: FULL OUTER JOIN

-- each account who has a sales rep and each sales rep that has an account (all of the columns in these returned rows will be full)
-- but also each account that does not have a sales rep and each sales rep that does not have an account (some of the columns in these returned rows will be empty)
-- write a query with FULL OUTER JOIN to fit the above described Parch & Posey scenario 
SELECT *
FROM accounts 
FULL JOIN sales_reps 
ON accounts.sales_rep_id = sales_reps.id;

-- Inequality JOINs
-- write a query that left joins the accounts table and the sales_reps tables on each sale rep's ID number and joins it using the < comparison operator 
-- on accounts.primary_poc and sales_reps.name, like so: accounts.primary_poc < sales_reps.name. The query results should be a table with three columns: The account name, the primary contact name, and the sales representative's name
SELECT a.name,a.primary_poc,sr.name
FROM accounts a
LEFT JOIN sales_reps sr
ON a.sales_rep_id = sr.id
AND a.primary_poc < sr.name;

-- Quiz: Self JOINs
-- Modify the query from the previous video, which is pre-populated in the SQL Explorer below, to perform the same interval analysis except for the web_events table. 
-- Also:change the interval to 1 day to find those web events that occurred after, but not more than 1 day after, another web event 
-- add a column for the channel variable in both instances of the table in your query
SELECT 	w1.id AS w1_id,
		w1.account_id AS w1_account_id,
		w1.occurred_at AS w1_occurred_at,
		w1.channel AS w1_channel,
		w2.id AS w2_id,
		w2.account_id AS w2_account_id,
		w2.occurred_at AS w2_occurred_at,
		w2.channel AS w2_channel
FROM web_events w1
LEFT JOIN web_events w2
   ON w1.account_id = w2.account_id
  AND w2.occurred_at > w1.occurred_at
  AND w2.occurred_at <= DATE_ADD(w1.occurred_at, INTERVAL 1 DAY)
ORDER BY w1.account_id, w1.occurred_at;

-- Quiz: UNION
-- Write a query that uses UNION ALL on two instances (and selecting all columns) of the accounts table.
SELECT *
FROM accounts a1

UNION ALL

SELECT *
FROM accounts a2;

-- Add a WHERE clause to each of the tables that you unioned in the query above, 
-- filtering the first table where name equals Walmart and filtering the second table where name equals Disney.
SELECT *
FROM accounts a1
WHERE name = 'Walmart'

UNION ALL

SELECT *
FROM accounts a2
WHERE name = 'Disney';

-- Perform the union in your first query (under the Appending Data via UNION header) in a common table expression and name it double_accounts. 
-- Then do a COUNT the number of times a name appears in the double_accounts table.
WITH double_accounts AS (SELECT *
FROM accounts a1

UNION ALL

SELECT *
FROM accounts a2)

SELECT name, COUNT(*) name_count
FROM double_accounts
GROUP BY 1
ORDER BY 2 DESC;




