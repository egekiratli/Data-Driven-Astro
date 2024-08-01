import psycopg2

def select_all(table):
  conn = psycopg2.connect(dbname='db', user='grok') #connection to database
  cursor = conn.cursor() #obj that interfaces with database
  query = f'SELECT * FROM {table}'
  cursor.execute(query) #to run query
  records = cursor.fetchall() #returns the output of last query
  return records


  