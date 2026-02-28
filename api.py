import requests

url = "https://api.freeapi.app/api/v1/todos/"

def create_todo(payload):
    response = requests.post(url, data=payload).json()
    
    return response["message"]

def get_todos():
    response = requests.get(url+"?query=python&complete=false").json()
    
    return response["data"]

def get_todo(id):
    response = requests.get(url+id).json()
    
    return response["data"]

def update_todos(id, payload):
    response = requests.put(url+id, data=payload)
    
    return response

def delete_todo(id):
    response = requests.delete(url+id).json()
    
    return response["message"]



operation = input("Enter operation: ")

if operation == "c":
    title = input("Enter title: ")
    description = input("Enter description: ")
    response = create_todo({"description": description, "title": title})
elif operation == "u":
    id = input("Enter id: ")
    title = input("Enter title: ")
    description = input("Enter description: ")
    response = update_todos(id, {"description": description, "title": title})
elif operation == "g":
    response = get_todos()
elif operation == "p":
    id = input("Enter id: ")
    response = get_todo(id)
elif operation == "d":
    id = input("Enter id: ")
    response = delete_todo(id)

print(response)