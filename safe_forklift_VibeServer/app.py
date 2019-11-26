import sqlite3

from flask import Flask, url_for, render_template, request, redirect, session
import json
import socket

app = Flask(__name__)
app.secret_key = 'We are Fried Chicken Dinner!!!!'

@app.route("/", methods=['GET', 'POST'])
def doorLock():
    if request.method == 'POST':
        returnjson = request.get_json(silent=True, cache=False, force=True)
        if returnjson['code'] == 'b':
            return render_template("matrix_back.html")
        elif returnjson['code'] == 'r':
            return render_template('matrix_right.html')
        elif returnjson['code'] == 'l':
            return render_template("matrix_left.html")

        return str(returnjson)
    if request.method == 'GET':
        return 'test'
def DBinit():
    conn = sqlite3.connect("test.db")
    curs = conn.cursor()
    curs.execute("DROP TABLE IF EXISTS User")
    curs.execute("CREATE TABLE if not exists User(Student_ID, Name);")
    conn.commit()
    curs.close()
    conn.close()

    conn = sqlite3.connect("fileLogDB.db")
    curs = conn.cursor()
    curs.execute("CREATE TABLE  if not exists fileLogDB(username, time, file)")
    conn.commit()
    curs.close()
    conn.close()

    conn = sqlite3.connect("test.db")
    curs = conn.cursor()
    curs.execute("select*from User")
    curs.execute("INSERT INTO user(Student_ID,Name) VALUES("    +  '20178999'  + "," + "'testdata'" + ")")
    conn.commit()
    curs.close()
    conn.close()

if __name__ == '__main__':
    IP = str(socket.gethostbyname(socket.gethostname()))
    app.run(host="192.168.0.6", port=9090, debug=True)
