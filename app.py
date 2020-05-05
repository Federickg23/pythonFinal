# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
Name: Federick Gonzalez
Uni:  fag2113

"""

# import statements
import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Flask app variable
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


# static route
@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template("index.html")


@app.route("/1006")
def classPage():
    return render_template("1006.html")


@app.route("/weather", methods=['GET', 'POST'])
def weatherInfo():
    if request.method == 'POST':
        new_city = request.form.get('city')
        if new_city:
            new_city_obj = City(name=new_city)
            db.session.add(new_city_obj)
            db.session.commit()
    cities = City.query.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=ea56b0b34d21c36bb2d730ae0da1c52e'
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city.name)).json()
        weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(weather)

    return render_template('weather.html', weather_data=weather_data)

@app.route("/Wushu", methods=['GET', 'POST'])
def wushu():
    return render_template("wushu.html")
    pass


# start the server
if __name__ == "__main__":
    app.run()
