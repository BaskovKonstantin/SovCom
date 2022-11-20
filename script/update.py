from pprint import pprint # optional
import requests # pip install requests
import xml.etree.ElementTree as ET
import sqlite3
import datetime
import time


def get_cbrf_data(dd: int, mm: int, yyyy: int):
  if 1 <= dd <= 31 and 1 <= mm <= 12 and 1970 <= yyyy:
    r = requests.post(url=f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={dd}/{mm}/{yyyy}')
    if not r.ok:
      print('Error')
      return
    root = ET.fromstring(r.text)
    # print(r.text)
    valutes = []
    for child in root:
      valute = {}
      for gchild in child:
        valute[gchild.tag] = gchild.text
      valutes.append(valute)
      # print(child.tag, child.attrib)
    # pprint(valutes)
    return valutes

def insert_data(con, tablename, date, price):

  try:
    cursor = con.cursor()
    print("Подключен к SQLite")

    sqlite_insert_query = f"""INSERT INTO {tablename} VALUES ({date}, {price});"""
    cursor.execute(sqlite_insert_query)
    con.commit()
    print("Запись успешно вставлена   в таблицу sqlitedb_developers ", cursor.rowcount)
    cursor.close()

  except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)

def update_db(con):


  dt_now = str(datetime.date.today())
  dd = int(dt_now.split(sep='-')[2])
  mm = int(dt_now.split(sep='-')[1])
  yyyy = int(dt_now.split(sep='-')[0])

  answer = get_cbrf_data( dd, mm, yyyy)

  for i in answer:

    insert_data(con, i['CharCode'].lower(), dt_now, i['Value'])
  time.sleep(86400)

