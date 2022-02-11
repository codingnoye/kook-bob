from flask import Flask, jsonify, render_template
import datetime as dt
import parser
import json

def get_today():
    return "2021-02-09"
    # return dt.date.today().strftime("%Y-%m-%d")

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template("index.html", data=parser.get_menu(get_today()))

@app.route('/json')
def json_menu():
    today = get_today()
    parsed = parser.get_menu(today)
    return jsonify(parsed)

if __name__ == '__main__':
    app.run(debug=True, port=5001)