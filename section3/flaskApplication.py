from flask import Flask 

app = Flask(__name__)
@app.route('/')

def homie():
    return "Hello Thuss Thuss"

app.run(port=5000)