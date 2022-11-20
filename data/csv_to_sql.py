import pandas
import sqlite3
import os

con = sqlite3.connect('data')


files = os.listdir('C:\\Users\\KonBas\\PycharmProjects\\flaskProject1\\data')

for file in files:

    part = file.split(sep = '.')
    if (len(part) > 1):
        if (part[1] == 'csv'):
            data = pandas.read_csv(file, sep=';')
            data.to_sql(part[0].split(sep='_')[0], con, if_exists='replace')

# e = pandas.read_csv('eur_rub.csv', sep=';')
# u = pandas.read_csv('usd_rub.csv', sep=';')
# print(e)
# e.to_sql('eur_rub', con, if_exists = 'replace')
# u.to_sql('usd_rub', con, if_exists = 'replace')


