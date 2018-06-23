import requests
from random import randint

start = 1
end = 1944
comic_no = randint(start, end)
comic_url = 'https://xkcd.com/{}/info.0.json'.format(comic_no)
output = requests.get(comic_url)

print('IMG_URL:{}'.format(output.json()['img']))
