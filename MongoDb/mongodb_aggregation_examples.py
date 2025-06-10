
import pymongo
import datetime as datetime

a = 'abcdef'
client = pymongo.MongoClient('mongodb+srv://cemdogan1109:'+a+'@cluster0.gweobzp.mongodb.net/?retryWrites=true&w=majority')

mydb = client['employee']

collection = mydb.inventory

mydb2 = client['footboollers']

collection2 = mydb2.teaminfo2

mydb3 = client['students']

collection3 = mydb3['studentsscore']

collection4 = mydb3['stores']

collection5 = mydb3['books']

collection6 = mydb3['studentinfo']

#data = [{'_id': 1, 'firstname': 'nazım', 'lastname': 'koyuncu', 'class': 1, 'grade': 65, 'age': 7},
#        {'_id': 2, 'firstname': 'murat', 'lastname': 'teke', 'class': 3, 'grade': 50, 'age': 9},
#        {'_id': 3, 'firstname': 'harun', 'lastname': 'bayır', 'class': 2, 'grade': 70, 'age': 8},
#        {'_id': 4, 'firstname': 'serkan', 'lastname': 'akyol', 'class': 5, 'grade': 90, 'age': 11},
#        {'_id': 5, 'firstname': 'mehmet', 'lastname': 'akın', 'class': 4, 'grade': 45, 'age': 10},
#        {'_id': 6, 'firstname': 'recai', 'lastname': 'sönmez', 'class': 3, 'grade': 70, 'age': 9},
#        {'_id': 7, 'firstname': 'suat', 'lastname': 'ayan', 'class': 5, 'grade': 80, 'age': 11},
#        {'_id': 8, 'firstname': 'yusuf', 'lastname': 'erener', 'class': 2, 'grade': 90, 'age': 8},
#        {'_id': 9, 'firstname': 'mithat', 'lastname': 'demir', 'class': 4, 'grade': 45, 'age': 10},
#        {'_id': 10, 'firstname': 'nuri', 'lastname': 'tekinsoy', 'class': 5, 'grade': 70, 'age': 11},
#        {'_id': 11, 'firstname': 'ibrahim', 'lastname': 'eryaman', 'class': 1, 'grade': 95, 'age': 7},
#        {'_id': 12, 'firstname': 'burak', 'lastname': 'albayrak', 'class': 3, 'grade': 45, 'age': 9},
#        {'_id': 13, 'firstname': 'osman', 'lastname': 'ince', 'class': 4, 'grade': 50, 'age': 10},
#        {'_id': 14, 'firstname': 'ercüment', 'lastname': 'balta', 'class': 2, 'grade': 95, 'age': 8},
#        {'_id': 15, 'firstname': 'ümit', 'lastname': 'sevim', 'class': 1, 'grade': 80, 'age': 7},
#        {'_id': 16, 'firstname': 'celal', 'lastname': 'ersoy', 'class': 4, 'grade': 95, 'age': 10},
#        {'_id': 17, 'firstname': 'fahrettin', 'lastname': 'doruk', 'class': 5, 'grade': 50, 'age': 11},
#        {'_id': 18, 'firstname': 'metin', 'lastname': 'yiğitsoy', 'class': 2, 'grade': 95, 'age': 8}]

#collection6.insert_many(data)

#for i in collection6.aggregate([{'$project': {'_id': 0, 'age': 1, 'grade': 1}}]):
#    print(i)



#data = [{'user': 'kamil', 'subject': 'database', 'score': 80},
#        {'user': 'osman', 'subject': 'javascript', 'score': 90},
#        {'user': 'osman', 'subject': 'database', 'score': 85},
#        {'user': 'kamil', 'subject': 'javascript', 'score': 75},
#        {'user': 'osman', 'subject': 'data science', 'score': 60},
#        {'user': 'kamil', 'subject': 'data science', 'score': 95}]

#collection3.insert_many(data)

#agg_result = collection3.aggregate([{'$group': {'_id': '$score', 'total results': {'$sum': 1}}}])

#for i in agg_result:
        #print(i)

#agg_result = collection3.aggregate([{'$group': {'_id': '$user', 'StudentScoreAverage': {'$avg': '$score'}}}])
#
#for i in agg_result:
#        print(i)



#data = [{'_id': 1, 'item': 'klima', 'price': 1500, 'quantity': 4, 'date': datetime.datetime.utcnow()},
#        {'_id': 2, 'item': 'telefon', 'price': 2000, 'quantity': 3, 'date': datetime.datetime.utcnow()},
#        {'_id': 3, 'item': 'fön', 'price': 800, 'quantity': 6, 'date': datetime.datetime.utcnow()},
#        {'_id': 4, 'item': 'klima', 'price': 1600, 'quantity': 12, 'date': datetime.datetime.utcnow()},
#        {'_id': 5, 'item': 'fön', 'price': 500, 'quantity': 15, 'date': datetime.datetime.utcnow()}]

#collection4.insert_many(data)

#agg_results = collection4.aggregate([{'$group': {'_id': '$item',
#                        'avgAmount': {'$avg': {'$multiply': ['$price', '$quantity']}},
#                        'avgQuantity': {'$avg': '$quantity'}}}])
#
#for i in agg_results:
#        print(i)




#data = [{'_id': 1,
#         'title': 'abc123',
#         'isbn': '0001122223334',
#         'author': {'last': 'zzz', 'first': 'aaa'},
#         'copies': 5},
#        {'_id': 2,
#         'title': 'baked goods',
#         'isbn': '9999999999999',
#         'author': {'last': 'xyz', 'first': 'abc', 'middle': ''},
#         'copies': 2}]

##collection5.insert_many(data)
#
#for i in collection5.aggregate([{'$project': {'author.last': 1}}]):
    #print(i)






#collection2.insert_one({'foundation year': '1923'})


#record = {'firstname': 'haydar', 'lastname': 'kabak', 'department': 'insan kaynakları'}
#
#collection.insert_one(record)

#records = []
#
#records.append({'firstname': 'mert', 'lastname': 'duygun', 'department': 'teknik servis', 'salary': 25000, 'age': 27})
#records.append({'firstname': 'orhan', 'lastname': 'sayar', 'department': 'teknik servis', 'salary': 26000, 'age': 33})
#records.append({'firstname': 'mecnun', 'lastname': 'inan', 'department': 'teknik servis', 'salary': 28000, 'age': 24})
#records.append({'firstname': 'muharrem', 'lastname': 'incesoy', 'department': 'teknik servis', 'salary': 30000, 'age': 22})
#
#collection.insert_many(records)

#print(collection.find_one())

#for i in collection.find():
#    print(i)

#for i in collection.find({'firstname': 'suat'}):
#    print(i)


#print(collection.count_documents({}))

#for i in collection.find({'lastname': {'$in': ['adıgüzel']}}):
#    print(i)

#for i in collection.find({'department': 'insan kaynakları', 'age': {'$gte': 35}}):
#    print(i)

#for i in collection.find({'$or': [{'firstname': 'hasan'}, {'salary': {'$gte': 90000}}]}):
    #print(i)

#envanter = mydb.inventory
#
#inventory.insert_many([{'item': 'bilgisayar', 'quantity': 25, 'price': 35000},
#                       {'item': 'televizyon', 'quantity': 40, 'price': 45000},
#                       {'item': 'klima', 'quantity': 50, 'price': 20000},
#                       {'item': 'telefon', 'quantity': 70, 'price': 15000},
#                       {'item': 'playstation', 'quantity': 65, 'price': 10000},
#                       {'item': 'fön', 'quantity': 115, 'price': 3000},
#                       {'item': 'süpürge', 'quantity': 120, 'price': 5000},
#                       {'item': 'bulaşık makinası', 'quantity': 90, 'price': 60000},
#                       {'item': 'çamaşır makinası', 'quantity': 25, 'price': 65000},
#                       {'item': 'su ısıtıcı', 'quantity': 130, 'price': 2500}])

#for i in envanter.find({'$or': [{'quantity': {'$gte': 100}}, {'price': {'$lt': 50000}}]}):
#    print(i)
#
#print(envanter.count_documents({'quantity': {'$gte': 100}}))

#yöneticiler = mydb.managers

#yöneticiler.insert_one({'firstname': 'harun', 'lastname': 'toprakoğlu', 'age': 74, 'salary': 440000, 'gender': 'male'})

#for i in collection.find({'$and': [{'age': {'$gte': 40}}, {'salary': {'$gte': 30000}}]}):
#    print(i)

#print(yöneticiler.count_documents({}))

#mydb2.create_collection('teaminfo2')

#for i in mydb2.list_collection_names():
#    print(i)

#for i in collection.find({'age': {'$in': [53]}}):
#    print(i)

#print(collection.find_one())

#for i in collection.find():
#    print(i)

#collection.update_one({'firstname': 'harun'}, {'$set': {'lastname': 'yağanoğlu', 'age': 66, 'salary': 420000}})

#collection.update_many({'gender': 'female'}, {'$set': {'age': 37, 'salary': 530000}})

#collection.replace_one({'item': 'araba'}, {'item': 'tren', 'price': 45000000, 'capacity': 750, 'length': 88, 'height': 6})

#collection.update_many({'quantity': 350}, {'$set': {'item': 'araba', 'price': 2300000, 'capacity': 5, 'km': 6200, 'color': 'beyaz', 'top speed': 320}})

