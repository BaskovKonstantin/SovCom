from flask import Flask, jsonify
from flask_cors import CORS
from script.predict import get_predict
from script.predict import get_data
from script.predict import get_rsi
from script.predict import get_mean
from script.update import update_db
from threading import Thread
import sqlite3
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__)
con = sqlite3.connect('data\\data', check_same_thread=False)

th = Thread(target = update_db, args = (con, ))
th.start()

@app.route('/mean/<string:table>/<string:start_date>/<string:end_date>', methods=['GET'])
def mean(table, start_date, end_date):

    json = jsonify(get_mean(con, table, start_date, end_date))
    json.headers.add("Access-Control-Allow-Origin", "*")
    return json

@app.route('/rsi/<string:table>/<string:start_date>/<string:end_date>', methods=['GET'])
def rsi(table, start_date, end_date):

    json = jsonify(get_rsi(con, table, start_date, end_date))
    json.headers.add("Access-Control-Allow-Origin", "*")
    return json

@app.route('/data/<string:table>/<string:start_date>/<string:end_date>', methods=['GET'])
def data(table, start_date, end_date):
    json = jsonify(get_data(con, table, start_date, end_date))
    json.headers.add("Access-Control-Allow-Origin", "*")
    return json

@app.route('/predict/<string:table>/<string:start_date>/<string:end_date>', methods=['GET'])
def predict(table, start_date, end_date):

    json = jsonify(get_predict(con, table, start_date, end_date))
    json.headers.add("Access-Control-Allow-Origin", "*")
    return json

@app.route('/')
def hello_world():
    json = jsonify({'POP':'IT'})
    json.headers.add("Access-Control-Allow-Origin", "*")
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
