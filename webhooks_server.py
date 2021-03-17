from flask import Flask, request, Response
import logging
import numpy

app = Flask(__name__)
if __name__ == '__main__':
    app.run()
    
@app.route('/', methods=['POST'])
def respond():
    print('get')
    print(request.json)
    return "<h1>Welcome to our server !!</h1>"


@app.route('/', methods=['GET'])
def index():
	return "<h1>Welcome to our server !!</h1>"