import pandas
import sqlite3

con = sqlite3.connect('data')


e = pandas.read_csv('eur_rub.csv', sep=';')
u = pandas.read_csv('usd_rub.csv', sep=';')
print(e)
e.to_sql('eur_rub', con, if_exists = 'replace')
u.to_sql('usd_rub', con, if_exists = 'replace')


