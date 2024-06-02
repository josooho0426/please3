
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run()


import pymysql

db = pymysql.connect(host="localhost",user="root",passwd="1234",db="myboard", charset="utf8")
cur =db.cursor()

sql ="SELECT * FROM board"
cur.execute(sql)

data_list = cur.fetchall()

print(data_list[0])


