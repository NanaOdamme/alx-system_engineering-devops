#!/usr/bin/python3
'''A script that gathers employee name completed
tasks and total number of tasks from an API,
and exports the data in CSV format.
'''

import re
import requests
import csv
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


def export_to_csv(employee_id, employee_name, tasks):
    """
    Export data to CSV format.

    Args:
        employee_id (int): The employee ID.
        employee_name (str): The employee name.
        tasks (list): List of tasks.
    """
    csv_filename = f"{employee_id}.csv"
    csv_header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_header)

        for task in tasks:
            task_row = [
                employee_id,
                employee_name,
                task.get('completed'),
                task.get('title')
            ]
            csv_writer.writerow(task_row)

    print(f"Data exported to {csv_filename}")


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

        export_to_csv(employee_id, emp_name, tasks)
