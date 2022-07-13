from flask import Flask, request

app = Flask(__name__)

@app.route("/something")
def something():
    return { 'somedata' : [{'some' : 'data'}, {'some' : 'otherdata'}] }