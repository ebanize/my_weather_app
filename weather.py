
# THE BEGINING OF NEW LINE OF CODES 

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.

    Returns:
    float: Temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

api_key = '090f8c0452deaf1ca4e65aec8b052777'

@app.route('/weather', methods=['GET'])
def get_weather():
    user_input = request.args.get('city')
    if not user_input:
        return jsonify({'error': 'City parameter is required'}), 400
    
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
    
    if weather_data.status_code != 200:
        return jsonify({'error': 'City not found'}), 404

    weather = weather_data.json()['weather'][0]['main']
    temp_fahrenheit = round(weather_data.json()['main']['temp'])
    temp_celsius = round(fahrenheit_to_celsius(temp_fahrenheit), 2)

    return jsonify({
        'city': user_input,
        'weather': weather,
        'temperature': {
            'fahrenheit': f"{temp_fahrenheit}°F",
            'celsius': f"{temp_celsius}°C"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



