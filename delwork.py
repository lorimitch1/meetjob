import db

print("刪除員工資料")

sql = "select su_no from employee"

cursor = db.conn.cursor()

cursor.execute(sql)
db.conn.commit()

result = cursor.fetchall() # 抓取全部的資料出來
print("員工ID")
for row in result:
    print(row[0])
    
no = input("請輸入ID：") 


sql = "delete from jobs where su_no='{}' ".format(no)

cursor.execute(sql)
db.conn.commit()
db.conn.close()
