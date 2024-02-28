#!/usr/bin/python3 

import requests
import sys

def get_employee_info(employee_id):
    """Get the endpoint"""
    employee_url = "https://jsonplaceholder.typicode.com/users/{}"
    employee_response = requests.get(employee_url.format(employee_id))
     
    """ if staus code is correct get employee details"""
    if employee_response.status_code == 200:
        employee_details = employee_response.json()
        employee_name = employee_details['name']
    else: 
        print(f"Failed to retrieve employee's details:{employee_response.status_code}")
        return None
    
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    

    if todo_response.status_code == 200:
        todo_data = todo_response.json()
    else:
        print(f"Failed to retrieve employee's todos:{employee_response.status_code}")
        return None
    
    # employee_name = employee_details['name']
    completed_tasks = sum(todo['completed'] for todo in todo_data)
    number_of_done_tasks = completed_tasks
    total_number_of_tasks = len(todo_data)
    
    print(f"Employee {employee_name} is done with tasks {number_of_done_tasks}/{total_number_of_tasks}:")
    for task in todo_data:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)  # Exit with an error code
    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)








    






