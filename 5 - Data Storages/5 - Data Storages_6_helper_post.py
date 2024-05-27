import requests, random

titles = ["Title One", "Title Two", "Title Three", "Title Four", "TitleFive", "Title Six", "Title Seven", "Title Eight", "Title Nine", "Title ..."]

authors = ["Korhonen", "Virtanen", "Nieminen", "Laine", "Heikkinen", "Koskinen", "Lehtonen", "Lehtinen", "Saarinen", 
           "Salminen", "Heinonen", "Niemi", "Kinnunen", "Salonen", "Turunen", "Salo", "Laitinen", "Rantanen", "Tuominen", 
           "Karjalainen", "Jokinen", "Mattila", "Savolainen", "Lahtinen", "Ahonen"]

for num in range(1, 11):
    rreply = requests.post('http://localhost:5000/add_data/', json = {"_id": num, "title": random.choice(titles),"author": random.choice(authors)})
    print(rreply.status_code)
    print(rreply.content)