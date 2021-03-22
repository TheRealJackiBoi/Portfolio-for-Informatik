from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
app.config['SECRET_KEY'] = 'GOSay1LoveChu'

@app.route('/',methods=['GET','POST'])
def home():
    
    return render_template('index.html')


@app.route('/opgaver',methods=['GET','POST'])
def opgaver():

   return render_template('opgaver.html')

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




@app.route('/kontakt',methods=['GET','POST'])
def kontakt():

   return render_template('kontakt.html')


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=8080,debug=True)