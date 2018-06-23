import datetime
import sys

eateries = {
    'Yummpys': {
        'open': 10,
        'close': 25,
    },
    'ANC 1': {
        'open': 22,
        'close': 25,
    },
    'ANC 2': {
        'open': 22,
        'close': 25,
    },
    'Bits & Bytes': {
        'open': 11,
        'close': 21
    },
    'C3': {
        'open': 17,
        'close': 24
    },
    'Mess 1': {
        'open': 7,
        'close': 20
    },
    'Mess 2': {
        'open': 7,
        'close': 20
    },
    'CP': {
        'open': 9,
        'close': 20
    },
}


current_hr = datetime.datetime.now().hour

if len(sys.argv) == 1:
    print('These eateries are open at this time||', end='')
    x = 1
    for eatery in eateries:
        if current_hr <= 3:
            current_hr += 24
        if eateries[eatery]['open'] <= current_hr <= eateries[eatery]['close']:
            print('{}. {}||'.format(x, eatery), end='')
            x += 1
elif len(sys.argv) == 2:
    for eatery in eateries:
        if sys.argv[1] == eatery:
            if current_hr <= 3:
                current_hr += 24
            if eateries[eatery]['open'] <= current_hr <= eateries[eatery]['close']:
                print('Yes, {} is open now'.format(sys.argv[1]))
            else:
                print('Sorry, {} is closed now'.format(sys.argv[1]))
            exit(0)
    print('Eatery doesn\'t exists in BPHC')
