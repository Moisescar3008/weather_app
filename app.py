from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#configurations of the api
API_KEY = '6049ef654f9da42330a26a29ce07b3bf'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather',methods=['POST'])
def get_weather():
    city = request.form['city']
    url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=es'
    response = requests.get(url)

    if response.status_code==200:
        data = response.json()
        weather = {
            'city':data['name'],
            'temperature':data['main']['temp'],
            'description':data['weather'][0]['description'],
            'icon':data['weather'][0]['icon']
        }
        return render_template('result.html',weather=weather)
    else:
        error_message = "City not found"
        return render_template('index.html',error=error_message)
    
if __name__=="__main__":
    app.run(debug=True)