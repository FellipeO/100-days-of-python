import os

import requests
import datetime as dt
import dotenv


#------------------------------------CREATE USER------------------------------------#
pixela_endpoint = "https://pixe.la/v1/users"

dotenv.load_dotenv(".env")
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#------------------------------------CREATE GRAPH------------------------------------#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Push-ups Graph",
    "unit":"push-ups",
    "type":"int",
    "color":"kuro",
}

headers = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#------------------------------------CREATE PIXEL------------------------------------#
today = dt.datetime.now()

GRAPH_ID = "graph1"
PUSH_UPS = "16"
PIXEL_DATE = today.strftime("%Y%m%d") #yyyymmdd
pixel_endpoint = f"{graph_endpoint}/graph1"

pixel_config = {
    "date":PIXEL_DATE,
    "quantity":PUSH_UPS
}
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

#------------------------------------EDIT PIXEL------------------------------------#
put_pixel_endpoint = f"{pixel_endpoint}/{PIXEL_DATE}"
#
# response = requests.put(url=put_pixel_endpoint, json=pixel_config, headers=headers)
# print(response)

#------------------------------------DELETE PIXEL------------------------------------#
response = requests.delete(url=put_pixel_endpoint, headers=headers)
print(response)