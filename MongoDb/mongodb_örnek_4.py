
import pymongo

from pymongo import MongoClient

a = 'abcdef'
myclient = pymongo.MongoClient('mongodb+srv://cemdogan1109:'+a+'@cluster0.gweobzp.mongodb.net/?retryWrites=true&w=majority')

mydb = myclient['students']
mycoll = mydb['studentinfo']

mylist = [{'_id': 1, 'name': 'vehpi', 'semt': 'bostancı'},
          {'_id': 2, 'name': 'alican', 'semt': 'küçükyalı'},
          {'_id': 3, 'name': 'tarık', 'semt': 'maltepe'},
          {'_id': 4, 'name': 'soner', 'semt': 'göztepe'},
          {'_id': 5, 'name': 'samet', 'semt': 'etiler'},
          {'_id': 6, 'name': 'ayhan', 'semt': 'akatlar'},
          {'_id': 7, 'name': 'kemal', 'semt': 'ortaköy'},
          {'_id': 8, 'name': 'koray', 'semt': 'beykoz'},
          {'_id': 9, 'name': 'orhan', 'semt': 'beylerbeyi'},
          {'_id': 10, 'name': 'sefa', 'semt': 'çengelköy'},
          {'_id': 11, 'name': 'fahri', 'semt': 'sarıyer'},
          {'_id': 12, 'name': 'harun', 'semt': 'emirgan'},
          {'_id': 13, 'name': 'güngör', 'semt': 'kuzguncuk'},
          {'_id': 14, 'name': 'serkan', 'semt': 'bebek'}]

#x = mycoll.insert_many(mylist)

#x = mycoll.find()
#for i in x:
#    print(i)

#myquery = {'semt': 'emirgan'}
#mydoc = mycoll.find(myquery)
#for i in mydoc:
#    print(i)

#myquery = {'semt': {'$regex': '^emir$'}}
#mydoc = mycoll.find(myquery)
#for i in mydoc:
#    print(i)

#mydoc = mycoll.find().sort('name', -1)
#for i in mydoc:
#    print(i)

#myquery = {'semt': 'bostancı'}
#mydoc = mycoll.delete_one()

#myquery = {'semt': {'$regex': '^a'}}
#mydoc = mycoll.delete_many({})

#myquery = {'semt': 'emirgan'}
#newvalues = {'$set': {'semt': 'taksim'}}
#
#mycoll.update_one(myquery, newvalues)

#myquery = {'name': {'$regex': '^c'}}
#newvalues = {'$set': {'semt': 'harbiye'}}
#
#mycoll.update_one(myquery, newvalues)

#myquery = {'semt': {'$regex': '^o'}}
#newvalues = {'$set': {'name': 'zeytinburnu'}}
#
#mycoll.update_many(myquery, newvalues)

#mycoll.drop()


















