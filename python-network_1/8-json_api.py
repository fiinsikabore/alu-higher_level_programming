#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        user_json = response.json()

        if user_json == {}:
            print("No result")
        else:
            user_id = user_json.get("id")
            user_name = user_json.get("name")
            print("[{}] {}".format(user_id, user_name))
    except ValueError:
        print("Not a valid JSON")
