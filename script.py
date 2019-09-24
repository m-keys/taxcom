import requests
from dotenv import load_dotenv
import os


def get_token(login, password, integration_id):
    url = "https://api-lk-ofd.taxcom.ru/API/v2/Login"
    properties = {"login": login, "password": password}
    headers = {"Integrator-ID": integration_id, 
               "Content-Type": "application/json"}
    response = requests.post(url, json=properties, headers=headers)
    response.raise_for_status()
    return response.json()["sessionToken"]


def get_department_list(token):
    url = "https://api-lk-ofd.taxcom.ru/API/v2/DepartmentList"
    headers = {"Session-Token": token}
    response = requests.get(url, headers=headers)
    return response.json()

def get_outlet_list(token):
    url = "https://api-lk-ofd.taxcom.ru/API/v2/Outletlist"
    headers = {"Session-Token": token}
    response = requests.get(url, headers=headers)
    return response 


if __name__ == "__main__":
    load_dotenv()
    USER_LOGIN = os.getenv("USER_LOGIN")
    USER_PASS = os.getenv("USER_PASS")
    INTEGRATION_ID = os.getenv("INTEGRATION_ID")
    SESSION_TOKEN = get_token(USER_LOGIN, USER_PASS, INTEGRATION_ID)
    
    response = get_outlet_list(SESSION_TOKEN)
    if response.ok:
        dep_list = response.json()["records"]
        for dep in dep_list:
            print(dep["id"], dep["name"])
    else:
       print(response.json())
