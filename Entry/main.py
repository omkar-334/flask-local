import datetime

import openpyxl
import pandas as pd
from flask import Flask, render_template, request
from openpyxl.styles import Border, Side

global message
message = "Submit to make new entry"
defdate = datetime.datetime.today().strftime("%d-%m-%Y")
file = "feescopy1.xlsx"
wb = openpyxl.load_workbook(file)
sheet = wb["Daily Fees Entry"]

cols = [1, 2, 3, 7, 13, 11]
out = pd.read_excel(io=file, sheet_name="Student Master", converters={"Cell": str, "Adm": str}, usecols=cols)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("entry.html", message=message, defdate=defdate)


@app.route("/", methods=["POST"])
def entry():
    A = sheet.max_row
    cell = "D" + str(A + 1)
    B = request.form["Date"]
    C = int(request.form["Receipt"])
    D = int(request.form["Adm"])
    E = str(request.form["FeeType"])
    F = int(request.form["FeeAmt"])
    G = ""
    H = "=IF(TRIM(" + cell + ')="","",IFERROR(INDEX(\'Student Master\'!C:C,MATCH(' + cell + ",'Student Master'!B:B,0)),\"Not Found\"))"
    I = "=IF(TRIM(" + cell + ')="","",IFERROR(INDEX(\'Student Master\'!D:D,MATCH(' + cell + ",'Student Master'!B:B,0)),\"Not Found\"))"
    J = "=IF(TRIM(" + cell + ')="","",IFERROR(INDEX(\'Student Master\'!H:H,MATCH(' + cell + ",'Student Master'!B:B,0)),\"Not Found\"))"
    K = "=IF(TRIM(" + cell + ')="","",IFERROR(INDEX(\'Student Master\'!N:N,MATCH(' + cell + ",'Student Master'!B:B,0)),\"Not Found\"))"
    L = "=IF(TRIM(" + cell + ')="","",IFERROR(INDEX(\'Student Master\'!L:L,MATCH(' + cell + ",'Student Master'!B:B,0)),\"Not Found\"))"
    M = ""
    N = ""

    sheet.append([A, B, C, D, E, F, G, H, I, J, K, L, M, N])

    border = Border(left=Side(style="thin"), right=Side(style="thin"), top=Side(style="thin"), bottom=Side(style="thin"))

    start = "A" + str(A + 1)
    end = "N" + str(A + 1)
    range = [sheet[start:end]]

    for cell in range[0]:
        for x in cell:
            x.border = border
    wb.save(filename=file)
    wb.close()
    global message
    message = "Entry Made Successfully"

    temp = out[out["Adm"] == str(D)]
    del temp["Adm"]
    temp.reset_index(inplace=True, drop=True)
    dicdef = [{"S.N.": A, "Date": B, "Receipt No.": C, "Adm": str(D), "Fee Type": E, "Fee Amount": F}]
    old = pd.DataFrame(dicdef)
    result = pd.concat([old, temp], axis=1)
    outtable = result.to_html(col_space="50px", classes="data", header="True")

    return render_template("entry.html", message=message, defdate=defdate, outtable=outtable)


if __name__ == "__main__":
    app.run()
