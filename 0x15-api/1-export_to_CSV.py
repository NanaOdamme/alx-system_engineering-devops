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
            emp_name = emp_req.get('name').split()[0]
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))

            csv_filename = '{}.csv'.format(id)
            with open(csv_filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

                for task in completed_tasks:
                    writer.writerow([
                        str(id),
                        emp_name,
                        str(task['completed']),
                        task['title']
                    ])

                print('Data exported to {}'.format(csv_filename))
