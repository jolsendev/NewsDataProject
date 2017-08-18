#!/usr/bin/env python3

'''
def get_posts():
    """Return all posts from the 'database', most recent first."""
    conn = psycopg2.connect("dbname=forum")
    cur = conn.cursor()
    cur.execute("SELECT content, time FROM posts order by time desc;")
    posts = cur.fetchall()
    conn.close()
    return posts


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    bleached_content = bleach.clean(content)
    conn = psycopg2.connect("dbname=forum")
    cur = conn.cursor()
    cur.execute("INSERT INTO posts (content) VALUES (%s)", (bleached_content,))
    conn.commit()
    conn.close()
'''


def main():
    #call code here




if __name__ == '__main__':
    #do stuff here.