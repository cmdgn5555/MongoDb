import pymongo
from pprint import pprint
from bson import ObjectId
import uuid

a = "abcdef"
connect = pymongo.MongoClient("mongodb+srv://cemdogan1109:"+a+"@cluster0.gweobzp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

database = connect["okul"]
collection = database["öğrenciler"]

#collection.insert_one({"isim": "samet", "soyisim": "demir", "sınıfı": "8-A", "vize": 40, "final": 70, "hobiler": ["beyzbol", "yüzme", "tenis"]})

#print(database.list_collection_names())

#pprint(database.get_collection("basketbolcular"))

#for i in database.list_collections():
#    pprint(i)

#pprint(database.get_collection("basketbolcular"))

#pprint(database.list_collection_names())

#collection.rename("basketbolcular")

#database.drop_collection("futbolcular")

#data =[{"isim": "serkan", "soyisim": "çimen", "sınıfı": "6-A", "vize": 10, "final": 30, "hobiler": ["müzik", "dans", "fotoğrafçılık"]},
#       {"isim": "caner", "soyisim": "yiğitel", "sınıfı": "7-A", "vize": 70, "final": 20, "hobiler": ["masa oyunları", "seyahat", "müzeleri gezmek"]},
#       {"isim": "ertan", "soyisim": "berk", "sınıfı": "5-A", "vize": 50, "final": 90, "hobiler": ["dövüş sanatları", "tarih okumak", "yemek yapmak"]}]
#
#collection.insert_many(data)

#print(collection.count_documents({}))

#for i in collection.find({"vize": 50, "hobiler": ["belgesel", "sinema", "tiyatro"]}):
#    pprint(i)

#for i in collection.find({"isim": "samet"}, {"vize": 1, "final": 1}):
#    pprint(i)

#for i in collection.find({"final": 50}, {"isim": 1, "soyisim": 1}):
#    print(i)

#for i in collection.find({"sınıfı": "6-A"}, {"isim": 1, "soyisim": 1}):
#    print(i)

#for i in collection.find({}, {"hobiler": 1}):
#    print(i)

#for i in collection.find({}, {"_id": 0, "isim": 1, "soyisim": 1}):
#    print(i)

#print(collection.find_one({"_id": ObjectId("661590256f9e9378e73f7d7b")}))

#for i in collection.find():
#    print(i)
#print("_"*50)

#print(collection.find_one({"_id": ObjectId("6615940e925414b65541a4f0")}))
#print(collection.find_one({"_id": ObjectId('6615940e925414b65541a4ef')}))

#uu = uuid.uuid4()
#data = {"_id": str(uu), "isim": "necdet", "soyisim": "ersan", "sınıfı": "7-A", "vize": 30, "final": 90}
#
#collection.insert_one(data)

#uu = uuid.uuid4()
#data = {"_id": str(uu), "isim": "mehmetcan", "soyisim": "keser", "sınıfı": "7-A", "vize": 40, "final": 60}
#
#collection.insert_one(data)

#print(collection.find_one({"_id": "357a3714-5e82-45c4-97b5-7725753a86ce"}))

#print(collection.find_one({"_id": ObjectId('6615940e925414b65541a4ee')}))

#print(collection.count_documents({"isim": "samet"}))
#print(collection.count_documents({"sınıfı": "6-A"}))
#print(collection.count_documents({"final": 90}))

#for i in collection.find().limit(5):
#    print(i)

#for i in collection.find().sort("isim", -1):
#    print(i)


#for i in collection.find().sort("soyisim", 1):
#    print(i)

#for i in collection.find().sort("vize", 1):
#    print(i)

#for i in collection.find().sort("final", -1):
#    print(i)

#for i in collection.find().sort("sınıfı", 1):
#    print(i)

#for i in collection.find().limit(5).sort("isim", 1):
#    print(i)

#for i in collection.find().sort("soyisim", -1).limit(7):
#    print(i)

#data = ({"isim": "fatih", "soyisim": "inci", "sınıfı": "8-A", "vize": 80, "final": 90, "hobiler": ["tenis", "müzik", "seyahat"],
#         "öğretmenlerin öğrenci hakkındaki görüşleri": [{"matematik öğretmeni ismi": "alper", "görüşü": "fatih inci matematikte sınıfın en iyilerinden fakat geometrisi biraz zayıf"},
#                                                        {"türkçe öğretmeni ismi": "nazife", "görüşü": "fatih inci'nin sözel derslerlerde kendini geliştirmesi lazım"},
#                                                        {"ingilizce öğretmeni ismi": "saliha", "görüşü": "fatih inci'nin ingilizce sınavlarından aldığı yüksek notlar derse olan ilgisini gösteriyor"}]})
#
#collection.insert_one(data)

#data = ({"isim": "nedim", "soyisim": "yaver", "sınıfı": "6-A", "vize": 50, "final": 70, "hobiler": ["bisiklet sürmek", "motorsiklet sürmek", "arabayla gezmek"],
#         "öğretmenlerin öğrenci hakkındaki görüşleri": [{"matematik öğretmeni ismi": "alper", "görüşü": "nedim yaver matematikte son sınavından iyi not alırsa dersten geçebilir"},
#                                                        {"türkçe öğretmeni ismi": "nazife", "görüşü": "nedim yaver'in türkçe ders notları ortalamanın altında"},
#                                                        {"ingilizce öğretmeni ismi": "saliha", "görüşü": "nedim yaver'in ingilizce grameri çok zayıf"}]})
#
#collection.insert_one(data)

#for i in collection.find({"final": {"$gt": 50}}):
#    print(i)

#for i in collection.find({"vize": {"$lt": 50}}):
#    print(i)

#for i in collection.find({"sınıfı": {"$gte": "7-A"}}):
#    print(i)

#for i in collection.find({"sınıfı": {"$lte": "7-A"}}):
#    print(i)

#for  i in collection.find({"vize": {"$gt": 60}, "sınıfı": "8-A"}):
#    print(i)

#for i in collection.find({"final": {"$lt": 40}, "sınıfı": "6-A"}):
#    print(i)

#for i in collection.find({"sınıfı": {"$eq": "7-A"}, "final": {"$ne": 50}}):
#    print(i)

#for i in collection.find({"sınıfı": {"$ne": "6-A"}, "vize": {"$eq": 50}}):
#    print(i)

#for i in collection.find({"$or": [{"vize": 40}, {"vize": 80}]}):
#    print(i)

#for i in collection.find({"$or": [{"final": 70}, {"sınıfı": "7-A"}]}):
#    print(i)

#for i in collection.find({"$or": [{"vize": {"$lte": 50}, "final": {"$gte": 50}}]}):
#    print(i)

#for i in collection.find({"$and": [{"vize": {"$lte": 40}}, {"sınıfı": {"$lte": "7-A"}}]}):
#    print(i)

#for i in collection.find({"$and": [{"final": {"$eq": 90}}, {"sınıfı": {"$eq": "8-A"}}]}):
#    print(i)

#for i in collection.find({"$and": [{"sınıfı": {"$ne": "7-A"}}, {"isim": {"$gte": "k"}}]}):
#    print(i)

#for i in collection.find({"$and": [{"soyisim": {"$lte": "m"}}, {"final": {"$gte": 70}}]}):
#    print(i)

#for i in collection.find({"final": {"$in": [50, 60, 70]}}):
#    print(i)

#for i in collection.find({"sınıfı": {"$in": ["7-A", "8-A"]}}):
#    print(i)

#for i in collection.find({"final": {"$nin": [90, 60, 50]}}):
#    print(i)

#for i in collection.find({"vize": {"$nin": [20, 30, 40, 50, 60, 70]}}):
#    print(i)

#for i in collection.find({"sınıfı": {"$in": ["7-A", "8-A"]}, "vize": {"$nin": [50, 60, 70]}}):
#    print(i)

#for i in collection.find({"hobiler": "tenis"}):
#    print(i)

#for i in collection.find({"hobiler": "futbol"}):
#    print(i)

#for i in collection.find({"hobiler": ["tenis"]}):
#    print(i)

#for i in collection.find({"hobiler": ["belgesel", "sinema", "tiyatro"]}):
#    print(i)

#for i in collection.find({"hobiler": ["tenis", "seyahat"]}):
#    print(i)

#for i in collection.find({"hobiler": {"$all": ["futbol", "voleybol"]}}):
#    print(i)

#for i in collection.find({"öğretmenlerin öğrenci hakkındaki görüşleri.matematik öğretmeni ismi": "alper"}):
    #pprint(i)

#for i in collection.find({"öğretmenlerin öğrenci hakkındaki görüşleri.türkçe öğretmeni ismi": "sevim"}):
    #pprint(i)

#for i in collection.find({"öğretmenlerin öğrenci hakkındaki görüşleri.ingilizce öğretmeni ismi": "saliha"}):
#    pprint(i)

#for i in collection.find({"öğretmenlerin öğrenci hakkındaki görüşleri.türkçe öğretmeni ismi": "nazife"}):
#    print(i)

#for i in collection.find({"öğretmenlerin öğrenci hakkındaki görüşleri.matematik öğretmeni ismi": "alican"}):
#    print(i)

#for i in collection.find({"öğretmenlerin öğrenci hakkındaki görüşleri.türkçe öğretmeni ismi": "sevim"}):
#    print(i)

#for i in collection.find({"öğretmenlerin öğrenci hakkındaki görüşleri.ingilizce öğretmeni ismi": "serpil"}):
#    print(i)

#print(collection.delete_one({"_id": ObjectId("661590256f9e9378e73f7d7b")}))

#print(collection.delete_many({"vize": {"$lte": 20}}))

#print(collection.delete_many({"final": {"$eq": 40}}))

#print(collection.delete_one({"_id": "9539af75-4d21-4fea-bd4d-3eb210235496"}))

#print(collection.update_one({"_id": ObjectId("66159287951919be6a2f3a58")}, {"$set": {"vize": 95, "final": 95, "sınıfı": "8-A"}}))

#print(collection.update_one({"_id": ObjectId("66159287951919be6a2f3a5a")}, {"$set": {"isim": "nurullah", "soyisim": "timur", "vize": 85, "final": 85, "sınıfı": "7-A"}}))

#print(collection.update_many({"isim": "samet"}, {"$set": {"isim": "koray"}}))

#print(collection.update_many({"final": 90}, {"$set": {"vize": 35}}))

#print(collection.update_one({"_id": ObjectId("66159287951919be6a2f3a58")}, {"$inc": {"vize": 3}}))

#print(collection.update_one({"_id": ObjectId("66159287951919be6a2f3a5a")}, {"$inc": {"final": 4}}))

#print(collection.update_one({"_id": ObjectId("6615940e925414b65541a4ef")}, {"$inc": {"vize": -15}}))

#print(collection.update_one({"_id": "357a3714-5e82-45c4-97b5-7725753a86ce"}, {"$inc": {"final": -45}}))

#print(collection.update_one({"_id": ObjectId("66167417bc8f68826de9ba79")}, {"$pull": {"hobiler": "seyahat"}}))

#print(collection.update_one({"_id": ObjectId("6615940e925414b65541a4ef")}, {"$pull": {"hobiler": "voleybol"}}))

#print(collection.update_one({"soyisim": "berk"}, {"$pull": {"hobiler": "yemek yapmak"}}))

#print(collection.update_one({"_id": ObjectId("66159287951919be6a2f3a58")}, {"$pull": {"hobiler": "belgesel"}}))

#print(collection.update_one({"_id": ObjectId("66159287951919be6a2f3a58")}, {"$push": {"hobiler": "dans etmek"}}))

#print(collection.update_one({"_id": ObjectId("66159287951919be6a2f3a5a")}, {"$push": {"hobiler": "temizlik yapmak"}}))

#print(collection.update_one({"soyisim": "berk"}, {"$push": {"hobiler": "resim yapmak"}}))

#print(collection.update_many({"sınıfı": "8-A"}, {"$push": {"hobiler": "yeni bir dil öğrenmek"}}))

#print(collection.update_many({"sınıfı": "8-A"}, {"$pull": {"hobiler": "yeni bir dil öğrenmek"}}))

#print(collection.update_many({"sınıfı": "7-A"}, {"$push": {"hobiler": "araba sürmek"}}))

#print(collection.update_one({"_id": ObjectId("66159287951919be6a2f3a58")}, {"$push": {"hobiler": {"$each": ["müzik dinlemek", "piyano çalmak", "gitar çalmak"]}}}))

#print(collection.update_many({"sınıfı": "7-A"}, {"$push": {"hobiler": {"$each": ["yüzmek", "koşu yapmak", "uzun atlama", "güreş"]}}}))

#print(collection.update_many({"isim": "koray"}, {"$push": {"hobiler": {"$each": ["tarih", "coğrafya", "biyoloji"]}}}))

#print(collection.update_one({"_id": "357a3714-5e82-45c4-97b5-7725753a86ce"}, {"$push": {"hobiler": {"$each": ["matematik", "fizik", "geometri"]}}}))

#print(collection.update_one({"_id": ObjectId("66167936cd3cfd6780b17ce7")}, {"$inc": {"final": 60}}))

#print(collection.update_one({"isim": "nedim"}, {"$max": {"vize": 90}}))

#print(collection.update_one({"isim": "nedim"}, {"$max": {"vize": 99}}))

#print(collection.update_one({"isim": "fatih"}, {"$max": {"vize": 91}}))

#print(collection.update_one({"isim": "fatih"}, {"$max": {"final": 92}}))

#print(collection.update_one({"isim": "mehmetcan"}, {"$min": {"vize": 33}}))

#print(collection.update_one({"isim": "mehmetcan"}, {"$min": {"final": 12}}))

#print(collection.update_many({"sınıfı": "7-A"}, {"$max": {"vize": 50}}))

#print(collection.update_many({"sınıfı": "7-A"}, {"$max": {"final": 40}}))

#print(collection.update_many({"sınıfı": "8-A"}, {"$max": {"vize": 90}}))

#print(collection.update_many({"sınıfı": "8-A"}, {"$max": {"final": "60"}}))

#print(collection.update_many({"sınıfı": "8-A"}, {"$set": {"final": 88}}))

#print(collection.update_many({"sınıfı": "8-A"}, {"$max": {"final": 93}}))

#print(collection.update_many({"sınıfı": "8-A"}, {"$min": {"vize": 80}}))

#print(collection.update_many({"sınıfı": "7-A"}, {"$min": {"vize": 30}}))

#print(collection.update_one({"isim": "nedim"}, {"$mul": {"final": 2.5}}))

#print(collection.update_many({"sınıfı": "7-A"}, {"$mul": {"vize": 3.1}}))

#print(collection.update_one({"isim": "nedim"}, {"$mul": {"final": 1.2}}))

#print(collection.update_one({"soyisim": "yaver"}, {"$rename": {"isim": "name"}}))

#print(collection.update_one({"name": "nedim"}, {"$rename": {"hobiler": "hobbies"}}))

#print(collection.update_many({"sınıfı": "7-A"}, {"$rename": {"soyisim": "lastname"}}))

#print(collection.update_many({"sınıfı": "8-A"}, {"$rename": {"isim": "name", "soyisim": "lastname"}}))

#print(collection.update_many({"sınıfı": "7-A"}, {"$rename": {"lastname": "soyisim"}}))

#print(collection.update_many({"sınıfı": "8-A"}, {"$rename": {"name": "adı", "lastname": "soyadı", "hobiler": "hobbies"}}))

#uu = uuid.uuid4()
#print(collection.update_one({"_id": str(uu)}, {"$set": {"isim": "kenan", "soyisim": "bekir"}, "$setOnInsert": {"vize": 100, "final": 90, "bölümü": "türkçe-matematik", "sevdiği dersler": ["geometri", "tarih", "coğrafya"]}}, upsert=True))

#print(collection.update_one({"adı": "niyazi", "soyadı": "sertan"}, {"$set": {"vize": 77, "final": 79}, "$setOnInsert": {"bölümü": "türkçe-matematik", "sevdiği dersler": ["fizik", "kimya", "biyoloji"]}}, upsert=True))

#print(collection.update_one({"adı": "onur", "soyadı": "çivi", "vize": 18, "final": 26}, {"$setOnInsert": {"bölümü": "tarih", "en sevdiği ders": "türkçe", "boyu": 168, "kilosu": 60, "yaşı": 15}}, upsert=True))

#print(collection.update_one({"adı": "ercan", "soyadı": "yılmaz"}, {"$setOnInsert": {"hobileri": ["yüzme", "futbol", "fitness", "basketbol"], "fobileri": ["kapalı alan", "yükseklik"], "aylık okul harçlığı": 1000, "boyu": 177, "kilosu": 72, "yaşı": 18}}, upsert=True))

#print(collection.update_one({"adı": "yener", "soyadı": "albayrak"}, {"$setOnInsert": {"cinsiyeti": "erkek", "memleketi": "adana", "en başarısız olduğu dersler": ["matematik", "kimya"]}}, upsert=True))

#print(collection.update_one({"isim": "ali", "soyisim": "şahin"}, {"$setOnInsert": {"aylık okul harçlığı": 1200, "memleketi": "izmir", "yaşı": 17}}, upsert=True))

#print(collection.update_one({"isim": "veli", "soyisim": "oğuz"},
# {"$setOnInsert": {"hobiler": ["balık tutmak", "seyahat", "bisiklet binmek"],
# "en başarılı olduğu ders": "fizik",
# "en başarısız olduğu ders": "edebiyat",
# "not ortalaması": 85,
# "boyu": 170,
# "kilosu": 68,
# "yaşı": 16,
# "vize": 90,
# "final":80,
# "memleketi": "bursa",}},
# upsert=True))

#collection.find_one_and_update({"adı": "koray"}, {"$inc": {"vize": -10}})

#collection.find_one_and_update({"sınıfı": "7-A"}, {"$inc": {"vize": 7}})

#collection.find_one_and_update({"soyisim": "timur"}, {"$set": {"isim": "orkan"}})

#collection.find_one_and_update({"_id": ObjectId("6615940e925414b65541a4f0")}, {"$set": {"soyadı": "berker"}})

#collection.find_one_and_update({"_id": "357a3714-5e82-45c4-97b5-7725753a86ce"}, {"$set": {"final": 45}})

#collection.find_one_and_delete({"_id": ObjectId("661934ed7b16b50c75a6577f")})

#collection.find_one_and_delete({"soyadı": "sertan"})

#collection.find_one_and_replace({"yaşı": 13}, {"adı": "namık", "soyadı": "ak", "yaşı": 14, "vize": 50, "final": 70, "sınıfı": "6-A", "boyu": 165, "kilosu": 62})

#collection.find_one_and_replace({"_id": "4aef7df9-5c1b-4d47-98e6-6b87ad314dd2"}, {"adı": "murat", "soyadı": "akar", "vize": 40, "final": 45, "bölümü": "ingilizce", "başarısız olduğu dersler": ["kimya", "biyoloji", "coğrafya"]})

#collection.find_one_and_replace({"isim": "metin"}, {"isim": "burak", "soyisim": "yaman", "final": 32, "vize": 44, "boy": 170, "kilo": 65, "yaş": 20, "sınıfı": "6-A", "aylık okul harçlığı": 1300, "memleketi": "giresun"})

#collection.find_one_and_replace({"_id": ObjectId("66159287951919be6a2f3a58")}, {"adı": "soner", "soyadı": "uzun", "vize": 35, "final": 90, "aylık okul harçlığı": 1600, "hobileri": ["piyano çalmak", "gitar çalmak", "keman çalmak", "flüt çalmak"]})

#for i in collection.find().sort("vize", 1):
#    print(i)

#for i in collection.find().sort("final", -1):
#    print(i)

#print(collection.count_documents({}))

#print(database.list_collection_names())

#collection.delete_one({"adı": "namık"})

#collection.delete_many({"sınıfı": "7-A"})

#print(collection.distinct("adı"))

#print(collection.distinct("soyadı"))

#print(collection.distinct("aylık okul harçlığı"))

#print(collection.distinct("isim"))

#print(collection.distinct("hobileri"))

#print(collection.distinct("memleketi"))

#for i in collection.find().limit(4):
#    print(i)

#for i in collection.find().skip(6):
#    print(i)

#for i in collection.index_information():
#    print(i)

#pprint(collection.find({"sınıfı": "8-A"}).explain())

#pprint(collection.create_index({"final": 3}))
#
#pprint(collection.index_information())
#
#pprint(collection.find({"final": 90}).explain())
#
#print(collection.estimated_document_count())

#print(database.create_collection("öğretmenler"))

#datas = [{"isim": "cemil", "soyisim": "şener", "branş": "matematik", "maaş": 34000},
#         {"isim": "selim", "soyisim": "yavuz", "branş": "coğrafya", "maaş": 33500},
#         {"isim": "mehmet", "soyisim": "alp", "branş": "tarih", "maaş": 35000},
#         {"isim": "nurettin", "soyisim": "ok", "branş": "türkçe", "maaş": 32000},
#         {"isim": "kamil", "soyisim": "sever", "branş": "fizik", "maaş": 36000},
#         {"isim": "güngör", "soyisim": "demir", "branş": "kimya", "maaş": 36500},
#         {"isim": "uğur", "soyisim": "doğan", "branş": "edebiyat", "maaş": 32500},
#         {"isim": "umut", "soyisim": "sarı", "branş": "biyoloji", "maaş": 35500}]
#
#collection.insert_many(datas)

#collection.delete_many({})

#collection.delete_one({})

#print(collection.distinct("maaş"))

#print(collection.count_documents({}))

#print(database.list_collection_names())

#print(database.drop_collection("öğretmenler"))

#print(collection.drop())

#for i in collection.aggregate([
#    {"$match": {"adı": "soner"}},
#    {"$project": {
#        "dizi_mi_1": {"$isArray": "$vize"},
#        "dizi_mi_2": {"$isArray": "$hobileri"}}}]):
#    print(i)







#for i in collection.aggregate([{"$match": {"isim": "kenan"}},
#                               {"$project": {"dizi_mi_1": {"$isArray": "$vize"}, "dizi_mi_2": {"$isArray": "$bölümü"}, "dizi_mi_3": {"$isArray": "$sevdiği dersler"}}}]):
#    print(i)


#for i in collection.aggregate([{"$match": {"_id": ObjectId("66167936cd3cfd6780b17ce7")}},
#                               {"$project": {"dizi_mi_1": {"$isArray": "$öğretmenlerin öğrenci hakkındaki görüşleri"},
#                                             "dizi_mi_2": {"$isArray": "$hobbies"},
#                                             "dizi_mi_3": {"$isArray": "$sınıfı"},
#                                             "dizi_mi_4": {"$isArray": "$final"},
#                                             "dizi_mi_5": {"$isArray": "$vize"}}}]):
#
#    pprint(i)

#for i in collection.aggregate([{"$match": {"_id": ObjectId("66167417bc8f68826de9ba79")}},
#                               {"$project":   {"dizi_mi_1": {"$isArray": "$adı"},
                #                               "dizi_mi_2": {"$isArray": "$soyadı"},
                #                               "dizi_mi_3": {"$isArray": "$sınıfı"},
                #                               "dizi_mi_4": {"$isArray": "$vize"},
                #                               "dizi_mi_5": {"$isArray": "$öğretmenlerin öğrenci hakkındaki görüşleri"},
                #                               "dizi_mi_6": {"$isArray": "$hobbies"}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"_id": ObjectId("661937607b16b50c75add7a8")}},
#                               {"$project": {"dizi_mi_1": {"$isArray": "$isim"},
#                                             "dizi_mi_2": {"$isArray": "$soyisim"},
#                                             "dizi_mi_3": {"$isArray": "$boyu"},
#                                             "dizi_mi_4": {"$isArray": "$kilosu"},
#                                             "dizi_mi_5": {"$isArray": "$memleketi"},
#                                             "dizi_mi_6": {"$isArray": "$yaşı"},
#                                             "dizi_mi_7": {"$isArray": "$hobiler"},
#                                             "dizi_mi_8": {"$isArray": "$not ortalaması"}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"_id": ObjectId("66167936cd3cfd6780b17ce7")}},
#                               {"$project": {"dizi_mi_1": {"$isArray": "$öğretmenlerin öğrenci hakkındaki görüşleri.görüşü"}}}]):
#    pprint(i)

#datas = [{"isim": "osman", "soyisim": "tuna", "yaş": 12, "sınıfı": "7-A", "favori oyunlar": {"evde": ["satranç", "tavla", "okey"], "dışarda": ["futbol", "basketbol", "voleybol"]}},
#         {"isim": "şener", "soyisim": "güler", "yaş": 14, "sınıfı": "8-A", "favori yemekler": {"evde": ["fasulye", "patlıcan", "makarna"], "dışarda": ["pizza", "hamburger", "döner"]}},
#         {"isim": "şükrü", "soyisim": "beşerler", "yaş": 15, "sınıfı": "8-A", "favori renkler": {"eskiden": ["kırmızı", "yeşil", "mor"], "şuan": ["beyaz", "mavi", "turuncu"]}}]
#
#collection.insert_many(datas)

#for i in collection.aggregate([{"$match": {"_id": ObjectId("661aff14981138dece6eb9c8")}},
#                               {"$project": {"dizi_mi_1": {"$isArray": "$favori oyunlar.evde"}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"isim": "şener"}},
#                               {"$project": {"dizi_mi_1": {"$isArray": "$favori yemekler.dışarda"}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"soyisim": "beşerler"}},
#                               {"$project": {"dizi_mi_1": {"$isArray": "$favori renkler.şuan"}}}]):
#    pprint(i)

#data = {"isim": "latif", "soyisim": "yaman", "yaş": 13, "sınıfı": "6-A", "favori içecekler": {"evde": "ayran"}, "dışarda": ["cola", "sprite", "fanta"]}
#
#collection.insert_one(data)

#for i in collection.aggregate([{"$match": {"isim": "latif"}},
#                               {"$project": {"dizi_mi_1": {"$isArray": "$favori içecekler.evde"}}}]):
#    pprint(i)







#for i in collection.aggregate([{"$match": {"adı": "soner"}},
#                               {"$project": {"eleman sayısı": {"$size": "$hobileri"}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"_id": ObjectId("6615940e925414b65541a4f0")}},
#                               {"$project": {"eleman sayısı": {"$size": "$hobbies"}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"adı": "fatih"}},
#                               {"$project": {"eleman sayısı": {"$size": "$öğretmenlerin öğrenci hakkındaki görüşleri"}}}]):
#    pprint(i)


#for i in collection.aggregate([{"$match": {"soyisim": "yaver"}},
#                               {"$project": {"eleman sayısı": {"$size": "$hobbies"}}}]):
#    pprint(i)


#for i in collection.aggregate([{"$match": {"isim": "osman"}},
#                               {"$project": {"eleman sayısı": {"$size": "$favori oyunlar.evde"}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"_id": ObjectId("661aff14981138dece6eb9c8")}},
#                               {"$project": {"eleman sayısı": {"$size": "$favori oyunlar.dışarda"}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"isim": "şener"}},
#                               {"$project": {"eleman sayısı": {"$size": "$favori yemekler.evde"}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"soyisim": "güler"}},
#                               {"$project": {"eleman sayısı": {"$size": "$favori yemekler.dışarda"}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"isim": "latif"}},
#                               {"$project": {"eleman sayısı": {"$size": "$dışarda"}}}]):
#    pprint(i)







#for i in collection.aggregate([{"$match": {"adı": "soner"}},
#                               {"$project": {
#                                   "eleman adı1": {"$arrayElemAt": ["$hobileri", 2]},
#                                   "eleman adı2": {"$arrayElemAt": ["$hobileri", -1]},
#                                   "eleman adı3": {"$arrayElemAt": ["$hobileri", 0]},
#                                   "eleman adı4": {"$arrayElemAt": ["$hobileri", 1]}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"_id": ObjectId("6615940e925414b65541a4f0")}},
#                               {"$project": {
#                                   "eleman adı1": {"$arrayElemAt": ["$hobbies", 4]},
#                                   "eleman adı2": {"$arrayElemAt": ["$hobbies", 1]},
#                                   "eleman adı3": {"$arrayElemAt": ["$hobbies", 5]}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"isim": "şükrü"}},
#                               {"$project": {
#                                    "eleman adı1": {"$arrayElemAt": ["$favori renkler.eskiden", 7]},
#                                    "eleman adı2": {"$arrayElemAt": ["$favori renkler.eskiden", 3]},
#                                    "eleman adı3": {"$arrayElemAt": ["$favori renkler.eskiden", 5]},
#                                    "eleman adı4": {"$arrayElemAt": ["$favori renkler.eskiden", 2]},
#                                    "eleman adı5": {"$arrayElemAt": ["$favori renkler.eskiden", 6]}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"isim": "şener"}},
#                               {"$project": {
#                                    "eleman adı1": {"$arrayElemAt": ["$favori yemekler.evde", 3]},
#                                    "eleman adı2": {"$arrayElemAt": ["$favori yemekler.evde", 5]},
#                                    "eleman adı3": {"$arrayElemAt": ["$favori yemekler.evde", 1]},
#                                    "eleman adı4": {"$arrayElemAt": ["$favori yemekler.evde", 0]}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"soyisim": "güler"}},
#                               {"$project": {
#                                    "eleman adı1": {"$arrayElemAt": ["$favori yemekler.dışarda", 2]},
#                                    "eleman adı2": {"$arrayElemAt": ["$favori yemekler.dışarda", 0]},
#                                    "eleman adı3": {"$arrayElemAt": ["$favori yemekler.dışarda", -1]},
#                                    "eleman adı4": {"$arrayElemAt": ["$favori yemekler.dışarda", -2]}}}]):
#    pprint(i)


#for i in collection.aggregate([{"$match": {"_id": ObjectId("661aff14981138dece6eb9c8")}},
#                               {"$project": {
#                                    "eleman adı1": {"$arrayElemAt": ["$favori oyunlar.dışarda", -1]},
#                                    "eleman adı2": {"$arrayElemAt": ["$favori oyunlar.dışarda", 0]},
#                                    "eleman adı3": {"$arrayElemAt": ["$favori oyunlar.dışarda", 2]}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"isim": "osman"}},
#                               {"$project": {
#                                   "eleman adı1": {"$arrayElemAt": ["$favori oyunlar.evde", -1]},
#                                   "eleman adı2": {"$arrayElemAt": ["$favori oyunlar.evde", 0]}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"isim": "şener"}},
#                               {"$project": {
#                                    "eleman adı1": {"$arrayElemAt": ["$favori yemekler.evde", 1]},
#                                    "eleman adı2": {"$arrayElemAt": ["$favori yemekler.evde", 2]},
#                                    "eleman adı3": {"$arrayElemAt": ["$favori yemekler.evde", 3]},
#                                    "eleman adı4": {"$arrayElemAt": ["$favori yemekler.dışarda", 0]},
#                                    "eleman adı5": {"$arrayElemAt": ["$favori yemekler.dışarda", -1]},
#                                    "eleman adı6": {"$arrayElemAt": ["$favori yemekler.dışarda", 4]}}}]):
#     pprint(i)

#for i in collection.aggregate([{"$match": {"adı": "murat"}},
#                               {"$project": {
#                                   "eleman adı1": {"$arrayElemAt": ["$başarısız olduğu dersler", -1]},
#                                   "eleman adı2": {"$arrayElemAt": ["$başarısız olduğu dersler", -2]},
#                                   "eleman adı3": {"$arrayElemAt": ["$başarısız olduğu dersler", -3]}}}]):
#    pprint(i)

#for i in collection.aggregate([{"$match": {"_id": "e065d3f0-dca8-496a-b765-0e60b23f8649"}},
#                               {"$project": {
#                                   "eleman adı1": {"$arrayElemAt": ["$sevdiği dersler", 0]},
#                                   "eleman adı2": {"$arrayElemAt": ["$sevdiği dersler", -1]}}}]):
#    pprint(i)


#for i in collection.aggregate([{"$match": {"adı": "ercan"}},
#                               {"$project": {
#                                   "eleman adı1": {"$arrayElemAt": ["$fobileri", 0]},
#                                   "eleman adı2": {"$arrayElemAt": ["$hobileri", 0]}}}]):
#    pprint(i)







#for i in collection.aggregate([{"$match": {"isim": "şükrü"}},
#                               {"$project": {
#                                   "birlestir": {"$concatArrays": ["$favori renkler.eskiden", "$favori renkler.şuan"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"isim": "şener"}},
#                               {"$project": {
#                                   "birlestir": {"$concatArrays": ["$favori yemekler.evde", "$favori yemekler.dışarda"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"_id": ObjectId("661aff14981138dece6eb9c8")}},
#                               {"$project": {
#                                   "birlestir": {"$concatArrays": ["$favori oyunlar.evde", "$favori oyunlar.dışarda"]}}}]):
#    print(i)


#for i in collection.aggregate([{"$match": {"adı": "ercan"}},
#                               {"$project": {
#                                   "birlestir": {"$concatArrays": ["$fobileri", "$hobileri"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"isim": "kenan"}},
#                               {"$project": {
#                                   "birlestir": {"$concatArrays": ["$bölümü", "$sevdiği dersler"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"name": "nedim"}},
#                               {"$project": {
#                                   "birlestir": {"$concatArrays": ["$öğretmenlerin öğrenci hakkındaki görüşleri", "$hobbies"]}}}]):
#       print(i)


#for i in collection.aggregate([{"$match": {"adı": "fatih"}},
#                               {"$project": {
#                                      "birlestir": {"$concatArrays": ["$öğretmenlerin öğrenci hakkındaki görüşleri", "$hobbies"]}}}]):
#       print(i)


#for i in collection.aggregate([{"$match": {"isim": "cumali"}},
#                               {"$project": {
#                                   "birlestir": {"$concatArrays": ["$hobileri", "$fobileri", "$en sevdiği yemekler", "$en sevdiği dersler", "$en sevdiği sporlar", "$en sevdiği içecekler"]}}}]):
#    print(i)







#for i in collection.aggregate([{"$match": {"adı": "soner"}},
#                               {"$project": {
#                                   "ters cevir": {"$reverseArray": ["$hobileri"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"adı": "koray"}},
#                               {"$project": {
#                                   "ters cevir": {"$reverseArray": ["$hobbies"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"_id": ObjectId("66167417bc8f68826de9ba79")}},
#                               {"$project": {
#                                   "ters cevir": {"$reverseArray": ["$öğretmenlerin öğrenci hakkındaki görüşleri"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"isim": "osman"}},
#                               {"$project": {
#                                   "ters cevir": {"$reverseArray": ["$favori oyunlar.evde"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"soyisim": "tuna"}},
#                               {"$project": {
#                                   "ters cevir": {"$reverseArray": ["$favori oyunlar.dışarda"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"_id": ObjectId("661aff14981138dece6eb9ca")}},
#                               {"$project": {
#                                   "ters cevir": {"$reverseArray": ["$favori renkler.eskiden"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"isim": "şener"}},
#                               {"$project": {
#                                   "ters cevir": {"$reverseArray": ["$favori yemekler.evde"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"soyisim": "güler"}},
#                               {"$project": {
#                                   "ters cevir": {"$reverseArray": ["$favori yemekler.dışarda"]}}}]):
#    print(i)







#datas = [{"isim": "cevdet", "soyisim": "yıldırım", "yaş": 28, "sevdiği renkler": ["pembe", "mor", "yeşil", "siyah"]},
#         {"isim": "mustafa", "soyisim": "aksoy", "yaş": 28, "sevdiği renkler": ["siyah", "kırmızı", "beyaz", "mor"]},
#         {"isim": "haluk", "soyisim": "okan", "yaş": 28, "sevdiği renkler": ["kırmızı", "pembe", "siyah", "yeşil"]},
#         {"isim": "muzaffer", "soyisim": "erdem", "yaş": 28, "sevdiği renkler": ["kırmızı", "mor", "yeşil", "pembe"]},
#         {"isim": "osman", "soyisim": "gündoğan", "yaş": 25, "sevdiği renkler": ["turuncu", "eflatun", "sarı", "kahverengi"]},
#         {"isim": "tarık", "soyisim": "seçkin", "yaş": 25, "sevdiği renkler": ["kahverengi", "lacivert", "mavi", "turuncu"]},
#         {"isim": "tuna", "soyisim": "eryaman", "yaş": 25, "sevdiği renkler": ["kahverengi", "turuncu", "sarı", "mavi"]},
#         {"isim": "turgay", "soyisim": "beşer", "yaş": 25, "sevdiği renkler": ["eflatun", "sarı", "mavi", "lacivert"]},
#
#         {"isim": "vedat", "soyisim": "ateş", "yaş": 32, "sevdiği yemekler": ["makarna", "pilav", "pizza", "hamburger"]},
#         {"isim": "vehbi", "soyisim": "çolak", "yaş": 32, "sevdiği yemekler": ["döner", "iskender", "pilav", "pizza"]},
#         {"isim": "ramazan", "soyisim": "kartal", "yaş": 32, "sevdiği yemekler": ["iskender", "makarna", "hamburger", "döner"]},
#         {"isim": "şaban", "soyisim": "ozan", "yaş": 32, "sevdiği yemekler": ["pilav", "pizza", "makarna", "döner"]},
#         {"isim": "recai", "soyisim": "kılınç", "yaş": 36, "sevdiği yemekler": ["fasulye", "ıspanak", "semizotu", "karnabahar"]},
#         {"isim": "sezai", "soyisim": "görkemli", "yaş": 36, "sevdiği yemekler": ["brokoli", "patlıcan", "semizotu", "fasulye"]},
#         {"isim": "suat", "soyisim": "tatlı", "yaş": 36, "sevdiği yemekler": ["patlıcan", "ıspanak", "karnabahar", "brokoli"]},
#         {"isim": "harun", "soyisim": "duyar", "yaş": 36, "sevdiği yemekler": ["ıspanak", "brokoli", "fasulye", "patlıcan"]}]
#
#collection.insert_many(datas)

#datas = [{"isim": "turan", "soyisim": "aybars", "notlar": [40, 70, 50], "dersler": ["matematik", "geometri"]},
#         {"isim": "turan", "soyisim": "türkoğlu", "notlar": [30, 20, 90], "dersler": ["fizik", "kimya", "biyoloji"]},
#         {"isim": "turan", "soyisim": "alp", "notlar": [80, 30, 50], "dersler": ["türkçe", "edebiyat", "felsefe"]},
#         {"isim": "turan", "soyisim": "semiz", "notlar": [70, 60, 20], "dersler": ["tarih", "coğrafya"]},
#         {"isim": "turan", "soyisim": "yılmaz", "notlar": [10, 80, 90], "dersler": ["ingilizce", "fransızca", "almanca"]},
#         {"isim": "turan", "soyisim": "yıldırım", "notlar": [50, 60, 20], "dersler": ["din kültürü", "beden eğitimi", "müzik"]}]
#
#collection.insert_many(datas)







#print(collection.update_many({"yaş": 28}, {"$pull": {"sevdiği renkler": "pembe"}}))

#print(collection.update_many({"yaş": 25}, {"$pull": {"sevdiği renkler": "sarı"}}))

#print(collection.update_many({"yaş": 32}, {"$pull": {"sevdiği yemekler": "makarna"}}))

#print(collection.update_many({"yaş": 36}, {"$pull": {"sevdiği yemekler": "fasulye"}}))

#print(collection.update_many({"isim": "turan"}, {"$pull": {"notlar": 30}}))

#print(collection.update_many({"isim": "turan"}, {"$pull": {"notlar": {"$gt": 80}}}))

#print(collection.update_many({"isim": "turan"}, {"$pull": {"notlar": {"$lt": 30}}}))

#print(collection.update_many({"isim": "turan"}, {"$pull": {"notlar": {"$eq": 50}}}))

#print(collection.update_many({"isim": "turan"}, {"$pull": {"notlar": {"$ne": 100}}}))

#print(collection.update_many({"isim": "turan"}, {"$pull": {"notlar": {"$in": [30, 40]}}}))

#print(collection.update_many({"isim": "turan"}, {"$pull": {"notlar": {"$ne": 100}}}))

#print(collection.update_many({"isim": "turan"}, {"$pull": {"notlar": 50, "dersler": {"$in": ["felsefe", "fransızca"]}}}))

#print(collection.update_many({"isim": "turan"}, {"$pull": {"notlar": 10, "dersler": {"$in": ["müzik", "din kültürü", "beden eğitimi"]}}}))

#print(collection.update_many({"isim": "turan"}, {"$pull": {"notlar": {"$nin": [90, 80]}, "dersler": {"$in": ["tarih", "coğrafya", "ingilizce", "almanca"]}}}))







#datas = [{"isim": "orkan", "soyisim": "yalın", "kişisel bilgiler": {"memleketi": "ankara", "yaş": 23, "notları": [55, 60, 40, 20, 85]}},
#         {"isim": "tolga", "soyisim": "yalın", "kişisel bilgiler": {"memleketi": "sivas", "yaş": 22, "notları": [100, 45, 35, 90, 95]}},
#         {"isim": "enis", "soyisim": "yalın", "kişisel bilgiler": {"memleketi": "erzurum", "yaş": 20, "notları": [50, 70, 75, 80, 30]}}]
#
#print(collection.insert_many(datas))


#print(collection.update_one({"adı": "koray"}, {"$pop": {"hobbies": 1}}))

#print(collection.update_one({"adı": "koray"}, {"$pop": {"hobbies": -1}}))

#print(collection.update_one({"name": "nedim"}, {"$pop": {"hobbies": -1}}))

#print(collection.update_one({"_id": "e065d3f0-dca8-496a-b765-0e60b23f8649"}, {"$pop": {"sevdiği dersler": 1}}))

#print(collection.update_one({"isim": "cumali"}, {"$pop": {"en sevdiği içecekler": -1}}))

#print(collection.update_one({"isim": "cumali"}, {"$pop": {"en sevdiği sporlar": 1}}))

#print(collection.update_one({"isim": "savaş"}, {"$pop": {"kişisel bilgiler.notları": 1}}))

#print(collection.update_many({"soyisim": "yalın"}, {"$pop": {"kişisel bilgiler.notları": -1}}))

#print(collection.update_many({"soyisim": "yalın"}, {"$pop": {"kişisel bilgiler.notları": 1}}))

#print(collection.update_many({"soyisim": "yalın"}, {"$pop": {"kişisel bilgiler.notları": 1}}))

#print(collection.update_many({"soyisim": "yalın"}, {"$pop": {"kişisel bilgiler.notları": -1}}))







#datas = [{"isim": "orkan", "soyisim": "yalın", "kişisel bilgiler": {"memleketi": "ankara", "yaş": 23, "bildiği diller": ["java", "php", "python", "c", "c##"]}},
#         {"isim": "tolga", "soyisim": "yalın", "kişisel bilgiler": {"memleketi": "sivas", "yaş": 22, "bildiği diller": ["c##", "php", "ruby", "python"]}},
#         {"isim": "enis", "soyisim": "yalın", "kişisel bilgiler": {"memleketi": "erzurum", "yaş": 20, "bildiği diller": ["python", "c", "c##", "php", "java"]}}]
#
#print(collection.insert_many(datas))

#data = {"isim": "kerem", "soyisim": "yılmaz", "kişisel bilgiler": {"memleketi": "izmir", "yaş": 25, "sevdiği renkler": ["mavi", "kırmızı", "beyaz", "turuncu", "sarı", "eflatun", "mor", "pembe"]}}
#
#collection.insert_one(data)

#datas = [{"isim": "ibrahim", "soyisim": "şişman", "hobiler": ["bisiklet", "motorsiklet", "yüzme", "koşu", "futbol", "kitap", "seyahat", "araba"]},
#         {"isim": "ibrahim", "soyisim": "esen",  "hobiler": ["araba", "kitap", "yüzme", "futbol", "voleybol", "hentbol"]},
#         {"isim": "ibrahim", "soyisim": "bekir",  "hobiler": ["futbol", "yüzme", "kitap", "araba", "balık tutmak", "dans etmek", "film izlemek"]}]
#
#print(collection.insert_many(datas))


#print(collection.update_many({"soyisim": "yalın"}, {"$pullAll": {"kişisel bilgiler.bildiği diller": ["python", "php", "c##"]}}))

#print(collection.update_many({"soyisim": "yalın"}, {"$pullAll": {"kişisel bilgiler.bildiği diller": ["java", "c"]}}))

#print(collection.update_one({"isim": "kerem"}, {"$pullAll": {"kişisel bilgiler.sevdiği renkler": ["mavi", "kırmızı", "beyaz", "turuncu"]}}))

#print(collection.update_one({"isim": "kerem"}, {"$pullAll": {"kişisel bilgiler.sevdiği renkler": ["mor", "pembe"]}}))

#print(collection.update_one({"isim": "kerem"}, {"$pullAll": {"kişisel bilgiler.sevdiği renkler": ["eflatun", "sarı"]}}))

#print(collection.update_many({"isim": "ibrahim"}, {"$pullAll": {"hobiler": ["futbol", "yüzme", "kitap", "araba"]}}))

#print(collection.update_many({"isim": "ibrahim"}, {"$pullAll": {"hobiler": ["balık tutmak", "dans etmek", "film izlemek"]}}))







#print(collection.update_one({"isim": "tarık"}, {"$push": {"sevdiği renkler": "siyah"}}))

#print(collection.update_one({"_id": ObjectId("661d85dadf9b423a67c94680")}, {"$push": {"sevdiği renkler": "eflatun"}}))

#print(collection.update_one({"adı": "soner"}, {"$push": {"hobileri": "davul çalmak"}}))

#print(collection.update_one({"adı": "koray"}, {"$push": {"hobbies": "fizik"}}))

#print(collection.update_many({"isim": "ibrahim"}, {"$push": {"hobiler": "yurtdışına çıkmak"}}))

#print(collection.update_many({"isim": "ibrahim"}, {"$push": {"hobiler": "dalış yapmak"}}))

#print(collection.update_one({"adı": "soner"}, {"$push": {"hobileri": {"$each": ["org çalmak", "saz çalmak", "saksafon çalmak"]}}}))

#print(collection.update_one({"adı": "yener"}, {"$push": {"en başarısız olduğu dersler": {"$each": ["fizik", "biyoloji", "geometri", "ingilizce"]}}}))

#print(collection.update_one({"isim": "kenan"}, {"$push": {"sevdiği dersler": {"$each": ["fransızca", "türkçe", "edebiyat"]}}}))

#print(collection.update_one({"isim": "veli"}, {"$push": {"hobiler": {"$each": ["voleybol", "tenis", "hentbol", "beyzbol"]}}}))

#print(collection.update_many({"isim": "ibrahim"}, {"$push": {"hobiler": {"$each": ["dans etmek", "sinema", "yemek yapmak", "tiyatro"]}}}))

#print(collection.update_many({"isim": "ibrahim"}, {"$push": {"hobiler": {"$each": ["resim yapmak", "kitap okumak", "belgesel izlemek"]}}}))

#print(collection.update_many({"sınıfı": "8-A"}, {"$push": {"hobbies": {"$each": ["yemek yapmak", "roman okumak", "oyun oynamak", "yazılım öğrenmek"]}}}))

#print(collection.update_many({"yaş": 28}, {"$push": {"sevdiği renkler": {"$each": ["kiremit rengi", "limon sarısı", "turkuaz mavisi"]}}}))

#print(collection.update_many({"soyisim": "yalın"}, {"$push": {"kişisel bilgiler.bildiği diller": {"$each": ["css", "html", "bootstrap"]}}}))

#print(collection.update_many({"soyisim": "yalın"}, {"$push": {"kişisel bilgiler.bildiği diller": {"$each": ["opencv", "pandas", "numpy", "moviepy"]}}}))

#print(collection.update_many({"soyisim": "yalın"}, {"$push": {"kişisel bilgiler.bildiği diller": {"$each": ["mongodb", "sql", "mysql", "sqlite3"]}}}))

#print(collection.update_one({"isim": "hulusi"}, {"$push": {"kişisel bilgiler.yabancı diller": {"$each": ["türkçe", "almanca", "fransızca"]}}}))

#print(collection.update_one({"isim": "hulusi"}, {"$push": {"kişisel bilgiler.yabancı diller": {"$each": ["rusça", "çince", "japonca", "arapça"]}}}))

#print(collection.update_one({"isim": "hulusi"}, {"$push": {"kişisel bilgiler.yabancı diller": {"$each": ["lehçe", "farsça", "latince"]}}}))

#print(collection.update_one({"isim": "deniz"}, {"$push": {"kişisel bilgiler.arkadaşları": {"$each": ["ali", "berkan", "can", "dursun", "emel", "fadime"],
#                                                                                           "$sort": -1, "$slice": 50}}}))

#print(collection.update_one({"isim": "hulusi", "kişisel bilgiler.yabancı diller": "ispanyolca"},
#                            {"$set": {"kişisel bilgiler.yabancı diller.$": "hintçe"}}))

#print(collection.update_one({"isim": "hulusi", "kişisel bilgiler.yabancı diller": "almanca"},
#                            {"$set": {"kişisel bilgiler.yabancı diller.$": "macarca"}}))

#print(collection.update_one({"isim": "hulusi", "kişisel bilgiler.yabancı diller": "türkçe"},
#                            {"$set": {"kişisel bilgiler.yabancı diller.$": "korece"}}))

#print(collection.update_one({"isim": "hulusi", "kişisel bilgiler.yabancı diller": "arapça"},
#                            {"$set": {"kişisel bilgiler.yabancı diller.$": "bulgarca"}}))

#print(collection.update_one({"isim": "hulusi", "kişisel bilgiler.yabancı diller": "latince"},
#                            {"$set": {"kişisel bilgiler.yabancı diller.$": "makedonca"}}))

#print(collection.update_one({"adı": "soner", "hobileri": "piyano çalmak"},
#                            {"$set": {"hobileri.$": "yan flüt çalmak"}}))

#print(collection.update_one({"adı": "koray", "hobbies": "yazılım öğrenmek"},
#                            {"$set": {"hobbies.$": "vücut çalışmak"}}))

#print(collection.update_one({"adı": "fatih", "hobbies": "tenis"},
#                            {"$set": {"hobbies.$": "uzun atlama"}}))

#print(collection.update_one({"soyisim": "yaver", "hobbies": "arabayla gezmek"},
#                            {"$set": {"hobbies.$": "tekneyle gezmek"}}))

#print(collection.update_one({"adı": "murat", "başarısız olduğu dersler": "coğrafya"},
#                            {"$set": {"başarısız olduğu dersler.$": "felsefe"}}))

#print(collection.update_one({"soyadı": "albayrak", "en başarısız olduğu dersler": "matematik"},
#                            {"$set": {"en başarısız olduğu dersler.$": "fransızca"}}))


#data = {"isim": "cemal", "soyisim": "şanlı",
#        "ders durumu": [{"ders": "fizik", "vize": 60, "final": 70},
#                        {"ders": "kimya", "vize": 40, "final": 30},
#                        {"ders": "biyoloji", "vize": 20, "final": 90},
#                        {"ders": "matematik", "vize": 100, "final": 40}]}
#
#collection.insert_one(data)

#print(collection.update_one({"isim": "cemal", "ders durumu": {"$elemMatch": {"vize": {"$lt": 50}}}},
#                            {"$set": {"ders durumu.$.final": 150}}))

#print(collection.update_one({"isim": "cemal", "ders durumu": {"$elemMatch": {"vize": {"$eq": 100}}}},
#                            {"$set": {"ders durumu.$.final": 200}}))

#print(collection.update_many({"isim": "cemal", "ders durumu": {"$elemMatch": {"final": {"$ne": 300}}}},
#                             {"$set": {"ders durumu.$.vize": 10}}))

#print(collection.update_one({"isim": "cemal", "ders durumu": {"$elemMatch": {"final": {"$eq": 90}}}},
#                            {"$set": {"ders durumu.$.final": 1500}}))

#print(collection.update_one({"isim": "cemal", "ders durumu": {"$elemMatch": {"final": {"$eq": 200}}}},
#                            {"$set": {"soyisim": "bilir"}}))

#print(collection.update_one({"soyisim": "bilir", "ders durumu": {"$elemMatch": {"vize": {"$eq": 10}}}},
#                            {"$set": {"ders durumu.$.final": "finale girmedi"}}))

#print(collection.update_one({"isim": "cemal", "ders durumu": {"$elemMatch": {"final": {"$eq": 1500}}}},
#                            {"$set": {"ders durumu.$.vize": "vizeye girmedi"}}))

#print(collection.update_one({"isim": "cemal", "ders durumu": {"$elemMatch": {"ders": {"$eq": "matematik"}}}},
#                            {"$set": {"ders durumu.$.vize": 33, "ders durumu.$.final": 43}}))

#print(collection.update_one({"isim": "cemal", "ders durumu": {"$elemMatch": {"ders": {"$eq": "kimya"}}}},
#                            {"$set": {"ders durumu.$.vize": 12, "ders durumu.$.final": 22}}))

#print(collection.update_one({"isim": "cemal", "ders durumu": {"$elemMatch": {"ders": {"$eq": "biyoloji"}}}},
#                            {"$set": {"ders durumu.$.vize": 51, "ders durumu.$.final": 61}}))

#print(collection.update_one({"isim": "cemal", "ders durumu": {"$elemMatch": {"ders": {"$eq": "fizik"}}}},
#                            {"$set": {"ders durumu.$.vize": 100, "ders durumu.$.final": 100}}))

#print(collection.update_one({"isim": "cemal"}, {"$inc": {"ders durumu.$[].vize": 200}}))

#print(collection.update_one({"isim": "cemal"}, {"$inc": {"ders durumu.$[].final": -1000}}))

#print(collection.update_one({"isim": "cemal"}, {"$set": {"ders durumu.$[].vize": 50}}))

#print(collection.update_one({"isim": "cemal"}, {"$inc": {"ders durumu.$[].final": 1050}}))

#print(collection.update_one({"isim": "cemal"}, {"$inc": {"ders durumu.$[].final": -50}}))

#print(collection.update_one({"isim": "cemal"}, {"$set": {"ders durumu.$[].final": 40}}))

#datas = [{"isim": "sena", "soyisim": "başer", "sınıfı": "3-A", "points": [10, 20, 30]},
#         {"isim": "selma", "soyisim": "başer", "sınıfı": "3-A", "points": [10, 20, 30]},
#         {"isim": "ayşe", "soyisim": "izci", "sınıfı": "4-A", "points": [40, 50, 60]},
#         {"isim": "aynur", "soyisim": "izci", "sınıfı": "4-A", "points": [40, 50, 60]},
#         {"isim": "merve", "soyisim": "yıldız", "sınıfı": "5-A", "points": [70, 80, 90]},
#         {"isim": "meliha", "soyisim": "yıldız", "sınıfı": "5-A", "points": [70, 80, 90]}]
#
#collection.insert_many(datas)

#print(collection.update_many({"sınıfı": "3-A"}, {"$inc": {"points.$[]": 5}}))

#print(collection.update_many({"sınıfı": "4-A"}, {"$inc": {"points.$[]": -50}}))

#print(collection.update_many({"sınıfı": "5-A"}, {"$inc": {"points.$[]": 100}}))

#print(collection.update_many({"soyisim": "başer"}, {"$set": {"points.$[]": 40}}))

#print(collection.update_many({"soyisim": "izci"}, {"$set": {"points.$[]": 10}}))

#print(collection.update_many({"soyisim": "yıldız"}, {"$set": {"points.$[]": 0}}))



#print(collection.update_many({"sınıfı": "3-A"},
#                             {"$push": {"points": {"$each": [1000, 2000, 3000], "$position": 0}}}))

#print(collection.update_many({"sınıfı": "4-A"},
#                             {"$push": {"points": {"$each": [11, 21, 31, 41], "$position": 0}}}))

#print(collection.update_many({"sınıfı": "5-A"},
#                             {"$push": {"points": {"$each": [22, 32, 42, 52, 62], "$position": 0}}}))

#print(collection.update_many({"sınıfı": "3-A"},
#                             {"$push": {"points": {"$each": [111, 222, 333], "$position": 2}}}))

#print(collection.update_many({"sınıfı": "4-A"},
#                             {"$push": {"points": {"$each": [4040, 5050, 6060], "$position": -1}}}))

#print(collection.update_many({"sınıfı": "5-A"},
#                             {"$push": {"points": {"$each": ["a", "b", "c"], "$position": 4}}}))

#print(collection.update_many({"sınıfı": "3-A"},
#                             {"$push": {"points": {"$each": ["x", "y", "z"], "$position": 6}}}))

#print(collection.update_many({"sınıfı": "4-A"},
#                             {"$push": {"points": {"$each": ["abc", "xyz"], "$position": 8}}}))

#print(collection.update_many({"sınıfı": "5-A"},
#                             {"$push": {"points": {"$each": ["java", "python", "c##"], "$position": 20}}}))

#print(collection.update_one({"isim": "meliha"}, {"$addToSet": {"points": "hello"}}))

#print(collection.update_one({"isim": "merve"}, {"$addToSet": {"points": "hi"}}))

#print(collection.update_many({"sınıfı": "4-A"}, {"$addToSet": {"points": "how are you"}}))

#print(collection.update_many({"sınıfı": "3-A"}, {"$addToSet": {"points": ["başlık1", "başlık2"]}}))

#print(collection.update_many({"sınıfı": "5-A"}, {"$addToSet": {"points": "bootstrap"}}))

#print(collection.update_many({"sınıfı": "4-A"}, {"$addToSet": {"points": {"$each": ["fizik", "kimya", "biyoloji"]}}}))

#print(collection.update_many({"sınıfı": "5-A"}, {"$addToSet": {"points": {"$each": ["tarih", "felsefe", "edebiyat"]}}}))

#print(collection.update_many({"isim": "deniz"},
#                             {"$addToSet": {"kişisel bilgiler.arkadaşları": {"$each": ["john", "thompson", "denilson", "mary"]}}}))

#print(collection.update_one({"isim": "deniz"},
#                            {"$addToSet": {"kişisel bilgiler.arkadaşları": {"$each": ["henry", "joe", "jack", "thomas", "enrique"]}}}))

#print(collection.update_many({"sınıfı": "3-A"},
#                             {"$addToSet": {"points.12": {"$each": ["mysql", "sqlite3", "sql"]}}}))

#print(collection.update_many({"sınıfı": "3-A"},
#                             {"$addToSet": {"points.13": {"$each": ["başlık3", "başlık4", "başlık5", "başlık6", "başlık7"]}}}))


#print(collection.update_one({"isim": "halim"},
#            {"$push": {"diller": {"$each": ["hırvatça", "macarca", "bulgarca"], "$sort": 1}}}))

#print(collection.update_one({"isim": "halim"},
#             {"$push": {"diller": {"$each": ["fransızca", "türkçe", "ispanyolca"], "$sort": -1}}}))

#print(collection.update_one({"isim": "halim"},
#              {"$push": {"diller": {"$each": ["italyanca", "lehçe", "latince"], "$sort": 1}}}))

#print(collection.update_one({"isim": "halim"},
#               {"$push": {"diller": {"$each": ["cince", "rusca", "japonca"], "$sort": -1}}}))

#print(collection.update_one({"isim": "halim"},
#               {"$push": {"diller": {"$each": [], "$sort": 1}}}))

#print(collection.update_one({"isim": "deniz"},
#               {"$push": {"kişisel bilgiler.arkadaşları": {"$each": [], "$sort": 1}}}))

#print(collection.update_one({"isim": "orkan"},
#               {"$push": {"kişisel bilgiler.bildiği diller": {"$each": [], "$sort": -1}}}))

#print(collection.update_one({"isim": "enis"},
#               {"$push": {"kişisel bilgiler.bildiği diller": {"$each": [], "$sort": 1}}}))


#print(collection.update_one({"isim": "cemal"},
#                            {"$push": {"ders durumu": {"$each": [], "$sort": {"vize": -1}}}}))

#print(collection.update_one({"isim": "cemal"},
#                            {"$push": {"ders durumu": {"$each": [], "$sort": {"final": 1}}}}))

#print(collection.update_one({"isim": "cemal"},
#                            {"$push": {"ders durumu": {"$each": [], "$sort": {"kredi": -1}}}}))

#print(collection.update_one({"isim": "cemal"},
#                            {"$push": {"ders durumu": {"$each": [], "$sort": {"kitap adedi": -1}}}}))

#print(collection.update_one({"isim": "cemal"},
#                            {"$push": {"ders durumu": {"$each": [], "$sort": {"sözlü sınavı": 1}}}}))

#print(collection.update_one({"isim": "cemal"},
#                            {"$push": {"ders durumu": {"$each": [], "$sort": {"konu adedi": 1}}}}))

#print(collection.update_one({"isim": "cemal"},
#                            {"$push": {"ders durumu": {"$each": [], "$sort": {"kitap sayfa sayısı": -1}}}}))

#print(collection.update_one({"isim": "halim"},
#                            {"$push": {"diller": {"$each": [], "$sort": -1, "$slice": 15}}}))

#print(collection.update_one({"isim": "selma"},
#                            {"$push": {"points.12": {"$each": [], "$sort": -1, "$slice": 4}}}))

#print(collection.update_one({"isim": "selma"},
#                            {"$push": {"points.13": {"$each": [], "$sort": -1, "$slice": 5}}}))

#print(collection.update_many({"sınıfı": "3-A"},
#                            {"$push": {"points.12": {"$each": [], "$sort": -1, "$slice": 8}}}))

#print(collection.update_one({"isim": "meliha"},
#                            {"$push": {"points": {"$each": [], "$slice": -5}}}))

#print(collection.update_one({"isim": "merve"},
#                            {"$push": {"points": {"$each": [], "$slice": 14}}}))

#print(collection.update_many({"sınıfı": "4-A"},
#                             {"$push": {"points": {"$each": [], "$slice": 12}}}))

#print(collection.update_many({"sınıfı": "3-A"},
#                             {"$push": {"points": {"$each": [], "$slice": -7}}}))

#datas = [{"_id": 1, "tam isim": {"adı": "cenk", "soyadı": "berker"}, "bölüm": "ingilizce", "hobisi": "müzik", "memleketi": "nevşehir", "en sevdiği hayvan": "kedi", "en sevdiği renk": "beyaz", "en sevdiği yemek": "pizza", "en sevdiği içecek": "kola", "en sevdiği yazılım programı": "java", "burcu": "terazi", "tuttuğu takım": "chicago bulls"},
#         {"_id": 2, "tam isim": {"adı": "aziz", "soyadı": "kumbaracı"}, "bölüm": "türkçe", "hobisi": "seyahat", "memleketi": "kocaeli", "en sevdiği hayvan": "köpek", "en sevdiği renk": "kırmızı", "en sevdiği yemek": "makarna", "en sevdiği içecek": "ayran", "en sevdiği yazılım programı": "php", "burcu": "kova", "tuttuğu takım": "indiana pacers"},
#         {"_id": 3, "tam isim": {"adı": "fahrettin", "soyadı": "doğan"}, "bölüm": "matematik", "hobisi": "bisiklet", "memleketi": "afyon", "en sevdiği hayvan": "kelebek", "en sevdiği renk": "yeşil", "en sevdiği yemek": "pilav", "en sevdiği içecek": "fanta", "en sevdiği yazılım programı": "python", "burcu": "boğa", "tuttuğu takım": "los angeles lakers"},
#         {"_id": 4, "tam isim": {"adı": "erman", "soyadı": "yamansoy"}, "bölüm": "fizik", "hobisi": "dans", "memleketi": "eskişehir", "en sevdiği hayvan": "at", "en sevdiği renk": "sarı", "en sevdiği yemek": "hamburger", "en sevdiği içecek": "su", "en sevdiği yazılım programı": "c##", "burcu": "ikizler", "tuttuğu takım": "boston celtics"},
#         {"_id": 5, "tam isim": {"adı": "halil", "soyadı": "kartal"}, "bölüm": "tarih", "hobisi": "resim", "memleketi": "bursa", "en sevdiği hayvan": "tavşan", "en sevdiği renk": "siyah", "en sevdiği yemek": "kebap", "en sevdiği içecek": "gazoz", "en sevdiği yazılım programı": "ruby", "burcu": "akrep", "tuttuğu takım": "detroit pistons"},
#         {"_id": 6, "tam isim": {"adı": "vehbi", "soyadı": "bayraktar"}, "bölüm": "edebiyat", "hobisi": "oyun", "memleketi": "mersin", "en sevdiği hayvan": "sincap", "en sevdiği renk": "mavi", "en sevdiği yemek": "döner", "en sevdiği içecek": "soda", "en sevdiği yazılım programı": "go", "burcu": "başak", "tuttuğu takım": "orlando magic"}]
#
#collection.insert_many(datas)


#for i in collection.aggregate([{"$project": {"tam isim.adı": 1, "tam isim.soyadı": 1, "_id": 0, "bölümüm": {"$concat": ["benim bölümüm :", "$bölüm"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim.adı": 1, "tam isim.soyadı": 1, "_id": 0, "hobim": {"$concat": ["benim hobim :", "$hobisi"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim.adı": 1, "tam isim.soyadı": 1, "_id": 0, "memleketim": {"$concat": ["benim memleketim : ", "$memleketi"]}}}]):
#     print(i)

#for i in collection.aggregate([{"$project": {"tam isim.adı": 1, "favori hayvan": {"$concat": ["favori hayvan : ", "$en sevdiği hayvan"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim.soyadı": 1, "_id": 0, "favori renk": {"$concat": ["favori renk : ", "$en sevdiği renk"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim.adı": 1, "tam isim.soyadı": 1, "favori yemeğim": {"$concat": ["favori yemeğim : ", "$en sevdiği yemek"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim.adı": 1, "favori içeceğim": {"$concat": ["favori içeceğim : ", "$en sevdiği içecek"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim.adı": 1, "tam isim.soyadı": 1, "favori yazılım programı": {"$concat": ["favori yazılım programı : ", "$en sevdiği yazılım programı"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim.adı": 1, "burç": {"$concat": ["burcunu yazdır : ", "$burcu"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "favori takım": {"$concat": ["favori takımım : ", "$tuttuğu takım"]}}}]):
#    print(i)




#for i in collection.aggregate([{"$project": {"full name": {"$concat": ["$tam isim.göbek adı", " ", "$tam isim.adı", " ", "$tam isim.soyadı"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"bilgiler": {"$concat": ["$ögrenci bilgiler.burc", " ", "$ögrenci bilgiler.renk", " ",
#                                                                       "$ögrenci bilgiler.ders", " ", "$ögrenci bilgiler.yemek"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"isim": 1, "soyisim": 1, "_id": 0, "renk isimleri":
#   {"$concat": ["$renkler.renk1", " ", "$renkler.renk2", " ", "$renkler.renk3", " ", "$renkler.renk4", " ", "$renkler.renk5"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"isim": 1, "soyisim": 1, "_id": 0, "yiyecekler":
#                     {"$concat": ["$yemek sırası.kahvaltı", " ", "$yemek sırası.öğle yemeği", " ", "$yemek sırası.akşam yemeği"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"isim": 1, "soyisim": 1, "_id": 0, "aile bireyleri isimleri":
#    {"$concat": ["baba : ", "$aile bireyleri.baba", " ", "anne : ", "$aile bireyleri.anne", " ",
#                 "ağabey : ", "$aile bireyleri.ağabey", " ", "abla : ", "$aile bireyleri.abla"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"isim": 1, "soyisim": 1, "_id": 0, "ders isimleri":
#    {"$concat": ["birinci ders : ", "$lessons.ders1", " ", "ikinci ders : ", "$lessons.ders2", " ",
#                 "üçüncü ders : ", "$lessons.ders3", " ", "dördüncü ders : ", "$lessons.ders4"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"isim": 1, "soyisim": 1, "vize ve final":
#    {"$concat": ["birinci vize : ", "$vize ve final notları.vize1", " ", "ikinci vize : ", "$vize ve final notları.vize2", " ",
#                 "birinci final : ", "$vize ve final notları.final1", " ", "ikinci final : ", "$vize ve final notları.final2"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"isim": 1, "soyisim": 1, "_id": 0, "öğretmenler":
#    {"$concat": ["ingilizce öğretmeninin adı : ", "$öğretmen isimleri.ingilizce öğretmeni", " ",
#                 "tarih öğretmeninin adı : ", "$öğretmen isimleri.tarih öğretmeni", " ",
#                 "geometri öğretmeninin adı : ", "$öğretmen isimleri.geometri öğretmeni", " ",
#                 "fizik öğretmeninin adı : ", "$öğretmen isimleri.edebiyat öğretmeni"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"isim": 1, "soyisim": 1, "_id": 0, "arkadaşları":
#    {"$concat": ["mahalle : ", "$friends.mahalle arkadaşı", " ",
#                 "okul : ", "$friends.okul arkadaşı", " ",
#                 "dershane : ", "$friends.dershane arkadaşı"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"isim": 1, "_id": 0, "ünlüler":
#    {"$concat": ["futbolcu : ", "$favori ünlüler.futbol", " ", "basketbolcu : ", "$favori ünlüler.basketbol", " ",
#                 "sanatçı : ", "$favori ünlüler.şarkıcı", " ", "oyuncu : ", "$favori ünlüler.aktör"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "_id": 0,
#                                             "sonuc": {"$strcasecmp": ["$bölüm", "türkçe"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "_id": 0,
#                                             "sonuc": {"$strcasecmp": ["$hobisi", "oyun"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "_id": 0,
#                                             "sonuc": {"$strcasecmp": ["$memleketi", "mersin"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "_id": 0,
#                                             "sonuc": {"$strcasecmp": ["$en sevdiği hayvan", "yılan"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1,
#                                             "sonuc": {"$strcasecmp": ["$en sevdiği renk", "kahverengi"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1,
#                                             "sonuc": {"$strcasecmp": ["$en sevdiği yemek", "patates kızartması"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1,
#                                             "sonuc": {"$strcasecmp": ["$en sevdiği içecek", "oralet"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1,
#                                             "sonuc": {"$strcasecmp": ["$en sevdiği yazılım programı", "html"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "_id": 0,
#                                             "sonuc": {"$strcasecmp": ["$burcu", "aslan"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1,
#                                             "sonuc": {"$strcasecmp": ["$tuttuğu takım", "atlanta hawks"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"sonuc": {"$strcasecmp": ["$tam isim.göbek adı", "harun"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1,
#                                             "sonuc": {"$strcasecmp": ["$tam isim.adı", "muhsin"]}}}]):
#     print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1,
#                                             "sonuc": {"$strcasecmp": ["$tam isim.soyadı", "kemik"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1,
#                                             "sonuc": {"$strcasecmp": ["$tam isim.adı", "cenk"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1,
#                                             "sonuc": {"$strcasecmp": ["$tam isim.göbek adı", "abdülkerim"]}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1,
#                                             "sonuc": {"$strcasecmp": ["$tam isim.soyadı", "yamansoy"]}}}]):
#    print(i)





#for i in collection.aggregate([{"$project": {"tam isim": 1, "bölümü": {"$toUpper": "$bölüm"}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "hobi": {"$toUpper": "$hobisi"}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "_id": 0, "memleket": {"$toUpper": "$memleketi"}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "_id": 0, "favori hayvan": {"$toUpper": "$en sevdiği hayvan"}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "_id": 0, "favori renk": {"$toUpper": "$en sevdiği renk"}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "_id": 0, "burç": {"$toUpper": "$burcu"}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "takım": {"$toUpper": "$tuttuğu takım"}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "ad": {"$toUpper": "$tam isim.adı"}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "soyad": {"$toUpper": "$tam isim.soyadı"}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "tam ad": {"$toUpper": "$tam isim.göbek adı"}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"_id": 1}},
#                               {"$project": {"tam isim": 1, "hobi": {"$toUpper": "$hobisi"}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"_id": 2}},
#                               {"$project": {"tam isim": 1, "_id": 0, "memleket": {"$toUpper": "$memleketi"}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"_id": 3}},
#                               {"$project": {"tam isim": 1, "_id": 0, "bölümü": {"$toUpper": "$bölüm"}}}]):
#    print(i)







#for i in collection.aggregate([{"$project": {"tam isim": 1, "film": {"$toLower": "$en sevdiği film"}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "takım": {"$toLower": "$tuttuğu takım"}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "burç": {"$toLower": "$burcu"}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "yazılım programı": {"$toLower": "$en sevdiği yazılım programı"}}}]):
#    print(i)

#for i in collection.aggregate([{"$project": {"tam isim": 1, "_id": 0, "içecek": {"$toLower": "$en sevdiği içecek"}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"tam isim.adı": "halil"}},
#                               {"$project": {"film": {"$toLower": "$en sevdiği film"}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"tam isim.soyadı": "doğan"}},
#                               {"$project": {"takım": {"$toLower": "$tuttuğu takım"}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"tam isim.göbek adı": "hayrettin"}},
#                               {"$project": {"tam isim": 1, "_id": 0, "burç": {"$toLower": "$burcu"}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"tam isim.takma adı": "SAVAŞÇI"}},
#            {"$project": {"tam isim": 1, "_id": 0, "yazılım": {"$toLower": "$en sevdiği yazılım programı"}}}]):
#     print(i)

#for i in collection.aggregate([{"$match": {"_id": 4}},
#                               {"$project": {"tam isim": 1, "içecek": {"$toLower": "$en sevdiği içecek"}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"_id": 1}},
#                               {"$project": {"tam isim": 1, "_id": 0, "takma isim": {"$toLower": "$tam isim.takma adı"}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"_id": 6}},
#                               {"$project": {"tam isim": 1, "_id": 0, "takma isim": {"$toLower": "$tam isim.takma adı"}}}]):
#    print(i)

#for i in collection.aggregate([{"$match": {"_id": 3}},
#                               {"$project": {"tam isim": 1, "_id": 0, "takma isim": {"$toLower": "$tam isim.takma adı"}}}]):
#    print(i)






#datas = [{"_id": 10, "kitap adı": "sefiller", "yayım tarihi": "ocak2013"},
#         {"_id": 11, "kitap adı": "suç ve ceza", "yayım tarihi": "mart2016"},
#         {"_id": 12, "kitap adı": "madama bovary", "yayım tarihi": "ekim2010"},
#         {"_id": 13, "kitap adı": "yer altından notlar", "yayım tarihi": "şubat2015"},
#         {"_id": 14, "kitap adı": "büyük umutlar", "yayım tarihi": "nisan2004"},
#         {"_id": 15, "kitap adı": "bülbülü öldürmek", "yayım tarihi": "mayıs2007"},
#         {"_id": 16, "kitap adı": "yüzyıllık yalnızlık", "yayım tarihi": "eylül2003"},
#         {"_id": 17, "kitap adı": "kırmızı ve siyah", "yayım tarihi": "kasım2000"},
#         {"_id": 18, "kitap adı": "ölü canlar", "yayım tarihi": "temmuz2014"},
#         {"_id": 19, "kitap adı": "savaş ve barış", "yayım tarihi": "aralık2020"},
#         {"_id": 20, "kitap adı": "iki şehrin hikayesi", "yayım tarihi": "haziran2022"},
#         {"_id": 21, "kitap adı": "gazap üzümleri", "yayım tarihi": "ağustos2001"}]
#
#print(collection.insert_many(datas))

#for i in collection.aggregate([
#    {"$match": {"_id": 10}},
#    {"$project": {
#            "kitap adı": 1,
#            "yayın ayı": {"$substrCP": ["$yayım tarihi", 0, 4]},
#            "yayın yılı": {"$substrCP": ["$yayım tarihi", 4, {"$subtract": [{"$strLenCP": "$yayım tarihi"}, 4]}]}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 13}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayın ayı": {"$substrCP": ["$yayım tarihi", 0, 5]},
#        "yayın yılı": {"$substrCP": ["$yayım tarihi", 5, {"$subtract": [{"$strLenCP": "$yayım tarihi"}, 5]}]}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 18}},
#    {"$project": {
#        "kitap adı": 1,
#        "_id": 0,
#        "yayın ayı": {"$substrCP": ["$yayım tarihi", 0, 6]},
#        "yayın yılı": {"$substrCP": ["$yayım tarihi", 6, {"$subtract": [{"$strLenCP": "$yayım tarihi"}, 6]}]}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 21}},
#    {"$project": {
#                "yayım tarihi": 1,
#                "_id": 0,
#                "ad1": {"$substrCP": ["$kitap adı", 0, 5]},
#                "ad2": {"$substrCP": ["$kitap adı", 6, {"$subtract": [{"$strLenCP": "$kitap adı"}, 6]}]}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 20}},
#    {"$project": {
#        "yayım tarihi": 1,
#        "_id": 0,
#        "ad1": {"$substrCP": ["$kitap adı", 0, 3]},
#        "ad2": {"$substrCP": ["$kitap adı", 4, 6]},
#        "ad3": {"$substrCP": ["$kitap adı", 11, {"$subtract": [{"$strLenCP": "$kitap adı"}, 11]}]}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 19}},
#    {"$project": {
#        "yayım tarihi": 1,
#        "_id": 0,
#        "ad1": {"$substrCP": ["$kitap adı", 0, 5]},
#        "ad2": {"$substrCP": ["$kitap adı", 6, 2]},
#        "ad3": {"$substrCP": ["$kitap adı", 9, {"$subtract": [{"$strLenCP": "$kitap adı"}, 9]}]}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 18}},
#    {"$project": {
#        "yayım tarihi": 1,
#        "_id": 0,
#        "ad1": {"$substrCP": ["$kitap adı", 0, 3]},
#        "ad2": {"$substrCP": ["$kitap adı", 4, {"$subtract": [{"$strLenCP": "$kitap adı"}, 4]}]}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 17}},
#    {"$project": {
#        "yayım tarihi": 1,
#        "_id": 0,
#        "ad1": {"$substrCP": ["$kitap adı", 0, 7]},
#        "ad2": {"$substrCP": ["$kitap adı", 8, 2]},
#        "ad3": {"$substrCP": ["$kitap adı", 11, 5]}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 16}},
#    {"$project": {
#            "yayım tarihi": 1,
#            "_id": 0,
#            "ad1": {"$substrCP": ["$kitap adı", 0, {"$subtract": [{"$strLenCP": "$kitap adı"}, 9]}]},
#            "ad2": {"$substrCP": ["$kitap adı", 9, {"$subtract": [{"$strLenCP": "$kitap adı"}, 9]}]}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 15}},
#    {"$project": {
#        "yayım tarihi": 1,
#        "_id": 0,
#        "ad1": {"$substrCP": ["$kitap adı", 0, {"$subtract": [{"$strLenCP": "$kitap adı"}, 8]}]},
#        "ad2": {"$substrCP": ["$kitap adı", 7, {"$subtract": [{"$strLenCP": "$kitap adı"}, 7]}]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 14}},
#    {"$project": {
#        "yayım tarihi": 1,
#        "_id": 0,
#        "ad1": {"$substrCP": ["$kitap adı", 0, {"$subtract": [{"$strLenCP": "$kitap adı"}, 7]}]},
#        "ad2": {"$substrCP": ["$kitap adı", 5, {"$subtract": [{"$strLenCP": "$kitap adı"}, 5]}]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 13}},
#    {"$project": {
#        "yayım tarihi": 1,
#        "kitap adı": 1,
#        "_id": 0,
#        "ad1": {"$substrCP": ["$kitap adı", 0, {"$subtract": [{"$strLenCP": "$kitap adı"}, 16]}]},
#        "ad2": {"$substrCP": ["$kitap adı", 4, {"$subtract": [{"$strLenCP": "$kitap adı"}, 11]}]},
#        "ad3": {"$substrCP": ["$kitap adı", 13, {"$subtract": [{"$strLenCP": "$kitap adı"}, 13]}]},
#        "yayın ayı": {"$substrCP": ["$yayım tarihi", 0, {"$subtract": [{"$strLenCP": "$yayım tarihi"}, 4]}]},
#        "yayın yılı": {"$substrCP": ["$yayım tarihi", 5, {"$subtract": [{"$strLenCP": "$yayım tarihi"}, 5]}]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 12}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "_id": 0,
#        "ad1": {"$substrCP": ["$kitap adı", 0, {"$subtract": [{"$strLenCP": "$kitap adı"}, 7]}]},
#        "ad2": {"$substrCP": ["$kitap adı", 7, {"$subtract": [{"$strLenCP": "$kitap adı"}, 7]}]},
#        "yayın ayı": {"$substrCP": ["$yayım tarihi", 0, {"$subtract": [{"$strLenCP": "$yayım tarihi"}, 4]}]},
#        "yayın yılı": {"$substrCP": ["$yayım tarihi", 4, {"$subtract": [{"$strLenCP": "$yayım tarihi"}, 4]}]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 11}},
#    {"$project": {
#        "ad1": {"$substrCP": ["$kitap adı", 0, {"$subtract": [{"$strLenCP": "$kitap adı"}, 8]}]},
#        "ad2": {"$substrCP": ["$kitap adı", 4, {"$subtract": [{"$strLenCP": "$kitap adı"}, 9]}]},
#        "ad3": {"$substrCP": ["$kitap adı", 7, {"$subtract": [{"$strLenCP": "$kitap adı"}, 7]}]},
#        "yayın ayı": {"$substrCP": ["$yayım tarihi", 0, {"$subtract": [{"$strLenCP": "$yayım tarihi"}, 4]}]},
#        "yayın yılı": {"$substrCP": ["$yayım tarihi", 4, {"$subtract": [{"$strLenCP": "$yayım tarihi"}, 4]}]}}}]):
#
#    print(i)














