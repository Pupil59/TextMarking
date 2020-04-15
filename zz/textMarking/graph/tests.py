import requests, pprint

response = requests.get('http://127.0.0.1:8000/api/graph')

pprint.pprint(response.json())

# response = requests.get('http://127.0.0.1:8000/api/relations?action=list_relation')
#
# pprint.pprint(response.json())
