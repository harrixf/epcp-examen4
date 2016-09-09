# coding=utf-8

import os
import csv
from flask import Flask
from flask import render_template
app = Flask(__name__, static_url_path='')

    #carga de csv
csv_path = './static/serie.csv'
datos = list(csv.reader(open(csv_path, 'r')))

    #rutas
@app.route("/")
def index():
    return render_template('index.html',
        tabla=datos
    )

    # solo para cloud9
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8000,
        use_reloader=True,
        debug=True,
    )