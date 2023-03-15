from flask import Flask, render_template
app = Flask(__name__)

import datetime

@app.route('/')

def index():
  return render_template("città3.html", Ora=datetime.datetime.utcnow())


@app.route('/descrizioni')

def descrizioni():
  return render_template("città2.html", Ora=datetime.datetime.utcnow())

if __name__ == '__main__':#sempre alla fine queste due righe
  app.run(host='0.0.0.0', port=3245, debug=True)#sempre alla fine queste due righe