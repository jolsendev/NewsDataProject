#!/usr/bin/env python3

import psycopg2

COL_ONE = 0
COL_TWO = 1


QUERY_QUESTION_ONE = '''
    SELECT articles.title, count(*) AS num from log, articles 
    WHERE log.path <> '/' 
    AND SUBSTR(log.path, 10) like '%' || articles.slug || '%' 
    GROUP BY articles.title 
    ORDER BY num DESC 
    LIMIT 3 OFFSET 0;
'''

QUERY_QUESTION_TWO = ''' 
    SELECT authors.name , result.num 
    FROM  authors , (    
        SELECT articles.author, count(*) AS num from log, articles
        WHERE log.path <> '/'
        AND SUBSTR(log.path, 10) like '%' || articles.slug || '%'
        GROUP BY articles.author
        ORDER BY num DESC) as result        
    WHERE authors.id = result.author;
'''


QUERY_QUESTION_THREE = ''' 
SELECT final_result.total_requests, final_result.percentage
FROM (
    SELECT result.t_total_requests_per_day as total_requests, ( CAST (result_two.num AS FLOAT) / CAST(result.num AS FLOAT) ) * 100 as percentage
    FROM (
        SELECT TO_CHAR(time, 'Mon, dd YYYY') as t_total_requests_per_day, count(*) as num
        FROM log
        GROUP BY t_total_requests_per_day
    ) as result,
        (
        SELECT TO_CHAR(time, 'Mon, dd YYYY') as t_total_bad_requests_per_day, count(*) as num
        FROM log
        WHERE status != '200 OK'
        GROUP BY t_total_bad_requests_per_day
    ) as result_two
    WHERE result.t_total_requests_per_day = result_two.t_total_bad_requests_per_day) as final_result
WHERE final_result.percentage > 1.0;
'''

def get_query_results(query):
    try:
        conn = psycopg2.connect("dbname=news")
    except psycopg2.Error:
        print("I am unable to connect to the database.")

    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows


def question_one_result():
    rows = get_query_results(QUERY_QUESTION_ONE)
    results = ""
    for row in rows:
        results += row[COL_ONE] + " - " + str(row[COL_TWO]) + "\n"
    return results


def question_two_result():
    rows = get_query_results(QUERY_QUESTION_TWO)
    results = ""
    for row in rows:
        results += row[COL_ONE] + " - " + str(row[COL_TWO]) + "\n"
    return results


def question_three_result():
    rows = get_query_results(QUERY_QUESTION_THREE)
    results = ""
    for row in rows:
        results += row[COL_ONE] + " - " + "%"+str("%.1f" % row[COL_TWO]) + " errors\n"
    return results


if __name__ == '__main__':
    print(
        'Question 1 -  What are the most popular three articles of all time? Which articles have been accessed the '
        'most?\n')
    print(question_one_result())
    print("Question 2 - Who are the most popular article authors of all time?\n")
    print(question_two_result())
    print("Question 3 - On which days did more than 1% of requests lead to errors?\n")
    print(question_three_result())
