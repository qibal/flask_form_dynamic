from pymongo import MongoClient

db = None
collection = None

def init_db(app):
    global db, collection
    client = MongoClient(app.config['MONGO_URI'])
    db = client[app.config['DATABASE_NAME']]
    collection = db[app.config['COLLECTION_NAME']]

def get_all_data():
    return list(collection.find())

def add_cattle_data(data):
    collection.insert_one(data)