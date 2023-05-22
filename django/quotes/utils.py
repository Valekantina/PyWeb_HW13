from pymongo import MongoClient


def get_mongodb():
    client = MongoClient(
        'mongodb+srv://vgordynska:TheLastOfUs1@goithw.euffuef.mongodb.net/test')
    db = client.hw
    return db
