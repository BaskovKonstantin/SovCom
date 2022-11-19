import pandas
import sqlite3
import os
from script import predict


print(os.listdir('C:\\Users\\KonBas\\PycharmProjects\\flaskProject1\\data'))
con = sqlite3.connect('C:\\Users\\KonBas\\PycharmProjects\\flaskProject1\\data\\data')


print(pandas.read_sql('SELECT * FROM eur_rub', con).set_index('index'))

start_date = '2022-10-12'
end_date = '2022-11-17'
tablename = 'eur_rub'


print('Regression')
print(predict.get_predict(con, tablename, start_date, end_date))