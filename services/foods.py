import sys

foods = {
    'samosa': ['C3'],
    'sandwich': ['Yummpys', 'C3', 'Bits & Bytes', 'ANC 1', 'ANC 2'],
    'rice': ['ANC 1', 'ANC 2', 'Mess 1', 'Mess 2'],
    'noodles': ['Yummpys', 'ANC 1', 'ANC 2'],
    'paratha': ['Mess 1', 'Mess 2', 'C3']
}
if len(sys.argv) == 2:
    for food in foods:
        if food == sys.argv[1].lower():
            print('{} is available in the following eateries||'.format(sys.argv[1].title()), end='')
            for eatery in foods[food]:
                print('{}||'.format(eatery), end='')
            exit(0)
    print('This food is not available')
else:
    print('Wrong command')
