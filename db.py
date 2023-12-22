import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT NOW() ")

# Retrieve query results
records = cur.fetchall()