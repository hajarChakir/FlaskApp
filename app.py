from flask_mysqldb import MySQL
from flask import Flask, render_template, request, jsonify, url_for, flash
import logging as logger

from werkzeug.utils import redirect


logger.basicConfig(level="DEBUG")
import pymysql
import mysql.connector

app = Flask(__name__)
app.secret_key = 'flash messages'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3308
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'data'
mysql = MySQL(app)

@app.route('/select')
def select():
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM movies"
    cursor.execute(query)
    data = cursor.fetchall()
    resp = jsonify(data)
    resp.status_code = 200
    return resp
    cursor.close()

@app.route('/insert',methods=['POST'])
def insert():
    if request.method=="POST":
        Title=request.form['Title']
        ReleaseYear = request.form['ReleaseYear']
        Rank = request.form['Rank']
        Rating = request.form['Rating']
        Url = request.form['Url']
        Image = request.form['Image']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO movies (Title,ReleaseYear,Rank,Rating,Url,Image) VALUES (%s,%s,%s,%s,%s,%s)",(Title,ReleaseYear,Rank,Rating,Url,Image))
        flash("Data Inserted Successfully")
        mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method=="POST":
        id_data=request.form["id"]
        Title = request.form['Title']
        ReleaseYear = request.form['ReleaseYear']
        Rank = request.form['Rank']
        Rating = request.form['Rating']
        Url = request.form['Url']
        Image = request.form['Image']

        cursor = mysql.connection.cursor()
        cursor.execute("""update movies 
            SET Title=%s,ReleaseYear=%s,Rank=%s,Rating=%s,Url=%s,Image=%s 
            WHERE id=%s
            """,(Title,ReleaseYear,Rank,Rating,Url,Image,id_data))

        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('index'))


@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM movies WHERE id=%s", (id_data))
    mysql.connection.commit()
    return redirect(url_for('index'))


@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT* from movies")
    data=cursor.fetchall()
    cursor.close()
    return render_template("index.html",movies=data)
if __name__ == '__main__':
    app.run()