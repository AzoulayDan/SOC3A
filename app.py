#-*- encoding:utf-8 -*-
<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask 
>>>>>>> 76fb39f0ccc97dde3e6d91a160c193ffe31efd99
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)

@app.route('/')
def index():
	return 'hello world'

if __name__ == '__main__':
<<<<<<< HEAD
	app.run()
=======
	app.run()
>>>>>>> 76fb39f0ccc97dde3e6d91a160c193ffe31efd99
