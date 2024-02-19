#!/usr/bin/python3
'''A script that gathers employee name completed
tasks and total number of tasks from an API,
and exports the data in JSON format.
'''

import requests
import json
import sys

REST_API = "https://jsonplaceholder.typicode.com"

def fetch_all_employees_data():
    """
    Fetch data for all employees from the API.

    Returns:
        dict: Data for all employees.
    """
    users_url = f"{REST_API}/users"
    response = requests.get(users_url)

    try:
        response.raise_for_status()
        employees = response.json()
        return {employee['id']: employee['name'] for employee in employees}
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch data for all employees from API - {e}")
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

def export_to_json(employees_data, tasks):
    """
    Export data to JSON format.

    Args:
        employees_data (dict): Data for all employees.
        tasks (list): List of tasks.
    """
    json_filename = "todo_all_employees.json"
    json_data = {}

    for task in tasks:
        user_id = task.get("userId")
        username = employees_data.get(user_id, "Unknown")

        if user_id not in json_data:
            json_data[user_id] = []

        json_data[user_id].append({
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed"),
        })

    with open(json_filename, mode="w") as json_file:
        json.dump(json_data, json_file, indent=2)

    print(f"Data exported to {json_filename}")

if __name__ == '__main__':
    employees_data = fetch_all_employees_data()
    tasks_data = fetch_tasks_data()

    print("Exporting data for all employees...")

    export_to_json(employees_data, tasks_data)
