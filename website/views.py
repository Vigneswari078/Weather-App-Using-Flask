from flask import Blueprint,render_template,request
import requests
views = Blueprint('views',__name__)
from datetime import datetime
from .config import API_KEY

@views.route('/',methods=['GET','POST'])
def home():
    weatherlist=[]
    if(request.method=="POST"):
        city = request.form.get('city')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
        r = requests.get(url.format(city)).json()
        print(r)
        date_time = datetime.now()
        weather = {
            'city' : city,
            'temp' : int(r['main']['temp']),
            'desc' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'feels_like' : int(r['main']['feels_like']),
            'temp_max' : int(r['main']['temp_max']),
            'temp_min' : int(r['main']['temp_min']),
            'datetime' : date_time.strftime("%a %d %B %H:%M%p")
        }
        weatherlist.append(weather)
    return render_template("weather.html",weatherlist=weatherlist)

