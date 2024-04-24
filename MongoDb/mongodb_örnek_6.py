
import pymongo

a = "abcdef"
connection = pymongo.MongoClient("mongodb+srv://cemdogan1109:"+a+"@cluster0.gweobzp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
database = connection["Takım"]
collection = database["Futbolcular"]

#data = {"isim": "jude", "soyisim": "bellingham", "boy": 182, "kilo": 75, "ülke": "brezilya", "piyasa değeri": 150000000}
#collection.insert_one(data)

#data = {"isim": "cristiano", "soyisim": "ronaldo", "boy": 185, "kilo": 72, "ülke": "portekiz", "piyasa değeri": 220000000}
#collection.insert_one(data)

#data = [{"isim": "david", "soyisim": "beckham", "boy": 178, "kilo": 70, "ülke": "ingiltere", "piyasa değeri": 200000000},
#        {"isim": "david", "soyisim": "trezeguet", "boy": 175, "kilo": 65, "ülke": "fransa", "piyasa değeri": 120000000},
#        {"isim": "david", "soyisim": "villa", "boy": 170, "kilo": 63, "ülke": "ispanya", "piyasa değeri": 180000000}
#        ]
#collection.insert_many(data)

#data = {"_id": 2, "isim": "raul", "soyisim": "gonzales", "piyasa değeri": 300000000}
#collection.insert_one(data)

#print(collection.find_one())

#for i in collection.find():
#    print(i)

#for i in collection.find({}, {"_id": 1, "piyasa değeri": 0, "ülke": 0, "boy": 0, "kilo": 0}):
#    print(i)

#for i in collection.find({}, {"_id": 0, "boy": 1, "kilo": 1}):
#    print(i)

#for i in collection.find({}, {"_id": 0, "ülke": 1}):
#    print(i)

#for i in collection.find({}, {"_id": 1, "piyasa değeri": 1, "ülke": 1}):
#    print(i)

#query = {"isim": "kylian"}
#
#for i in collection.find(query, {"_id": 0}):
#        print(i)

#query = {"isim": "david"}
#
#for i in collection.find(query, {"_id": 0}):
#        print(i)

#query = {"boy": 178}
#
#for i in collection.find(query, {"_id": 0}):
#        print(i)

#query = {"kilo": 63}
#
#for i in collection.find(query, {"_id": 0}):
#        print(i)

#query = {"piyasa değeri": 200000000}
#
#for i in collection.find(query, {"_id": 0}):
#        print(i)

#query = {"ülke": "ingiltere"}
#
#for i in collection.find(query, {"_id": 0}):
#        print(i)

#for i in collection.find({"piyasa değeri": {"$gt": 200000000}}, {"_id": 0}):
#    print(i)

#for i in collection.find({"kilo": {"$gte": 70}}, {"_id": 0}):
#    print(i)

#for i in collection.find({"piyasa değeri": {"$lt": 150000000}}, {"_id": 0}):
#    print(i)

#for i in collection.find({"boy": {"$lte": 170}}, {"_id": 0}):
#    print(i)

#for i in collection.find({"ülke": {"$ne": "fransa"}}, {"_id": 0}):
#    print(i)

#for i in collection.find({"piyasa değeri": {"$in": [150000000, 300000000]}}, {"_id": 0}):
#    print(i)

#for i in collection.find({"ülke": {"$in": ["ingiltere", "fransa"]}}, {"_id": 0}):
#    print(i)

#for i in collection.find({"ülke": {"$nin": ["portekiz", "galler"]}}, {"_id": 0}):
#    print(i)

#query = {"isim": {"$regex": "^r"}}
#
#for i in collection.find(query):
#    print(i)

#for i in collection.find().sort("piyasa değeri", 1):
#    print(i)

#for i in collection.find().sort("piyasa değeri", -1):
#    print(i)

#for i in collection.find().sort("boy", 1):
#    print(i)

#for i in collection.find().sort("kilo", -1):
#    print(i)

#for i in collection.find().sort("ülke", 1):
#    print(i)

#for i in collection.find().sort("isim", -1):
#    print(i)

#for i in collection.find().sort("soyisim", -1):
#    print(i)

#for i in collection.find().sort("soyisim", 1):
#    print(i)

#for i in collection.find({"$and": [{"isim": "david"}, {"ülke": "ispanya"}]}):
#    print(i)

#for i in collection.find({"$and": [{"ülke": "ingiltere"}, {"piyasa değeri": 200000000}]}):
    #print(i)

#for i in collection.find({"$and": [{"ülke": "ispanya"}, {"isim": "david"}]}):
#    print(i)

#for i in collection.find({"$and": [{"boy": 178}, {"isim": "kylian"}]}):
#    print(i)

#for i in collection.find({"$and": [{"boy": 175}, {"kilo": 65}]}):
#    print(i)

#for i in collection.find({"$or": [{"ülke": "ingiltere"}, {"boy": 175}]}):
#    print(i)

#for i in collection.find({"$or": [{"isim": "david"}, {"ülke": "portekiz"}]}):
#    print(i)

#for i in collection.find({"$or": [{"piyasa değeri": 200000000}, {"soyisim": "totti"}]}):
#    print(i)

#for i in collection.find({"$or": [{"isim": "david"}, {"kilo": 63}]}):
#    print(i)

#for i in collection.find({"$or": [{"piyasa değeri": 120000000}, {"piyasa değeri": 180000000}]}):
#    print(i)

#query = {"isim": "cristiano"}
#new_value = {"$set": {"piyasa değeri": 8000}}
#
#print(collection.update_one(query, new_value))

#query = {"soyisim": "totti"}
#new_value = {"$set": {"boy": 183}}
#
#print(collection.update_one(query, new_value))

#query = {"soyisim": "scholes"}
#new_value = {"$set": {"piyasa değeri": 13000}}
#
#print(collection.update_one(query, new_value))

#query = {"isim": "raul"}
#new_value = {"$set": {"ülke": "ispanya"}}
#
#print(collection.update_one(query, new_value))

#query = {"isim": "david"}
#new_value = {"$set": {"piyasa değeri": 33000}}
#
#print(collection.update_one(query, new_value))

#query = {"isim": "david"}
#new_value = {"$set": {"piyasa değeri": 43000}}
#
#print(collection.update_many(query, new_value))

#query = {"ülke": "fransa"}
#new_value = {"$set": {"kilo": 80}}
#
#print(collection.update_many(query, new_value))


#query = {"ülke": "arjantin"}
#new_value = {"$set": {"boy": 195, "kilo": 85, "piyasa değeri": 125000}}
#
#print(collection.update_many(query, new_value))

#query = {"ülke": "mısır"}
#new_value = {"$set": {"boy": 172, "kilo": 67, "piyasa değeri": 90000, "hobiler": ["yüzme", "futbol", "seyahat"]}}
#
#print(collection.update_one(query, new_value))

#query = {"ülke": "ingiltere"}
#new_value = {"$set": {"piyasa değeri": 35000, "hobiler": ["kitap okumak", "sinema", "tiyatro"]}}
#
#print(collection.update_many(query, new_value))

#query = {"_id": 2}
#new_value = {"$set": {"boy": 177, "kilo": 70, "hobiler": ["seyahat", "sinema"]}}
#
#print(collection.update_one(query, new_value))

#for i in collection.find({}, {"_id": 0}).limit(3).skip(5):
#    print(i)

#for i in collection.find().limit(7):
#    print(i)

#for i in collection.find().skip(11):
#    print(i)

#for i in collection.find().skip(5).limit(6):
#    print(i)

#for i in collection.find().limit(3).skip(10):
#    print(i)

#query = {"ülke": "italya"}
#print(collection.delete_one(query))

#query = {"isim": {"$regex": "^d"}}
#print(collection.delete_one(query))

#query = {"piyasa değeri": {"$lt": 50000}}
#print(collection.delete_many(query))

#print(collection.delete_many({}))

#print(collection.drop())





