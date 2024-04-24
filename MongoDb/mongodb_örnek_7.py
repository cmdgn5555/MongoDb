import collections

import pymongo

a = "abcdef"
connect = pymongo.MongoClient("mongodb+srv://cemdogan1109:"+a+"@cluster0.gweobzp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

database = connect["company"]
collection = database["employee"]

#data = {"name": "mehmet", "lastname": "akın", "age": 54, "salary": 43000}
#print(collection.insert_one(data))

#data = [{"name": "mehmet", "lastname": "tok", "age": 35, "salary": 30000},
#        {"name": "mehmet", "lastname": "demir", "age": 50, "salary": 55000},
#        {"name": "ahmet", "lastname": "tok", "age": 37, "salary": 62000},
#        {"name": "ahmet", "lastname": "tok", "age": 45, "salary": 47000},
#        {"name": "ahmet", "lastname": "demir", "age": 37, "salary": 38000},
#        {"name": "ahmet", "lastname": "yaman", "age": 45, "salary": 55000},
#        {"name": "selim", "lastname": "ceylan", "age": 50, "salary": 47000},
#        {"name": "selim", "lastname": "akın", "age": 46, "salary": 32000},
#        {"name": "selim", "lastname": "yaman", "age": 43, "salary": 62000},
#        {"name": "hasan", "lastname": "ceylan", "age": 46, "salary": 65000},
#        {"name": "hasan", "lastname": "demir", "age": 50, "salary": 38000},
#        {"name": "hasan", "lastname": "eryaman", "age": 37, "salary": 68000},
#        {"name": "hasan", "lastname": "erdem", "age": 35, "salary": 43000},
#        {"name": "kemal", "lastname": "ceylan", "age": 43, "salary": 30000},
#        {"name": "kemal", "lastname": "tok", "age": 52, "salary": 32000},
#        {"name": "kemal", "lastname": "eryaman", "age": 35, "salary": 65000},
#        {"name": "kemal", "lastname": "erdem", "age": 52, "salary": 68000}]
#
#print(collection.insert_many(data))

#print(collection.find_one())

#for i in collection.find({"name": "kemal", "salary": 30000}):
#        print(i)

#for i in collection.find({}, {"name": 1, "lastname": 1, "_id": 0}):
#        print(i)

#for i in collection.find({}, {"age": 1}):
#       print(i)

#for i in collection.find({"salary": {"$eq": 32000}}):
#    print(i)

#for i in collection.find({"age": {"$eq": 35}}):
#    print(i)

#for i in collection.find({"salary": {"$ne": 65000}}):
#    print(i)

#for i in collection.find({"lastname": {"$ne": "tok"}}):
#    print(i)

#for i in collection.find({"salary": {"$gte": 55000}}):
#    print(i)

#for i in collection.find({"age": {"$gte": 52}}):
#    print(i)

#for i in collection.find({"name": {"$gte": "r"}}):
#    print(i)

#for i in collection.find({"lastname": {"$lte": "k"}}):
#    print(i)

#for i in collection.find({"salary": {"$lte": 43000}}):
#    print(i)

#for i in collection.find({"age": {"$lte": 37}}):
#    print(i)

#for i in collection.find({"salary": {"$gt": 60000}}):
#    print(i)

#for i in collection.find({"age": {"$gt": 45}}):
#    print(i)

#for i in collection.find({"name": {"$gt": "p"}}):
#    print(i)

#for i in collection.find({"lastname": {"$lt": "d"}}):
#    print(i)

#for i in collection.find({"age": {"$lt": 37}}):
#    print(i)

#for i in collection.find({"salary": {"$lt": 35000}}):
#    print(i)

#for i in collection.find({"name": {"$in": ["kemal", "selim"]}}):
#    print(i)

#for i in collection.find({"salary": {"$in": [30000, 68000]}}):
#    print(i)

#for i in collection.find({"age": {"$in": [50, 46, 43]}}):
#    print(i)

#for i in collection.find({"lastname": {"$in": ["tok", "eryaman", "erdem"]}}):
#    print(i)

#for i in collection.find({"salary": {"$nin": [35000, 68000, 30000, 32000, 65000]}}):
#    print(i)

#for i in collection.find({"age": {"$nin": [37, 46, 50, 52]}}):
#    print(i)

#for i in collection.find({"name": {"$nin": ["kemal", "ahmet", "mehmet"]}}):
#    print(i)

#for i in collection.find({"lastname": {"$nin": ["tok", "akın", "erdem", "eryaman"]}}):
#    print(i)

#for i in collection.find({"$and": [{"name": "ahmet", "salary": {"$gte": 50000}}]}):
#    print(i)

#for i in collection.find({"$and": [{"name": "hasan", "age": {"$lt": 40}}]}):
#    print(i)

#for i in collection.find({"$and": [{"lastname": "demir", "age": {"$eq": 50}}]}):
#    print(i)

#for i in collection.find({"$and": [{"name": "kemal", "salary": {"$ne": 30000}}]}):
#    print(i)

#for i in collection.find({"$and": [{"lastname": "tok", "age": {"$in": [35, 45]}}]}):
#    print(i)

#for i in collection.find({"$and": [{"lastname": "demir", "salary": {"$nin": [55000]}}]}):
#    print(i)

#for i in collection.find({"$or": [{"lastname": "ceylan"}, {"name": "hasan"}]}):
#    print(i)

#for i in collection.find({"$or": [{"name": "selim"}, {"salary": {"$gte": 65000}}]}):
#    print(i)

#for i in collection.find({"$or": [{"age": {"$lt": 37}}, {"salary": {"$lt": 32000}}]}):
#    print(i)

#for i in collection.find({"$or": [{"age": {"$gt": 50}}, {"salary": {"$gt": 60000}}]}):
#    print(i)

#for i in collection.find({"$or": [{"lastname": "eryaman"}, {"age": {"$in": [52, 43]}}]}):
#    print(i)

#for i in collection.find({"$or": [{"name": "mehmet"}, {"salary": {"$nin": [62000, 65000, 68000]}}]}):
#    print(i)

#for i in collection.find({"$or": [{"name": "hasan"}, {"salary": {"$eq": 62000}}]}):
#    print(i)

#for i in collection.find({"$nor": [{"name": "ahmet"}, {"name": "mehmet"}]}):
#    print(i)

#for i in collection.find({"$nor": [{"lastname": "tok"}, {"age": {"$gt": 50}}]}):
#    print(i)

#for i in collection.find({"$nor": [{"age": {"$lt": 37}}, {"salary": {"$lt": 60000}}]}):
#    print(i)

#dblist = connect.list_database_names()
#print(dblist)

#query = {"name": "mehmet"}
#new_values = {"$set": {"name": "hayrettin"}}
#
#collection.update_many(query, new_values)
#
#for i in collection.find():
#    print(i)

#query = {"name": {"$regex": "^a"}}
#new_values = {"$set": {"name": "orhan"}}
#
#collection.update_many(query, new_values)
#
#for i in collection.find():
#    print(i)

#query = {"name": "orhan", "lastname": "tok", "salary": 47000}
#
#collection.delete_one(query)
#
#for i in collection.find():
#    print(i)

#query = {"salary": 30000}
#collection.delete_many(query)
#
#for i in collection.find():
#    print(i)

#query = {"age": {"$gt": 50}}
#
#collection.delete_many(query)
#
#for i in collection.find():
#    print(i)

#query = {"salary": {"$eq": 62000}}
#
#collection.delete_many(query)
#
#for i in collection.find():
#    print(i)

#query = {"salary": {"$lt": 40000}}
#new_value = {"$set": {"salary": 88000}}
#
#collection.update_many(query, new_value)
#
#for i in collection.find():
#    print(i)

#query = {"lastname": "eryaman"}
#new_value = {"$set": {"age": 12}}
#
#collection.update_many(query, new_value)
#
#for i in collection.find():
#    print(i)

#query = {"name": "hasan", "lastname": "demir"}
#new_value = {"$set": {"age": 96}}
#
#collection.update_one(query, new_value)
#
#for i in collection.find():
#    print(i)

#query = {"age": 50}
#new_value = {"$set": {"age": 123}}
#
#collection.update_many(query, new_value)
#
#for i in collection.find():
#    print(i)


#print(collection.drop())

#print(connect.list_database_names())


























