from urllib.parse import quote_plus
import sys

sys.argv.pop(0)
if len(sys.argv) >= 1:
    print(quote_plus(" ".join(sys.argv)))
else:
    print('lmgtfy')
