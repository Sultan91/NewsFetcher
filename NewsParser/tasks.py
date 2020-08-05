from celery import shared_task
from NewsExtractor.Parser import retrieve_news
from django.db import connection
import datetime


@shared_task
def write():
    fresh_news = retrieve_news()
    with connection.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS News ( \
                            id serial PRIMARY KEY,\
                            title VARCHAR ( 250 ) UNIQUE NOT NULL, \
                            url VARCHAR ( 250 ) NOT NULL, \
                              saved_at TIMESTAMP );")

        query = """      INSERT INTO News (title, url, saved_at)
                         VALUES (%s, %s, %s) 
                         ON CONFLICT (title) DO NOTHING;
                     """
        for i in range(len(fresh_news[0])):
            title = fresh_news[0][i]
            url = fresh_news[1][i]
            time = datetime.datetime.now()
            record_tuple = (title, url, time)
            cursor.execute(query, record_tuple)
    print("Fresh news fetched and written to DB")
    return None
