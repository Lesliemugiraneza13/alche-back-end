#!/usr/bin/python3
"""Gather data from an API and export an employee's TODO list to JSON."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    ).json()

    username = user.get("username")

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    json_filename = "{}.json".format(employee_id)
    with open(json_filename, "w") as json_file:
        json.dump({employee_id: tasks}, json_file)
