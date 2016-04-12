#!flask/bin/python
from flask import Flask, jsonify
from flask import g
from flask import Response
from flask import request
import json
import MySQLdb

app = Flask(__name__)

@app.before_request
def db_connect():
  g.conn = MySQLdb.connect(host='10.0.0.7',
                              user='root',
                              passwd='Semrina77',
                              db='scheduler')
  g.cursor = g.conn.cursor()

@app.after_request
def db_disconnect(response):
  g.cursor.close()
  g.conn.close()
  return response
  
  
@app.route("/")
def hello():
  return "Hello World!"

@app.route('/rooms', methods=['GET'])  
def rooms():
  g.cursor.execute('SELECT roomid, roomname from rooms')
  rooms = g.cursor.fetchall()
  return jsonify({'rooms': rooms})
	
@app.route("/names", methods=['GET'])
def names():
  g.cursor.execute('SELECT personid, firstname, lastname from persons')
  result = g.cursor.fetchall()
  data = json.dumps(result)
  resp = Response(data, status=200, mimetype='application/json')
  return resp

if __name__ == '__main__':
    app.run(debug=True)