import requests
import json
import logging
from functools import reduce


# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

headers = {
    "Accept": "application/vnd.docker.distribution.manifest.v2+json"
}

response = requests.get("http://localhost:5000/v2/lib/nginx/manifests/1.9", headers=headers)

image_json = response.json()
print response.content

sizes = [ layer['size'] for layer in image_json['layers']]
print reduce((lambda x, y: x + y), sizes)

