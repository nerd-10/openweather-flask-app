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

```bash
# 1) Clone the repository
git clone https://github.com/nerd-10/openweather-flask-app.git
cd openweather-flask-app

# 2) Install dependencies
pip install -r requirements.txt

# 3) Create a .env file in the project root and add your API key
# API_KEY=your_openweather_api_key_here

# 4) Run the app
python fserver.py


```
