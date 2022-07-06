from unittest import result
from mysql import connector

CREDENTIALS = {'host': 'db',
               'port': 3306,
               'user': 'adminuser',
               'database': 'social',
               'password': 'fantastic'}


def create_connector():
    return connector.connect(**CREDENTIALS)


def run_query(query):
    with create_connector() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        conn.commit()
    return results
