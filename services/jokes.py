import requests

r = requests.get('http://api.icndb.com/jokes/random?limitTo=[nerdy]').json()
if r['type'] == 'success':
    print(r['value']['joke'])
else:
    print('I am so busy fetching jokes for you that I forgot to connect to Internet')
