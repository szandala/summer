import requests
import json




def get_key():
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    data = {"email":"summerschool@pwr.edu.pl","password":"B2258DC7D28407B694B5EE69382F568A728C1B0A5FEB56EAD8F4D51AE572A909"}

    response = requests.post('http://tw.thaumatec.com:8104/api/authenticate', headers=headers, data=json.dumps(data))

    print(response.status_code)
    print(response.json())

def get_motes_


get_key()
