'SQL Queries'
'1.	How many sessions were there since 1 June 2017(inclusive)?'

SELECT
  sum(totals.visits) as Sessions
FROM
  `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
  _table_suffix BETWEEN '20170601'
  AND FORMAT_DATE('%Y%m%d',DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))

'ANSWER = 137946 SESSIONS'


'2.For the last two days of data, how many sessions were there per day?'

SELECT
  _table_suffix as days,
  sum(totals.visits) as Sessions
FROM
  `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
  _table_suffix BETWEEN '20170731'
  AND FORMAT_DATE('%Y%m%d',DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
group by _table_suffix

'''ANSWER
DATE	SESSIONS
20170731	2620
20170801	2556'''

'3. How may sources had transactions in 2017.'

SELECT  
  COUNT( DISTINCT trafficsource.source) as Sources,
  sum(totals.transactions) as Transactions
FROM
  `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
  _table_suffix LIKE '%2017%'
  AND totals.transactions > 0

'ANSWER = 30 sources'
	
