import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import Column, Integer, String, create_engine  # ,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import InvalidRequestError, IntegrityError
from sqlalchemy.orm import sessionmaker
import requests
import sys
import os
import json


# Flask Globals
app = Flask(__name__)
Base = declarative_base()


# Weather database structures
class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)


# SQLAlchemy ORM DataBase Globals
engine = create_engine('sqlite:///weather.db?check_same_thread=False', echo=True)
# engine = create_engine('sqlite:///weather.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
# Open Weather Map parameters
owm_api_key = 'e63b28eeee08be11f00165c9dc93acd7'
owm_geo_url = 'https://api.openweathermap.org/geo/1.0/direct'
owm_geo_pars = 'q={city}&limit=1&appid={key}'
owm_url = 'https://api.openweathermap.org/data/2.5/weather'
owm_pars = 'lat={lat}&lon={lon}&appid={key}&units=metric&lang=en'
# define SECRETKEY for flash() messages
app.config.update(SECRET_KEY=os.urandom(42))


# Given a name,state,country return Latitude and Longitude
def get_city_geo(city_name):
    geo_r = requests.get(owm_geo_url, params=owm_geo_pars.format(city=city_name, key=owm_api_key))
    if geo_r:
        if geo_r.text == '[]':
            lat = lon = 99.0
        else:
            geo_r_d = json.loads(geo_r.text[1:-1])
            if geo_r_d['name'].lower() == city_name.lower():
                lat = geo_r_d['lat']
                lon = geo_r_d['lon']
            else:
                lat = lon = 99.0
    else:
        raise RuntimeWarning
    return (lat, lon)


# return dictionary of current weather for city at specified Latitude and Longitude
def get_city_weather(lat, lon):
    w_r = requests.get(owm_url, params=owm_pars.format(lat=lat, lon=lon, key=owm_api_key))
    if w_r:
        return json.loads(w_r.text)
    else:
        raise RuntimeWarning


# process view request of main html index
@app.route('/', methods=['GET', 'POST'])
def index():
    city_weather_list = []  # initially empty list of weather dictionaries
    if request.method == 'GET':
        # get list of cities from weather.db and form a dictionary structure for rendering
        query = session.query(City)                 # create a query object
        all_rows = query.all()                      # read all rows
        for row in all_rows:                        # from each row, get...
            city_name = row.name                    # Name of next city
            c_lat, c_lon = get_city_geo(city_name)  # GeoLocate that city...
            w_r_d = get_city_weather(c_lat, c_lon)  # get the current weather from OWM
            weather_l = w_r_d['weather']            # massage it...
            weather_d = weather_l[0]
            city_weather_d = {'city': city_name, 'degrees': int(w_r_d["main"]["temp"]), 'state': weather_d["main"]}
            city_weather_list.append(city_weather_d)
        return render_template('index.html', weather=city_weather_list)
    elif request.method == 'POST':
        # process POST request for a new city
        city_name = request.form["city_name"]       # get city Name,State,Country from HTML form
        if len(city_name) == 0:
            return redirect(url_for('index'))       # Nothing entered? Just return to main page...
        city_lat, city_lon = get_city_geo(city_name)  # GeoLocate that city...
        if city_lat > 90.0:
            flash("The city doesn't exist!")        # geolocate city_name failed??
            return redirect(url_for('index'))       # recycle...
        w_r_d = get_city_weather(city_lat, city_lon)  # Get current weather at that location
        city_id = w_r_d["id"]                       # including CityID
        try:                                        # and safely write a City record
            session.add(City(id=city_id, name=city_name))
            session.commit()
        except InvalidRequestError as message:
            print("Error writing to city.db:", message)
            session.rollback()
        except IntegrityError as message:
            flash("The city has already been added to the list!")
            print("sqlite integrity error: Duplicate key: ", message)
            session.rollback()
        except sqlite3.ProgrammingError as message:
            print("SQLAlchemy Programming error:", message)
            session.rollback()
        return redirect(url_for('index'))           # Always redirect back to the main page


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    d_query = session.query(City)
    d_city = d_query.filter_by(name=id).first()
    try:
        session.delete(d_city)
        session.commit()
    except InvalidRequestError as message:
        print("Error deleting from city.db:", message)
        session.rollback()
    return redirect(url_for('index'))


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
