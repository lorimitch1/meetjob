# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:05:21 2022

@author: watson
"""

import db

print("修改學生資料")

sql = "select staffid from employee"

cursor = db.conn.cursor()

cursor.execute(sql)
db.conn.commit()

result = cursor.fetchall() # 抓取全部的資料出來
print("員工ID")
for row in result:
    print(row[0])
    
staffid = input("請輸入員工ID：") 
tel = input("請輸入欲修改的電話：")

sql = "update employee set tel='{}' , where staffid='{}'".format(tel,staffid)


#"update students set  tel='04-12345678' , mobile='091111111'  where su_no='xxxxxxx' "

cursor.execute(sql)
db.conn.commit()

 

db.conn.close()    




