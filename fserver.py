from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/weather',methods=["GET","POST"])
def get_weather():
    if request.method == "POST":
        city = request.form.get("city")
        #check for empty string or empty spaces
        if not bool(city.strip()):
            city = "New Delhi" 
    else:
        city = request.args.get("city")
        ##check for empty string or empty spaces
        if not city:
            return render_template("index.html", error="Please type a city name.")
  
    weather_data = get_current_weather(city)
    #city is not found by api
    if str(weather_data.get("cod")) != "200":
        return render_template("city_notfound.html", city=city, error="Please enter a valid city name.")
    

    return render_template(
        "weather.html",city=city,
        title=weather_data["name"],
        status=weather_data["weather"][0]['description'].capitalize(),
        temp=(f"{weather_data['main']['temp']:.1f}"),
        weather_icon=weather_data["weather"][0]["icon"],
        feels_like=(f"{weather_data['main']['feels_like']:.1f}"),
        humidity=(f"{weather_data['main']['humidity']}"),
        wind_speed=(f"{weather_data['wind']['speed']:.1f}")
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)