#!/usr/bin/python3 
"""
this is a python file that export it's data to json"""

import json
import requests
import sys

def get_export_json(user_id):
    """Get the endpoint"""
    employee_url = "https://jsonplaceholder.typicode.com/users/{}"
    employee_response = requests.get(employee_url.format(user_id))
     
    #  if status code is correct get employee details
    if employee_response.status_code == 200:
        employee_details = employee_response.json()
        username = employee_details['username']

    else: 
        print(f"Failed to retrieve employee's details:{employee_response.status_code}")
        return None
    
    todo_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todo_response = requests.get(todo_url)
    

    if todo_response.status_code == 200:
        todo_data = todo_response.json()
    else:
        print(f"Failed to retrieve employee's todos:{employee_response.status_code}")
        return None
        
    
    employee_tasks = []
    for task in todo_data:
        employee_tasks.append({"USER_ID": [{
            "task": task['title'],
            "completed": task['completed'],
            "username": username,
        }]})
        

    json_filename = f"{user_id}.json"
    with open(json_filename, "w") as json_file:
        json.dump(employee_tasks, json_file, indent=2)

    print(f"the json file {json_filename} has been created using {user_id}")
       


if __name__ == "__main__":
    if len(sys.argv) > 2:
         user_id = int(sys.argv[1])
    else:
      user_id = 2
      get_export_json(user_id)










    



