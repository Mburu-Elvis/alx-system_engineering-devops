#!/usr/bin/python3
'''module consuming an employee data API'''
import requests
from sys import argv

url = 'https://jsonplaceholder.typicode.com/todos/1'
res = requests.get(url, 'html_parser')
name = res.name
tasks = res.completed
done = len(res)
print(name)
