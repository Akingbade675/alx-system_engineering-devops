#!/usr/bin/python3
'''Using a REST API, for a given employee ID,
returns information about his/her TODO list progress'''

import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    comp_todos_title = []
    todos_count = 0
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    name = requests.get(user_url).json().get("name")

    r = requests.get(todos_url)
    res = r.json()

    for todo in res:
        if todo.get("userId") == int(userId):
            todos_count += 1
            if todo.get("completed"):
                comp_todos_title.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
                                                        name,
                                                        len(comp_todos_title),
                                                        todos_count))
    [print("\t {}".format(title)) for title in comp_todos_title]
