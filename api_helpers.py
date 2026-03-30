import json
from urllib.request import urlopen, Request
from urllib.error import HTTPError

def get_json(url, headers=None):
    req = Request(url, headers=headers or {})
    try:
        with urlopen(req) as response:
            return json.loads(response.read().decode())
    except HTTPError as e:
        return {'error': str(e), 'status': e.code}

def post_json(url, data, headers=None):
    headers = headers or {}
    headers['Content-Type'] = 'application/json'
    req = Request(url, data=json.dumps(data).encode(), headers=headers, method='POST')
    try:
        with urlopen(req) as response:
            return json.loads(response.read().decode())
    except HTTPError as e:
        return {'error': str(e), 'status': e.code}
