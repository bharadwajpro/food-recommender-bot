import requests

appToken = 'b26764d904b793dd9eee2dceeaf7c7b1'
output = requests.get('http://api.openweathermap.org/data/2.5/weather', params={
            'lat': '17.5443294',
            'lon': '78.5697066',
            'appid': appToken
})
weather = output.json()
print('Weather: <b>{}</b>||'.format(weather['weather'][0]['main']), end='')
print('Current Temperature: <b>{} C</b>||'.format(round(weather['main']['temp'] - 273, 2)), end='')
print('Max Temperature: <b>{} C</b>||'.format(round(weather['main']['temp_max'] - 273, 2)), end='')
print('Min Temperature: <b>{} C</b>||'.format(round(weather['main']['temp_min'] - 273, 2)), end='')
print('Pressure: <b>{} hPa</b>||'.format(weather['main']['pressure']), end='')
print('Humidity: <b>{}%</b>||'.format(weather['main']['humidity']), end='')
