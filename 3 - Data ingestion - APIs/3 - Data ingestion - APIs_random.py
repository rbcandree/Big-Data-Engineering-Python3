"""
4) Implement a separate Python script to generate books into the book store. 
You can use the following code snippet as a starting point.

import requests

rreply = requests.post('http://localhost:5000/sell/', json={"title": "book","author":"Esteri","year_of_publication":1990})
print(rreply.status_code)
print(rreply.json())

Think of a way to randomize some of the input data, 
so that you can use the script to feed 100 books into the book store easily, without need to write 100 JSONs manually.
"""

import requests, random

titles = ["Book One", "Book Two", "Book Three", "Book Four", "Book Five", "Book Six", "Book Seven", "Book Eight", "Book Nine", "Book Ten", "Book ..."]

authors = ["Korhonen", "Virtanen", "Mäkinen", "Nieminen", "Mäkelä", "Hämäläinen", "Laine", "Heikkinen", "Koskinen", "Järvinen", "Lehtonen", 
"Lehtinen", "Saarinen", "Salminen", "Heinonen", "Niemi", "Heikkilä", "Kinnunen", "Salonen", "Turunen", "Salo", "Laitinen", 
"Rantanen", "Tuominen", "Karjalainen", "Jokinen", "Mattila", "Savolainen", "Lahtinen", "Ahonen"]

for num in range(1, 101):
    rreply = requests.post('http://localhost:5000/sell/', json = {"title": random.choice(titles),"author": random.choice(authors),"year_of_publication": random.randint(1970, 2023)})
    print(rreply.status_code)
    print(rreply.content)