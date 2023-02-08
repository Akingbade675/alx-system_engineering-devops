#!/usr/bin/python3
'''Using a REST API, for a given employee ID,
returns information about his/her TODO list progress'''

import sys
import requests
import json

if __name__ == "__main__":
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    json_data = {}

    # sends a request to the todo url to get all todos
    r = requests.get(todos_url)

    # decodes json rsponse
    res = r.json()

    # create a file to write formatted json response 
    with open("todo_all_employees.json", mode="w") as emp_file:

        for todo in res:
            username = ""
            userId = todo.get("userId")

            # checks if userId does not exists in the dict `json_data`
            if json_data.get(userId) is None:
                json_data[userId] = []

                # sends a get request to get the username of current todo userId
                user_url = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
                username = requests.get(user_url).json().get("username")

            # if the userId already exists in the `json_data` dict,
            #   get the username from an existing child of the userId
            #   in the `json_data` dict in order to reduce the number 
            #   of time the api is called to get the
            #   username of the same user
            username = username if username != "" else json_data.get(userId)[0].get("username")

            json_data[userId].append({
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")})

        # write the json_data dict to the file in json string format
        emp_file.write(json.dumps(json_data))
