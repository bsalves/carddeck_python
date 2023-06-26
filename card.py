import json, http.client

class Card:
    def __init__(self):
        self = self

    def get(self, endpoint:str):
        host = "deckofcardsapi.com"
        conn = http.client.HTTPSConnection(host)
        conn.request("GET", endpoint, headers={"Host": host})
        return conn.getresponse()
