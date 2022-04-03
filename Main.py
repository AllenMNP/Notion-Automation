import Constants
import requests, json
from Payload import Payload
from datetime import datetime

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

def queryDatabase(databaseId, headers):
    getDatabaseRequestEndpoint = f"https://api.notion.com/v1/databases/{databaseId}/query"
    result = requests.request(Constants.POST_REQUEST, getDatabaseRequestEndpoint, headers=headers)

    return result

def getDatabasePage(pageId, headers):
    getPageRequestEndpoint = f"https://api.notion.com/v1/pages/{pageId}"
    result = requests.request(Constants.GET_REQUEST, getPageRequestEndpoint, headers=headers)

    return result

def createPage(payload, headers):
    postPageEndpoint = "https://api.notion.com/v1/pages"
    requests.request(Constants.POST_REQUEST, postPageEndpoint, headers=headers, data=payload)

def turnToJSON(result):
    data = result.json()
    with open('./db.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

print("Starting Application")

currentDay = datetime.today()
payloads = Payload()

print("Current Month: ", currentDay.month)
print("Current Day: ", currentDay.day)

if(currentDay.day == 10):
    creditCardPayload = json.dumps(payloads.getCreditCardPayload())
    createPage(creditCardPayload, headers)
elif(currentDay.day == 20):
    rentPayload = json.dumps(payloads.getRentPayload())
    createPage(rentPayload, headers)

if((currentDay.month == 1 or currentDay.month == 7) and currentDay.day == 1):
    uciEmailPayload = json.dumps(payloads.getUCIEmailPayload())
    createPage(uciEmailPayload, headers)

