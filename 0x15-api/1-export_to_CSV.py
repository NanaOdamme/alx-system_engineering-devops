#!/usr/bin/python3
'''A script that gathers employee name completed
tasks and total number of tasks from an API and exports data in CSV format
'''
import csv
import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            emp_req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = emp_req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))

            csv_filename = '{}.csv'.format(id)
            with open(csv_filename, 'w', newline='') as csvfile:
                fieldnames = ['USER_ID', 'USERNAME',
                              'TASK_COMPLETED_STATUS', 'TASK_TITLE']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

                for task in completed_tasks:
                    writer.writerow({
                        'USER_ID': id,
                        'USERNAME': emp_name,
                        'TASK_COMPLETED_STATUS': str(task['completed']),
                        'TASK_TITLE': task['title']
                    })

                print('Data exported to {}'.format(csv_filename))
