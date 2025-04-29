from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://harivardhan9397921834:949383Hk@devops.oe48c2r.mongodb.net/?retryWrites=true&w=majority&appName=devops"

# Create a new client and connect to the server
client = MongoClient(uri,server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['database1']
collection = db['peddireddy']

dictionary = {'name':'peddireddy','age': 25}

insertDoc = collection.insert_one(dictionary)
print("Inserted Document : ", insertDoc.inserted_id)
client.close()