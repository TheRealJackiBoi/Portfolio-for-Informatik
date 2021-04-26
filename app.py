from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
app.config['SECRET_KEY'] = 'GOSay1LoveChu'

@app.route('/',methods=['GET','POST'])
def home():
    
    return render_template('index.html')


@app.route('/eksamen',methods=['GET','POST'])
def eksamen():
   return render_template('eksamen.html')

@app.route('/emner',methods=['GET','POST'])
def emner():

   return render_template('emner.html',)

#subpages af emner
@app.route("/emner/laeringsspil")
def laeringsspil():
   return render_template('/Emner/laeringsspil.html',)

@app.route("/emner/hjemmesider")
def hjemmesider():
   return render_template('/Emner/hjemmesider.html',)

@app.route("/emner/aarsprove")
def aarsprove():
   return render_template('/Emner/aarsprove.html',)

@app.route("/emner/arduino_tog")
def arduino_tog():
   return render_template('/Emner/arduino-tog.html',)

@app.route("/emner/arduino_projekt")
def arduino_projekt():
   return render_template('/Emner/arduino_projekt.html',)

@app.route("/emner/beamrobot")
def beamrobot():
   return render_template('/Emner/beamrobot.html',)

@app.route("/emner/big_data")
def big_data():
   return render_template('/Emner/bigdata.html',)

@app.route("/emner/corona_app")
def corona_app():
   return render_template('/Emner/corona_app.html',)

@app.route("/emner/databaser")
def databaser():
   return render_template('/Emner/databaser.html',)

@app.route("/emner/HMI")
def HMI():
   return render_template('/Emner/HMI.html',)

@app.route("/emner/prolog")
def prolog():
   return render_template('/Emner/prolog.html',)


@app.route('/kontakt',methods=['GET','POST'])
def kontakt():

   return render_template('kontakt.html')


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=8080,debug=True)