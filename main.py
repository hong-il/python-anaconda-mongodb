import pymongo

member = {
    "name": "hong-il",
    "age": 28,
    "address": "seoul",
    "profile": [
        "a.jpg",
        "b.jpg"
    ]
}

member2 = {
    "name": "hong-il",
    "address": "seoul",
    "profile": [
        "a.jpg",
        "b.jpg"
    ]
}

conn = pymongo.MongoClient("localhost", 27017)
db = conn.test  # Database
col = db.members    # Collection

col.insert_one(member)