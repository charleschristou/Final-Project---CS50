# import flask from the flask library, along with render_template and request
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from helpers import lookup, onedp, feel, rain, wind
from datetime import datetime, timedelta
import emoji

# tells python to create an app from the template. we give the Flask class the name of the current Python file
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Custom filter for Jinja
app.jinja_env.filters["onedp"] = onedp

app.config["FLASK_DEBUG"] = 1

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#define default route for index
@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method=="GET":
        return render_template("index.html")

@app.route("/weather", methods=["GET","POST"])
def weather():

    if request.method=="GET":
        return render_template("index.html")
    
    if request.method=="POST":
        location = request.form.get("location")
        timesteps = request.form.get("timesteps")
        weather = lookup(location, timesteps)
        
        if weather == None:
            flash('Location could not found, try enterting a US/UK postcode, co-ordinates, or location name')
            return render_template("index.html")
  

        #  get time range to pass to weather.html 

        if timesteps == "1d":
            today = datetime.today()
            date_range = []
            for time in range(len(weather["values"])):
                date_range.append((today + timedelta(days=time)).strftime('%d-%m-%Y'))
        elif timesteps == "1h":
            today = datetime.today()
            date_range = []
            time = 0
            while time < 25:
                date_range.append((today + timedelta(hours=time)).strftime('%H:%M'))
                time += 1

        # determine length of time

        times = len(date_range)

        # create a list of the heat emojis

        looks = []
        for time in weather["values"]:
            j = feel(weather["values"][time]["avg_temp"])
            looks.append(j)

        # create a list for the rain emojis

        rains = []
        for time in weather["values"]:
            i = rain(weather["values"][time]["precipitation"])
            rains.append(i)

        # wind emojis

        winds = []

        # convert meters/second to mph for wind for convention and emojis

        for time in weather["values"]:
            i = weather["values"][time]["avg_wind_speed"] * 2.23694
            winds.append(wind(i))
            weather["values"][time]["avg_wind_speed"] = i

        #render template

        return render_template("weather.html", weather=weather, date=date_range, looks=looks, rains=rains, winds=winds, times=times)
