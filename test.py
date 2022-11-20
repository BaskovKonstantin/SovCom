import pandas
import sqlite3
import os
from script import update
import datetime

dt_now = str(datetime.date.today())
print(dt_now)


print(os.listdir('C:\\Users\\KonBas\\PycharmProjects\\flaskProject1\\data'))
con = sqlite3.connect('C:\\Users\\KonBas\\PycharmProjects\\flaskProject1\\data\\data')



start_date = '2022-10-12'
end_date = '2022-11-17'
tablename = 'eur'


answer =  update.get_cbrf_data(int(dt_now.split(sep = '-')[2]) , int(dt_now.split(sep = '-')[1]), int(dt_now.split(sep = '-')[0]) )
j = 0
for i in answer:
    print(j)
    j+=1
    print(i['CharCode'].lower())
    print(i['Value'])
    update.insert_data(con, i['CharCode'].lower(), dt_now, i['Value'])




