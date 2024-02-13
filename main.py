# import psycopg2
#
# conn = psycopg2.connect(host="localhost", dbname="stayanka", user="postgres",
#                         password="123", port="5432")
#
# cur = conn.cursor()
#
# cur.execute("""SELECT * FROM users;""")
# data = cur.fetchall()
#
# conn.commit()
# print(data)
#
# cur.close()
# conn.close()


# import psycopg2
#
# # PostgreSQLga ulanish
# conn = psycopg2.connect(
#     host="localhost", port=5432, dbname="institut", user="postgres", password=123
# )
#
# # Ma'lumotlar ustida amal bajarish
# cur = conn.cursor()
# cur.execute("SELECT * FROM talabala")
# rows = cur.fetchall()
#
# for row in rows:
#     print(row)
#
# # Ulanishni yopish
# cur.close()
# conn.close()


# import psycopg2
#
# conn = psycopg2.connect(
#     host="localhost",
#     dbname="main",
#     password=123,
#     port=5432,
#     user='postgres'
# )
#
# cur = conn.cursor()
# conn.autocommit = True
#
# # cur.execute("CREATE DATABASE main;")
#
# cur.execute("""CREATE TABLE IF NOT EXISTS footballers(
#             id SERIAL PRIMARY KEY,
#             firstname VARCHAR(50),
#             lastname VARCHAR(50),
#             age INT
#             );""")
#
# cur.execute("""DELETE FROM footballers WHERE id=3;""")
#
# cur.execute("""INSERT INTO public.footballers(
# 	firstname, lastname, age)
# 	VALUES ('Kevin', 'De Bruyne', 33);""")
# print('Success')
#
# cur.execute("""SELECT * FROM footballers;""")
# data = cur.fetchall()
# print(data)
#
# cur.close()
# conn.close()

from p_sql_class import helperDB
base = helperDB()
base.setup()
base.delete_item(2)
base.add_item(123456, "Abdu.axa")
data = base.select_item()
base.update_item(2, "Abduaxad")
base.log_out()
print("Success")
print(data)
