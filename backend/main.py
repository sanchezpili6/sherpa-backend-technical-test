from mysql import connector

CREDENTIALS = {'host': 'db',
               'port': 3306,
               'user': 'pinner',
               'database': 'pinterest',
               'password': 'pintastic'}



def create_connector():
    return connector.connect(**CREDENTIALS)
