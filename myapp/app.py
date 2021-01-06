from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY'] = 'GOSay1LoveChu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/',methods=['GET','POST'])
def home():
    
    return render_template('index.html')


@app.route('/opgaver',methods=['GET','POST'])
def opgaver():

   return render_template('opgaver.html')

@app.route('/emner',methods=['GET','POST'])
def emner():

   return render_template('emner.html')

@app.route('/kontakt',methods=['GET','POST'])
def kontakt():

   return render_template('kontakt.html')


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=8080,debug=True)