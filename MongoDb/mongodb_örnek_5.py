
import pymongo

a = 'abcdef'
connection = pymongo.MongoClient('mongodb+srv://cemdogan1109:'+a+'@cluster0.gweobzp.mongodb.net/?retryWrites=true&w=majority')
database = connection['bookstore']
collection = database['books']

#data = {'_id': 1, 'title': 'Küçük Prens',
#        'author': 'Antoine De Saint-Exupéry', 'pages': 457,
#        'rating': 7, 'genres': ['fantasy', 'magic']}
#collection.insert_one(data)
#database.oyuncular.insert_one({'name': 'burak', 'lastname': 'koray', 'age': 54, 'hometown': 'alabama'})

#datas = [{'_id': 8, 'title': '	Gazap Üzümleri',
#        'author': 'John Steinbeck', 'pages': 663,
#        'rating': 10, 'genres': ['fantasy', 'magic']},
#         {'_id': 9, 'title': 'Çanlar Kimin İçin Çalıyor',
#         'author': 'Ernest Hemingway', 'pages': 751,
#         'rating': 9, 'genres': ['fantasy', 'magic']},
#         {'_id': 10, 'title': 'Günlerin Köpüğü',
#         'author': 'Boris Vian', 'pages': 943,
#         'rating': 6, 'genres': ['fantasy', 'magic']}]

#collection.insert_many(datas)
#database.mycol_1.insert_many(datas)

#for i in database.mycol_1.find({'author': 'Antoine De Saint-Exupéry', 'rating': 10}):
#    print(i)

#for i in database.mycol_1.find({'author': 'John Steinbeck'}, {'rating': 1, 'pages': 1}):
#    print(i)

#for i in database.mycol_1.find({}, {'title': 0, 'author': 0}):
#    print(i)

#print(database.mycol_1.find_one({'author': 'Antoine De Saint-Exupéry'})

#print(database.employeeinformation.count_documents({'firstname': 'arif', 'department': 'muhasebe'}))

#print(database.employeeinformation.count_documents({1}))

#for i in database.employeeinformation.find().limit(6):
#    print(i)

#for i in database.employeeinformation.find().sort('firstname', 1).limit(15):
#    print(i)

#database.books.insert_one({'title': 'İkinci Cins',
#                           'author': 'Simone de Beauvoir',
#                           'rating': 9, 'pages': 769,
#                           'genres': ['magic'],
#                           'reviews': [{'name': 'cihan', 'lastname': 'güngör', 'body': 'güzel kitap!!'},
#                                       {'name': 'canberk', 'lastname': 'aslan', 'body': 'idare eder'},
#                                       {'name': 'cenk', 'lastname': 'ışın', 'body': 'sıkıcı kitap..'}]})

#database.books.insert_many([{'_id': 1, 'title': 'Varlık ve Hiçlik', 'author': 'Jean-Paul Sartre',
#                             'pages': 568, 'rating': 6, 'genres': ['fantasy', 'magic'],
#                             'reviews': [{'name': 'fikri', 'body': 'hiç beğenmedim!!!'},
#                                         {'name': 'koray', 'body': 'iyi kitap beğendim...'}]},
#                            {'_id': 2, 'title': 'Gülün Adı', 'author': 'Umberto Eco',
#                             'pages': 679, 'rating': 8, 'genres': ['detective'],
#                             'reviews': [{'name': 'fatih', 'body': 'hiç beğenmedim rezalet!!!'},
#                                         {'name': 'harun', 'body': 'tek kelimeyle mükemmel bir kitap...'}]},
#                            {'_id': 3, 'title': 'Cesur Yeni Dünya', 'author': 'Aldous Huxley',
#                             'pages': 753, 'rating': 9, 'genres': ['comedy'],
#                             'reviews': [{'name': 'ali', 'body': 'fena sayılmaz bir kitap!!!'},
#                                         {'name': 'veli', 'body': 'on numara kitap...'}]},
#                            {'_id': 4, 'title': 'Tatar Çölü', 'author': 'Dino Buzzati',
#                             'pages': 933, 'rating': 7, 'genres': ['horror', 'sadness'],
#                             'reviews': [{'name': 'emre', 'body': 'bana göre değil beğenmedim valla!!!'},
#                                         {'name': 'ertan', 'body': 'sürükleyici iyi ve öğretici bir kitap...'}]},
#                            {'_id': 5, 'title': 'Ses ve Öfke', 'author': 'William Faulkner',
#                             'pages': 424, 'rating': 5, 'genres': ['sport', 'tragic'],
#                             'reviews': [{'name': 'serhat', 'body': 'acıklı hikayesi olan bir kitaptı sarmadı beni!!!'},
#                                         {'name': 'koray', 'body': 'efsane kitaptı hikayesi oldukça iyiydi...'}]}])

#database.books.insert_one({'title': 'Rüzgâr Gibi Geçti', 'author': 'Margaret Mitchell',
#                           'rating': 4, 'pages': '277', 'genres': ['comedy'],
#                           'reviews': [{'name': 'yasin', 'lastname': 'bardakçı', 'body': 'tam bitirmedim ama şimdilik sürükleyici bir kitaba benziyo!!'}],
#                           'scores': [{'1997': '**********', '1999': '*****', '2000': '***'}],
#                           'countries': [{'1': 'germany', '2': 'england', '3': 'france', '4': 'spain'}]})

#database.books.insert_one({'takım': 'milan', 'ülke': 'italya',
#                           'kupa sayısı': 34, 'kuruluş': '1899', 'teknik direktörler': [{'ad': 'carlo', 'soyad': 'angelotti'},
#                                                                                        [{'bilgiler' : [{'yaş': 68, 'kupa sayısı': 7, 'memleketi': 'ispanya'}]}]]})

#database.books.insert_one({'okul adı': ['istanbul iöo' ,{'adres' : [{'mah': 'beyoğlu', 'sok': 'yeşilsümbül', 'no': 54}],
#                           'öğretmenler': ['matematik öğretmeni', {'öğretmen bilgileri': [{'ad': 'ali', 'soyad': 'sadık', 'yaş': 44}],
#                            'öğrenciler': ['matematik öğretmenine bağlı öğrenciler', {'öğrenci sıralaması': [{'1': 'rıza', '2': 'metin', '3': 'halil', '4': 'tarık'}],
#                            'öğrencilere ait yorumlar': [{'yorum 1': 'rıza tembelin tekidir..', 'yorum 2': 'metin çok unutkan bir öğrencidir',
#                                                          'yorum 3': 'halil sınıfın en akıllı öğrencisidir!!', 'yorum 4': 'tarık sürekli devamsızlık yapan bir öğrencidir!!'}]}]}]}]})

#database.books.insert_one({'kulüp adı': ['real madrid' ,{'adres' : [{'mah': 'De Concha Espina', 'sok': 'Chamartín', 'no':28036}],
#                           'teknik direktörler': [{'teknik direktör bilgileri': [{'ad': 'sanchez', 'soyad': 'higuain', 'yaş': 68}],
#                            'futbolcular': [{'futbolcu sıralaması': [{'1': 'raul', '2': 'figo', '3': 'carlos', '4': 'zidane'}],
#                            'futbolcuların değerleri': [{'değer 1': 'raulun değeri 240 milyon dolardır!!!', 'değer 2': 'figonun değeri 215 milyon dolardır!!!',
#                                                          'değer 3': 'carlosun değeri 150 milyon dolardır!!', 'değer 4': 'zidanenin değeri 270 milyon dolardır!!'}]}]}]}]})


#for i in database.books.find({'pages': {'$lte': '200'}, 'rating': {'$lte': 7}}):
#    print(i)

#for i in database.books.find({'$and': [{'rating': {'$gte': 7}}, {'pages': {'$gte': 600}}]}):
#    print(i)

#for i in database.books.find({'rating': {'$in': [7, 8, 9]}, 'pages': {'$in': [769]}}):
#    print(i)

#for i in database.books.find({'okul adı': 'istanbul iöo'}):
#    print(i)

#for i in database.books.find({'genres': {'$all': ['sadness', 'horror', 'spy']}}):
#    print(i)

#for i in database.books.find({'kulüp adı.1.teknik direktörler.0.futbolcular.1.futbolcuların değerleri.0.değer 3': 'figonun değeri 215 milyon dolardır!!!'}):
#    print(i)

#database.books.delete_one({'title': 'Cesur Yeni Dünya'})
#
#database.books.delete_many({'genres': {'$all': ['fantasy', 'magic']}})

#
#result = database.books.delete_many({'rating': 8})
#print(result.deleted_count)

#result = database.books.update_one({'_id': 5}, {'$set': {'author': 'Umberto Eco', 'title': 'Gülün Adı', 'rating': 8, 'pages': 842}})
#print(result.modified_count)
#print(result.matched_count)

#result = database.books.update_many({'rating': 7}, {'$set': {'author': 'Jack London', 'pages': 1045}})
#print(result.modified_count)
#print(result.matched_count)

#result = database.books.update_one({'_id': 4}, {'$inc': {'pages': -20}})
#print(result.modified_count)
#print(result.matched_count)

#result = database.books.update_many({'rating': 7}, {'$inc': {'pages': 1500}})
#print(result.modified_count)
#print(result.matched_count)

#result = database.books.update_many({'author': 'Jacques Lacan'}, {'$pull': {'genres': 'sci-fi'}})
#print(result.modified_count)
#print(result.matched_count)

#result = database.books.update_many({'author': 'Jacques Lacan'}, {'$push': {'genres': 'horror'}})
#print(result.modified_count)
#print(result.matched_count)

#result = database.books.update_many({'author': 'Jacques Lacan'}, {'$push': {'genres': {'$each': [10, 20, 30, 40]}}})
#print(result.modified_count)
#print(result.matched_count)

