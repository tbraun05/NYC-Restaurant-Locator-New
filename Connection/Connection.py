from pymongo import MongoClient

mongodb_uri = "mongodb://studentmysql:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false"
conn = MongoClient(mongodb_uri)

db = conn.Geo
coll = db.restaurant

Geo_cursor = coll.find({})
print(Geo_cursor)

