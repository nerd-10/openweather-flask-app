# Flask Weather App

A simple Flask web application that fetches **real-time weather data** using the **OpenWeather API**.

Users can search any city and view:

- Weather description
- Temperature (°C)
- Feels like temperature
- Humidity
- Wind speed
- Weather icon

---

## Features

- Search weather by city name
- Weather icon display from OpenWeather
- Input persistence (keeps last searched city)
- Error handling:
  - Empty input
  - Invalid city name
- Clean UI using HTML + CSS
- Uses `.env` file to protect API key
- Production server support using Waitress

---

## Tech Stack

- Python
- Flask
- OpenWeather API
- HTML, CSS (Jinja Templates)
- Requests
- Python-dotenv
- Waitress

---

## Project Structure

```txt
flask_openweather/
├── fserver.py
├── weather.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── weather.html
│   └── city_notfound.html
│
└── static/
    └── styles/
        └── style.css
```

## Setup Instructions

-git clone [[https://github.com/nerd-10/openweather-flask-app]
-cd flask_openweather
-pip install -r requirements.txt
-API_KEY=your_openweather_api_key_here
-python fserver.py

