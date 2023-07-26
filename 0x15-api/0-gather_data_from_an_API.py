#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


def get_employee_todo_list(employee_id):
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = request.get(url)
    if response.status_code == 200:
        employee_data = response.json()
        name = employee_data['name']
    else:
        print(f"Error: Employee with ID {employee_id} not found.")
        return

    todo_url = f'https://jsonplaceholder.typicode.com/
    todos?userId={employee_id}'
    response = requests.get(todo_url)
    if response.status_code == 200:
        todos_data = response.json()
    else:
        print(f"Error: Unable to fetch TODO
                list for Employee ID {employee_id}.")
        return

    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])

    print(f"Employee {name} is done with tasks
            ({done_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo['completed']:
            print("\t", todo['title'])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
    else:
        try:
             employee_id = int(sys.argv[1])
             get_employee_todo_progress(employee_id)
        except ValueError:
            print("Error: Invalid employee ID. Please provide an integer.")
