from flask import Flask,render_template
import subprocess
import webbrowser
app = Flask(__name__)

@app.route('/')
def index():
   global cmarks
   global cfees
   cmarks="Run"
   cfees="Run"
   return render_template('default.html',cmarks=cmarks,cfees=cfees)

@app.route('/marks')
def marks():
   global cmarks
   global cfees
   if cmarks=="Run":
      try:
         subprocess.run("python Marks/main.py", shell=True,timeout=15)
      except:
         cmarks="Launch"
         webbrowser.open('http://127.0.0.1:2000')
   else:
      webbrowser.open('http://127.0.0.1:2000')
   return render_template('default.html',cmarks=cmarks,cfees=cfees)

@app.route('/fees')
def fees():
   global cmarks
   global cfees
   if cfees=="Run":
      try:
         subprocess.run("python Fees/main.py", shell=True,timeout=15)
      except:
         cfees="Launch"
         webbrowser.open('http://127.0.0.1:5000')
   else:
      webbrowser.open('http://127.0.0.1:5000')

   return render_template('default.html',cfees=cfees,cmarks=cmarks)

if __name__ == '__main__':
   app.run(port=8001)