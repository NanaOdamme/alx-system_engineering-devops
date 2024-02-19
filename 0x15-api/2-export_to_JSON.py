#!/usr/bin/python3
'''A script that gathers employee name completed
tasks and total number of tasks from an API,
and exports the data in JSON and CSV formats.
'''

import re
import requests
import json
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def fetch_employee_data(employee_id):
    """
    Fetch employee data from the API.

    Args:
        employee_id (int): The employee ID.

    Returns:
        dict: Employee data.
    """
    employee_url = f"{REST_API}/users/{employee_id}"
    response = requests.get(employee_url)

    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch employee data from API - {e}")
        sys.exit(1)


def fetch_tasks_data():
    """
    Fetch tasks data from the API.

    Returns:
        list: List of tasks.
    """
    tasks_url = f"{REST_API}/todos"
    response = requests.get(tasks_url)

    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch tasks data from API - {e}")
        sys.exit(1)


def export_to_json(employee_id, employee_name, tasks):
    """
    Export data to JSON format.

    Args:
        employee_id (int): The employee ID.
        employee_name (str): The employee name.
        tasks (list): List of tasks.
    """
    json_filename = f"{employee_id}.json"
    json_data = {
        "USER_ID": [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name,
            }
            for task in tasks
        ]
    }

    with open(json_filename, mode="w") as json_file:
        json.dump(json_data, json_file, indent=2)

    print(f"Data exported to {json_filename}")


if __name__ == '__main__':
    if len(sys.argv) != 2 or not re.fullmatch(r'\d+', sys.argv[1]):
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    emp_data = fetch_employee_data(employee_id)
    tasks_data = fetch_tasks_data()

    emp_name = emp_data.get('name')
    tasks = [task for task in tasks_data if task.get('userId') == employee_id]

    if tasks:
        for task in tasks:
            print(f"\t{task.get('title')}")

        export_to_json(employee_id, emp_name, tasks)
