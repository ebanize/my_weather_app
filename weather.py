#import requests

#api_key = '090f8c0452deaf1ca4e65aec8b052777'

#user_input = input("Enter city:")

#weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")   

#weather = weather_data.json()['weather'][0]['main']
#temp = round(weather_data.json()['main']['temp'])



#print(f"The weather {user_input} is: {weather}")
#print(f"The temperature in {user_input} is: {temp}°F")



import requests

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

user_input = input("Enter city:")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")   

weather = weather_data.json()['weather'][0]['main']
temp_fahrenheit = round(weather_data.json()['main']['temp'])
temp_celsius = round(fahrenheit_to_celsius(temp_fahrenheit), 2)

print(f"The weather in {user_input} is: {weather}")
print(f"The temperature in {user_input} is: {temp_fahrenheit}°F / {temp_celsius}°C")
