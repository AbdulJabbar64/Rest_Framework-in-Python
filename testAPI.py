import json
from unicodedata import name
import requests

URL = "http://127.0.0.1:8000/stud/"

def get_data(id=None):
    data = {"id":None}
    if id is not None:
        data = {"id":id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    print(r.json())

# get_data(4)

def post_data():
    data = {
        "name":"abc",
        "roll":64,
        "city":"city123"
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data= json_data)
    print(r.json())

# post_data()

def update_data():
    data = {
        "id":4,
        "name":"xyz",
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data= json_data)
    print(r.json())

# update_data()
# get_data(4)

def delete_data():
    data = {
        "id":4
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data= json_data)
    print(r.json())

# delete_data()
get_data()
