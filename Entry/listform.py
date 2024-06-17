import datetime

from flask import Flask, redirect, render_template, request

defdate = datetime.datetime.today().strftime("%d-%m-%Y")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("new.html")


@app.route("/", methods=["GET", "POST"])
def div():
    values = request.values
    Adm = list((values.getlist("Adm")))
    Date = list(values.getlist("Date"))
    FeeAmt = list(values.getlist("FeeAmt"))
    Receipt = list(values.getlist("Receipt"))
    print("Adm - ", Adm)
    print("Date - ", Date)
    print("FeeAmt - ", FeeAmt)
    print("Receipt - ", Receipt)

    return render_template("new.html")


if __name__ == "__main__":
    app.run(port=2000)
