import pandas
import sqlite3
from statistics import mean
from sklearn.linear_model import LinearRegression



def get_predict(con, tablename, start_date, end_date):

    df = pandas.read_sql(f'SELECT * FROM \'{tablename}\' WHERE date > \'{start_date}\' AND date < \'{end_date}\'', con).set_index('index')

    X = df['price'][0:len(df['price'])-2].to_numpy().reshape(-1, 1)
    y = df['price'][1:len(df['price'])-1].to_numpy().reshape(-1, 1)

    # print(X)
    # print(y)
    print(df['price'][len(df['price'])-1])

    model = LinearRegression()
    model_fit = model.fit(X, y)
    std = df['price'].std()/2
    expectation = model_fit.predict([[df['price'][len(df['price'])-1]]])[0][0]
    res = [expectation + std, expectation - std]
    return res


def get_data(con, tablename, start_date, end_date):

    df = pandas.read_sql(f'SELECT * FROM \'{tablename}\' WHERE date > \'{start_date}\' AND date < \'{end_date}\'', con).set_index('index')
    return [list(df['price'].values), list(df['date'].values)]

def get_mean(con, tablename, start_date, end_date):

    df = pandas.read_sql(f'SELECT * FROM \'{tablename}\' WHERE date > \'{start_date}\' AND date < \'{end_date}\'', con).set_index('index')
    print(df['price'])
    return df['price'].mean()


def get_rsi(con, tablename, start_date, end_date):

    df = pandas.read_sql(f'SELECT * FROM \'{tablename}\' WHERE date > \'{start_date}\' AND date < \'{end_date}\'', con).set_index('index')

    up = []
    down = []
    for i in range(1, len(df['price'].values) - 1):
        diff = df['price'].values[i] - df['price'].values[i - 1]
        if (diff > 0):
            up.append(diff)
        else:
            down.append(-diff)

    print(mean(up), mean(down))
    rsi = 100 - (100/(1 + (mean(up)/mean(down))))
    return rsi