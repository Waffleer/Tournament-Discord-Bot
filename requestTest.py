import json
import requests

resp = requests.get('http://127.0.0.1:9101/genServer?user=testUser&serverName=Bacon')
respDict = json.loads(resp.text)

print(resp.text)