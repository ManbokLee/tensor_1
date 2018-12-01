import sqlite3

con = sqlite3.connect('sales.db')

query = """
create table if not exists sales(
    mbr VARCHAR(10),
    product VARCHAR(10),
    amount NUMBER,
    date DATE default '2018-12-01'
);
"""
con.execute(query)
con.commit()
'''
data = [
    ('이','phone',50),
    ('김','TV',100),
    ('박','phone2',50),
    ('송','running',50)
    ]

stmt = """ 
insert into sales (mbr, product, amount) values(?,?,?)
"""
con.executemany(stmt, data)
con.commit()
'''
cursor = con.execute("select * from sales;")

rows = cursor.fetchall()
row_counter = 0
for i in rows:
    print(i)
    row_counter += 1
print("회원 수: {}".format(row_counter))
con.close()



