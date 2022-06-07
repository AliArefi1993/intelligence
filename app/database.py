import psycopg2

conn = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "db", port = "5432")

print("Opened database successfully")
test=1