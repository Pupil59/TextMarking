import requests, pprint

# data = {
#     "action": "del_entity",
#     "id": 3,
# }
#
# response = requests.delete('http://127.0.0.1:8000/api/entities',
#                            json=data)
#
# pprint.pprint(response.json())

response = requests.get('http://127.0.0.1:8000/api/entities?action=list_entity')

pprint.pprint(response.json())

response = requests.get('http://127.0.0.1:8000/api/relations?action=list_relation')

pprint.pprint(response.json())
