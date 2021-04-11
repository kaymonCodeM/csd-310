import MongoClient

url = "mongodb+srv://admin:<password>@cluster0.f2jka.mongodb.net/test";
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names);