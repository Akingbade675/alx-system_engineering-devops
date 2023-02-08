#!/usr/bin/python3
'''Using a REST API, for a given employee ID,
returns information about his/her TODO list progress'''

import sys
import requests
import csv

if __name__ == "__main__":
    userId = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    name = requests.get(user_url).json().get("username")

    r = requests.get(todos_url)
    res = r.json()

    with open("{}.csv".format(userId), mode="w") as emp_file:
        csv_writer = csv.writer(
                                emp_file,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for todo in res:
            if todo.get("userId") == int(userId):
                csv_writer.writerow([
                                    userId,
                                    name,
                                    todo.get("completed"),
                                    todo.get("title")])
