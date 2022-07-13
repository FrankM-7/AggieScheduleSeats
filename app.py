from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return { 'data' : 'data'}

@app.route("/something")
def something():
    return { 'somedata' : [{'some' : 'data'}, {'some' : 'otherdata'}] }