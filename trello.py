import json
import requests
import os
from dotenv import load_dotenv

 
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')
BOARD_ID = os.getenv('BOARD_ID')

def api(endpoint):
    boardId = BOARD_ID
    url = "https://api.trello.com/1/boards/" + boardId + "/"

    query = {
    'key': API_KEY,
    'token': API_TOKEN
    }

    response = requests.request(
    "GET",
    url + endpoint,
    params=query
    )

    data = json.loads(response.text)
    return data

list_map = {}
for l in api("lists"):
    list_map[l["id"]] = l["name"]


cardCount = 0
list_to_card = {}
for c in api("cards"):
    cardCount += 1
    if c["idList"] in list_to_card:
        list_to_card[c["idList"]].append(c)
    else:
        list_to_card[c["idList"]] = [c]

print("""--------
SUMMARY
NUMBER OF LISTS: """ + str(len(list_to_card)) + """
TOTAL NUMBER OF CARDS: """ + str(cardCount) + """
--------""")

for l in list_to_card:
    print("NAME: \"" + list_map[l] + "\"")
    print("COUNT: " + str(len(list_to_card[l])))
    print()


    if os.getenv("FULL_DETAILS") == 'True':
        print("CARDS: ")
        for c in list_to_card[l]:
            print("\n" + "- " + c["name"])
        print()
        print("--------------")
    


