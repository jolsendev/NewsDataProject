#!/usr/bin/env python3


class NewsConstants:

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
