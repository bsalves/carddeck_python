from flask import Flask, jsonify
import json, http.client
from card import Card

app = Flask(__name__) 
app.config["DEBUG"] = True

items = [ { "id": 1 } ]

@app.route("/cards")
def cards():
    c = Card()
    deck = c.get("/api/deck/new/shuffle/?deck_count=1")
    deckJson = json.loads(deck.read().decode())
    cards = c.get(f'/api/deck/{deckJson["deck_id"]}/draw/?count=1')
    return json.loads(cards.read().decode())

@app.route("/card/image")
def cardImage():
    c = Card()
    image = c["cards"][0]["image"]
    return image

app.run()
