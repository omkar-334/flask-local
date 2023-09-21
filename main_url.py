from flask import Flask,render_template
import subprocess
import webbrowser
import urllib.request as uqt
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('default.html')

@app.route('/marks')
def marks():
    try:
        subprocess.run("python Marks/main.py", shell=True,timeout=1)
    except:
        code=0
    while code!=200:
        try:
            code=uqt.urlopen("http://127.0.0.1:2000").getcode()
        except:
            code=0
    if code==200:
        webbrowser.open('http://127.0.0.1:2000')
    return render_template('default.html')

@app.route('/fees')
def fees():
    try:
        subprocess.run("python Fees/main.py", shell=True,timeout=1)
    except:
        code=0
    while code!=200:
        try:
            code=uqt.urlopen("http://127.0.0.1:5000").getcode()
        except:
            code=0
    if code==200:
        webbrowser.open('http://127.0.0.1:5000')
    return render_template('default.html')

if __name__ == '__main__':
   app.run(port=8001)