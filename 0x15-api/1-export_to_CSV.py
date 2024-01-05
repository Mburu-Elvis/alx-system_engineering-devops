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
        username = empData['username']
        return (username)
    return (None)


def employeeToDo(employeeId, username):
    '''Function to store  employee information to a CSV file.'''
    response = requests.get(f'{url}/todos?userId={employeeId}')
    if response.status_code == 200:
        todos = response.json()

        for task in todos:
            userId = task['userId']
            status = task['completed']
            title = task['title']
            with open(f'{userId}.csv', 'a') as myfile:
                row = f'"{userId}", "{username}", "{status}", "{title}"\n'
                myfile.write(f'{row}')


try:
    empId = int(argv[1])
    empId = str(empId)
except Exception as e:
    print(e)


username = employeeDetails(empId)
employeeToDo(empId, username)
