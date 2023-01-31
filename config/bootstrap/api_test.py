from urllib.request import urlopen, Request
import json

url = "https://ice-cream-factory.inso-internal.cognite.ai/site/oslo"
hdr = {
     "-H 'accept: application/json'"
}
req = Request(url)
req.get_method = lambda: 'GET'
try:
    response = urlopen(req)
except Exception as e:
    print(e.code)
result = json.loads(response.read().decode('utf-8'))
for asset in result:
    print (asset)
print("total = ",len(result))
