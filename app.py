from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# 🔗 Connect MySQL (edit these according to your phpMyAdmin)
mydb = mysql.connector.connect(
    host="localhost",    # or your host name
    user="root",         # phpMyAdmin username
    password="gautamlocalhost9812",         # password (if any)
    database="biodata_db"
)

cursor = mydb.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    email VARCHAR(100),
    bio TEXT
)
""")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/userdata', methods=['GET', 'POST'])
def userdata():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        bio = request.form['bio']

        cursor.execute("INSERT INTO users (name, age, email, bio) VALUES (%s, %s, %s, %s)", (name, age, email, bio))
        mydb.commit()
        return redirect('/')
    return render_template("userdata.html")

if __name__ == '__main__':
    app.run(debug=True)
