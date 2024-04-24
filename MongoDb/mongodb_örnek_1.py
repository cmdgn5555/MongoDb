
import pymongo
from pymongo import MongoClient

a = 'abcdef'
cluster = MongoClient('mongodb+srv://cemdogan1109:'+a+'@cluster0.gweobzp.mongodb.net/?retryWrites=true&w=majority')

db = cluster['database']
collection = db['basketciler']

#print(cluster.list_database_names())

data = {'_id': 5, 'name': 'suat', 'lastname': 'emir', 'age': 34}

#collection.insert_one(data)

data2 = [{'_id': 7, 'name': 'shaquille', 'lastname': 'oneal', 'age': 35},
         {'_id': 8, 'name': 'penny', 'lastname': 'hardaway', 'age': 29},
         {'_id': 9, 'name': 'michael', 'lastname': 'jordan', 'age': 32}]

#collection.insert_many(data2)


data3 = [{'_id': 1, 'name': 'kerem'},
         {'_id': 2, 'name': 'erkan'},
         {'_id': 3, 'name': 'caner'}]

#collection.insert_many(data3)

data4 = {'_id': 8, 'name': 'vince', 'lastname': 'carter', 'age': 34}

#collection.insert_one(data4)


#for i in collection.find().skip(3):
    #print(i)

#for i in collection.find().limit(5):
    #print(i)

#print(collection.find_one())

#for i in collection.find({}, {'_id': 1, 'age': 1, 'name': 1}):
    #print(i)

#sorgu = {'age': 24}
#for i in collection.find({'name': 'suat'}):
#    print(i)

#for i in collection.find({'name': {'$regex': '.*'}}, {'_id': 0}):
    #print(i)

#for i in collection.find().sort('age', -1):
#    print(i)

#for i in collection.find({'$and': [{'name': 'hulusi'}, {'age': 87}]}):
#    print(i)

#a = {'_id': 4}
#b = {'$set': {'name': 'hamza', 'lastname': 'albayrak', 'age': 15}}
#
#collection.update_many(a, b)

#for i in collection.find({}, {'_id': 0}).limit(10):
#    print(i)

#collection.delete_many({})

#collection.drop()

