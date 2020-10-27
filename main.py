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

# col.insert_one(member)

# results = col.find({"$or": [{"age": 28}, {"address": "seoul"}]})
# for r in results:
#    print(r)

# results = col.find({"age": {"$gte": 28, "$lt": 29}}, {"_id": False, "name": True, "address": True}).sort(-1).skip(1).limit(3)
# for r in results:
#     print(r)

col.update_many({"name": "hong-il"}, {"$set": {"name": "hongil.kim"}})

