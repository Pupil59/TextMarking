import requests, pprint

data = {
    "action": "del_relation",
    "id": 4,
}

response = requests.delete('http://127.0.0.1:8000/api/relations',
                           json=data)

pprint.pprint(response.json())

response = requests.get('http://127.0.0.1:8000/api/relations?action=list_relation')

pprint.pprint(response.json())
