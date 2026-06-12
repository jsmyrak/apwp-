from pymongo import MongoClient
import requests

client = MongoClient("mongodb://localhost:27017")
db = client.lab4
networks = db["networks"]

networks.drop()

print("Pobieranie danych z GeckoTerminal API...")
response = requests.get("https://api.geckoterminal.com/api/v2/networks")

if response.status_code == 200:
    data = response.json()["data"]
    
    print(f"Zapisywanie {len(data)} sieci do bazy...")
    networks.insert_many(data)
    
    pipeline = [
        {"$group": {
            "_id": "$type", 
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1}}
    ]
    
    print("\n--- WYNIKI AGREGACJI ---")
    print("Liczba sieci według typu:")
    
    for doc in networks.aggregate(pipeline):
        print(f" - Typ '{doc['_id']}': {doc['count']} szt.")

else:
    print(f"Błąd podczas łączenia z API: kod {response.status_code}")
client.close()