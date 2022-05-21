import Constants
import requests, json
from Filter import Filter
from Payload import Payload
from datetime import datetime

# Tutorial Video: https://www.youtube.com/watch?v=sdn1HgxLwEg

# Things To Do:
#   Create an Automatic Archiver
#   Create an Automatic Deleter

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22",
    "Authorization": "Bearer " + Constants.NOTION_TOKEN
}

def getDatabase(databaseId, headers):
    getDatabaseRequestEndpoint = f"https://api.notion.com/v1/databases/{databaseId}"
    result = requests.request(Constants.GET_REQUEST, getDatabaseRequestEndpoint, headers=headers)

    return result

def queryDatabase(databaseId, headers, filter):
    getDatabaseRequestEndpoint = f"https://api.notion.com/v1/databases/{databaseId}/query"
    result = requests.post(getDatabaseRequestEndpoint, headers=headers, json=filter)

    return result

def getDatabasePage(pageId, headers):
    getPageRequestEndpoint = f"https://api.notion.com/v1/pages/{pageId}"
    result = requests.request(Constants.GET_REQUEST, getPageRequestEndpoint, headers=headers)

    return result

def createPage(payload, headers):
    postPageEndpoint = "https://api.notion.com/v1/pages"
    requests.post(postPageEndpoint, headers=headers, data=payload)

def turnToJSON(result):
    data = result.json()
    with open('readme.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

print("Starting Application")

currentDay = datetime.today()
payloads = Payload()
filters = Filter()

print("Current Month: ", currentDay.month)
print("Current Day: ", currentDay.day)

if(currentDay.day == 10):
    if(len(queryDatabase(Constants.BULLETIN_BOARD, headers, filters.getCreditCardFilter()).json()["results"]) == 0):
        creditCardPayload = json.dumps(payloads.getCreditCardPayload())
        createPage(creditCardPayload, headers)

elif(currentDay.day == 21):
    if(len(queryDatabase(Constants.BULLETIN_BOARD, headers, filters.getRentFilter()).json()["results"]) == 0):
        rentPayload = json.dumps(payloads.getRentPayload())
        createPage(rentPayload, headers)

if((currentDay.month == 1 or currentDay.month == 7) and currentDay.day == 1):
    if(len(queryDatabase(Constants.BULLETIN_BOARD, headers, filters.getUCIFilter()).json()["results"]) == 0):
        uciEmailPayload = json.dumps(payloads.getUCIEmailPayload())
        createPage(uciEmailPayload, headers)

