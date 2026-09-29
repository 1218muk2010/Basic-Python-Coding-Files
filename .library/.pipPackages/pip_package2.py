import requests
import sys

if len(sys.argv) != 1:
    sys.exit()
else:
    response = requests.get("https://open.spotify.com/search/" + sys.argv[1])
    print(response.json())


