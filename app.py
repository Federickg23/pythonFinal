# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
Name: Federick Gonzalez
Uni:  fag2113

"""

#import statements
import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#Flask app variable
app = Flask(__name__)

#static route
@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template("index.html")

@app.route("/1006")
def classPage():
    return render_template("1006.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

#start the server
if __name__ == "__main__":
    app.run()

