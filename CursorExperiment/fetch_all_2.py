import sqlite3
 
conn = sqlite3.connect("mydatabase.db")
#conn.row_factory = sqlite3.Row
cursor = conn.cursor()
 
sql = "SELECT * FROM albums WHERE artist=?"
# cursor.execute(sql, [("Red")])
cursor.execute(sql, [("BBB")])
# print(cursor.fetchall()) # or use fetchone()
# print(cursor.fetchone()) # or use fetchone()

fetch_1_res = cursor.fetchone()
res = fetch_1_res if fetch_1_res not in [None, 'None'] else 0
# print('fetch_1_res', fetch_1_res)
print('fetch_1_res', fetch_1_res)
print('res', res)


# print("Here's a listing of all the records in the table:")
# for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
#     print(row)
 
# print("Results from a LIKE query:")
# sql = "SELECT * FROM albums WHERE title LIKE 'The%'"
# cursor.execute(sql)
 
# print(cursor.fetchall())
# res1 = cursor.fetchone()
# print('cursor.fetchone(): ', res1)