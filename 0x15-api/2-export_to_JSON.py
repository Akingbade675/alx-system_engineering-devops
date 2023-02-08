#!/usr/bin/python3
'''Using a REST API, for a given employee ID,
returns information about his/her TODO list progress'''

import json
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    json_data = {}
    task_list = []

    username = requests.get(user_url).json().get("username")

    r = requests.get(todos_url)
    res = r.json()

    with open("{}.json".format(userId), mode="w") as emp_file:
        for todo in res:
            if todo.get("userId") == int(userId):
                task_list.append({
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": username})
        emp_file.write(json.dumps({userId: task_list}))
