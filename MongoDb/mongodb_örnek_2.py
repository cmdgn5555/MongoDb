
from pymongo import MongoClient

a = 'abcdef'
client = MongoClient('mongodb+srv://cemdogan1109:'+a+'@cluster0.gweobzp.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database('kulüp')

collection = db.get_collection('futbolcular')

#document = {'name': 'murat', 'lastname': 'türkmen', 'age': 24, 'nationality': 'türkiye'}

#response = collection.insert_one(document)
#last_inserted_id = response.inserted_id
#print('last inserted id: {}'.format(last_inserted_id))
#print(client.list_database_names())
#print(db.list_collection_names())

#for i in collection.find():
    #print(i)

#documents = []
#
#documents.append({'name': 'francesco', 'lastname': 'totti', 'age': 35, 'nationality': 'italya'})
#documents.append({'name': 'paul', 'lastname': 'scholes', 'age': 28, 'nationality': 'ingiltere'})
#documents.append({'name': 'patrick', 'lastname': 'kluivert', 'age': 30, 'nationality': 'hollanda'})
#
#response = collection.insert_many(documents)
#last_inserted_ids = response.inserted_ids
#print('last inserted id: {}'.format(last_inserted_ids))

#document = collection.find_one()
#print(document)

#cursor = collection.find()
#print('****************************')
#for i in cursor:
#    print(i)

#for i in collection.aggregate([{'$count': 'futbolcular'}]):
#    print(i)

#filter = {'nationality': 'almanya', 'age': 33}
#cursor = collection.find(filter)
#print(collection.count_documents({'nationality': 'türkiye', 'age': 24}))
#
#for i in cursor:
#    print(i)

#cursor = collection.find().sort('_id', -1)
#for i in cursor:
#    print(i)

#for i in collection.aggregate([{'$count': 'futbolcular'}]):
#    print(i)

#result = collection.delete_one({'name': 'raul'})
#print(result)

#result = collection.delete_many({'age': 33})
#print(result.deleted_count)

#result = collection.delete_many({})
#print(result.deleted_count)

#collection.drop()







