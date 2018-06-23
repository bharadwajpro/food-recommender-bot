import datetime

eateries = {
    'Yummpys': {
        'open': 10,
        'close': 25
    },
    'Mess 1, Mess 2 ANC': {
        'open': 22,
        'close': 25
    },
    'Bits & Bytes': {
        'open': 11,
        'close': 21
    },
    'C3': {
        'open': 17,
        'close': 24
    },
    'Mess 1, Mess 2': {
        'open': 7,
        'close': 20
    },
    'CP': {
        'open': 9,
        'close': 20
    },
}

current_hr = datetime.datetime.now().hour

print('These eateries are open at this time||', end='')
x = 1
for eatery in eateries:
    if current_hr <= 3:
        current_hr += 24
    if eateries[eatery]['open'] <= current_hr <= eateries[eatery]['close']:
        print('{}. {}||'.format(x, eatery), end='')
        x += 1
