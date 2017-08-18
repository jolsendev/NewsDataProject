#!/usr/bin/env python3

#
# ef get_posts():
#    """Return all posts from the 'database', most recent first."""
#    conn = psycopg2.connect("dbname=forum")
#   cur = conn.cursor()
# cur.execute("SELECT content, time FROM posts order by time desc;")
#    posts = cur.fetchall()
#    conn.close()
#    return posts


# def add_post(content):
#    """Add a post to the 'database' with the current timestamp."""
#    bleached_content = bleach.clean(content)
#    conn = psycopg2.connect("dbname=forum")
#    cur = conn.cursor()
#    cur.execute("INSERT INTO posts (content) VALUES (%s)", (bleached_content,))
#    conn.commit()
#    conn.close()

import psycopg2

COL_TITLE_OF_ARTICLE = 0
COL_NUMBER_OF_ARTICLES = 1

QEURY_QUESTION_ONE = '''
    SELECT articles.title, count(*) AS num from log, articles 
    WHERE log.path <> '/' 
    AND SUBSTR(log.path, 10) like '%' || articles.slug || '%' 
    GROUP BY articles.title 
    ORDER BY num DESC 
    LIMIT 3 OFFSET 0;
'''


def get_query_results(query):
    try:
        conn = psycopg2.connect("dbname=news")
    except psycopg2.Error:
        print("I am unable to connect to the database.")

    cur = conn.cursor()
    cur.execute(QEURY_QUESTION_ONE)
    rows = cur.fetchall()
    conn.close()
    return rows


def question_one_result():
    rows = get_query_results(QEURY_QUESTION_ONE)
    results = ""
    for row in rows:
        results += row[COL_TITLE_OF_ARTICLE] + " - " + str(row[COL_NUMBER_OF_ARTICLES]) + "\n"
    return results


def question_two_result():
    return "Question 2 not implemented yet"


def question_three_result():
    return "Question 3 not implemented yet"


if __name__ == '__main__':
    print(
        'Question 1 -  What are the most popular three articles of all time? Which articles have been accessed the '
        'most?\n')
    print(question_one_result())
    print("Question 2 - Who are the most popular article authors of all time?")
    print(question_two_result())
    print("Question 3 - On which days did more than 1% of requests lead to errors?")
    print(question_three_result())
