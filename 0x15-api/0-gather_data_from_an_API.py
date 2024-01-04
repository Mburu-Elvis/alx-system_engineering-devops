#!/usr/bin/python3
'''module consuming an employee data API'''
import requests
from sys import argv

url = 'https://jsonplaceholder.typicode.com/'


def employeeDetails(employeeId):
    '''Function to retrieve employee details and return the name'''
    response = requests.get(f'{url}/users/{employeeId}')
    if response.status_code == 200:
        empData = response.json()
        name = empData['name']
    else:
        print('Employee doesn\'t exist')
    return (name)


def employeeToDo(employeeId, employeeName):
    '''Function to retrieve an employee todo list information.'''
    response = requests.get(f'{url}/todos?userId={employeeId}')
    if response.status_code == 200:
        todos = response.json()
        completed_tasks = [todo for todo in todos if todo['completed']]
        total_tasks = len(todos)
        total_completed = len(completed_tasks)
        print(f'Employee {employeeName} is done with ', end='')
        print(f'tasks({total_completed}/{total_tasks})')

        for task in completed_tasks:
            print(f"\t{task['title']}")


try:
    empId = int(argv[1])
    empId = str(empId)
except Exception as e:
    print(e)


name = employeeDetails(empId)
employeeToDo(empId, name)
