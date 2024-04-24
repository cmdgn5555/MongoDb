import pymongo
from pprint import pprint
from bson import ObjectId
import uuid
from pprint import pprint


a = "abcdef"
connect = pymongo.MongoClient("mongodb+srv://cemdogan1109:"+a+"@cluster0.gweobzp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

database = connect["okul"]
collection = database["öğrenciler"]

#for i in collection.aggregate([
#                      {"$match": {"_id": 11}},
#                      {"$project": {
#                          "kitap adı": 1,
#                          "yayım tarihi": 1,
#                          "toplam fiyat": {"$add": ["$normal fiyatı", "$zamlı fiyatı"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 12}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "toplam fiyat": {"$add": ["$normal fiyatı", "$zamlı fiyatı"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 13}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "toplam fiyat": {"$add": ["$normal fiyatı", "$zamlı fiyatı"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 14}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "kitap bilgi toplamı": {"$add": ["$kitap hakkındaki bilgiler.sayfa sayısı",
#                                         "$kitap hakkındaki bilgiler.basım adedi",
#                                         "$kitap hakkındaki bilgiler.satış adedi"]}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 15}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "kitap bilgi toplamı": {"$add": ["$kitap hakkındaki bilgiler.sayfa sayısı",
#                                         "$kitap hakkındaki bilgiler.basım adedi",
#                                         "$kitap hakkındaki bilgiler.satış adedi"]}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "kitap bilgi toplamı": {"$add": ["$kitap hakkındaki bilgiler.sayfa sayısı",
#                                         "$kitap hakkındaki bilgiler.basım adedi",
#                                         "$kitap hakkındaki bilgiler.satış adedi"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"isim": "tolga"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "kişisel bilgilerin toplamı": {"$add": ["$kişisel bilgiler.yaş",
#                                                "$kişisel bilgiler.boy",
#                                                "$kişisel bilgiler.kilo"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"isim": "orkan"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "kişisel bilgiler.memleketi": 1,
#        "_id": 0,
#        "kişisel bilgilerin toplamı": {"$add": ["$kişisel bilgiler.yaş",
#                                                "$kişisel bilgiler.boy",
#                                                "$kişisel bilgiler.harçlık",
#                                                "$kişisel bilgiler.kilo",
#                                                "$kişisel bilgiler.uğurlu sayı"]}}}]):
#
#    print(i)







#for i in collection.aggregate([
#    {"$match": {"_id": 11}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "fark": {"$subtract": ["$normal fiyatı", "$zamlı fiyatı"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 12}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "fark": {"$subtract": ["$zamlı fiyatı", "$normal fiyatı"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 13}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "fark": {"$subtract": ["$zamlı fiyatı", "$normal fiyatı"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 14}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "fark": {"$subtract": ["$kitap hakkındaki bilgiler.basım adedi",
#                               "$kitap hakkındaki bilgiler.satış adedi"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 15}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "fark": {"$subtract": ["$kitap hakkındaki bilgiler.basım adedi",
#                               "$kitap hakkındaki bilgiler.satış adedi"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"soyisim": "yalın"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "fark": {"$subtract": ["$kişisel bilgiler.boy",
#                               "$kişisel bilgiler.kilo"]}}}]):
#
#     print(i)







#for i in collection.aggregate([
#    {"$match": {"_id": 11}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "çarpımı": {"$multiply": ["$normal fiyatı", "$zamlı fiyatı", 2]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 12}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "çarpımı": {"$multiply": ["$normal fiyatı", 5]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 13}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "çarpımı": {"$multiply": ["$zamlı fiyatı", 9]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 14}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "çarpımı": {"$multiply": ["$kitap hakkındaki bilgiler.sayfa sayısı",
#                                  "$kitap hakkındaki bilgiler.sayfa sayısı"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 15}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "çarpımı": {"$multiply": ["$kitap hakkındaki bilgiler.sayfa sayısı",
#                                  "$kitap hakkındaki bilgiler.basım adedi",
#                                  "$kitap hakkındaki bilgiler.satış adedi"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"soyisim": "yalın"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "_id": 0,
#        "çarpımı": {"$multiply": ["$kişisel bilgiler.yaş", 4]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"soyisim": "yalın"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "çarpımı": {"$multiply": ["$kişisel bilgiler.kilo", 3]}}}]):
#
#    print(i)







#for i in collection.aggregate([
#    {"$match": {"_id": 11}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "bölme işlemi sonucu": {"$divide": ["$zamlı fiyatı", "$normal fiyatı"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"kitap adı": "madama bovary"}},
#    {"$project": {
#        "yayım tarihi": 1,
#        "_id": 0,
#        "bölme işlemi sonucu1": {"$divide": ["$normal fiyatı", 2]},
#        "bölme işlemi sonucu2": {"$divide": ["$zamlı fiyatı", 3]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"yayım tarihi": "şubat2015"}},
#    {"$project": {
#        "kitap adı": 1,
#        "_id": 0,
#        "bölme işlemi sonucu1": {"$divide": ["$normal fiyatı", 23]},
#        "bölme işlemi sonucu2": {"$divide": ["$zamlı fiyatı", 26]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"isim": "tolga"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "_id": 0,
#        "bölme işlemi sonucu1": {"$divide": ["$kişisel bilgiler.boy", 2]},
#        "bölme işlemi sonucu2": {"$divide": ["$kişisel bilgiler.kilo", 2]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"isim": "orkan"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "_id": 0,
#        "bölme işlemi sonucu1": {"$divide": ["$kişisel bilgiler.yaş", 5]},
#        "bölme işlemi sonucu2": {"$divide": ["$kişisel bilgiler.boy", 8]},
#        "bölme işlemi sonucu3": {"$divide": ["$kişisel bilgiler.harçlık", 12]},
#        "bölme işlemi sonucu4": {"$divide": ["$kişisel bilgiler.kilo", 4]},
#        "bölme işlemi sonucu5": {"$divide": ["$kişisel bilgiler.uğurlu sayı", 3]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"soyisim": "yalın"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "_id": 0,
#        "bölme işlemi sonucu": {"$divide": ["$kişisel bilgiler.yaş", 4]}}}]):
#
#    print(i)







#for i in collection.aggregate([
#    {"$match": {"_id": 11}},
#    {"$project": {
#        "_id": 0,
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "mutlak değer1": {"$abs": {"$add": ["$normal fiyatı", -1000]}},
#        "mutlak değer2": {"$abs": {"$add": ["$zamlı fiyatı", -1000]}}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 12}},
#    {"$project": {
#        "_id": 0,
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "mutlak değer1": {"$abs": {"$subtract": ["$normal fiyatı", 500]}},
#        "mutlak değer2": {"$abs": {"$subtract": ["$zamlı fiyatı", 500]}}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 13}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "mutlak değer": {"$abs": {"$subtract": ["$normal fiyatı", "$zamlı fiyatı"]}}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 14}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "_id": 0,
#        "mutlak değer": {"$abs": {"$subtract": ["$kitap hakkındaki bilgiler.satış adedi",
#                                                "$kitap hakkındaki bilgiler.basım adedi"]}}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 15}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "_id": 0,
#        "mutlak değer": {"$abs": {"$subtract": ["$kitap hakkındaki bilgiler.satış adedi",
#                                                "$kitap hakkındaki bilgiler.basım adedi"]}}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"soyisim": "yalın"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "_id": 0,
#        "mutlak değer": {"$abs": {"$subtract": ["$kişisel bilgiler.yaş", 30]}}}}]):
#
#    print(i)







#for i in collection.aggregate([
#    {"$match": {"_id": 11}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "rating": 1,
#        "_id": 0,
#        "sayıyı aşağı yuvarla": {"$floor": "$rating"}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 12}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "rating": 1,
#        "_id": 0,
#        "sayıyı aşağı yuvarla": {"$floor": "$rating"}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 13}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "rating": 1,
#        "_id": 0,
#        "sayıyı aşağı yuvarla": {"$floor": "$rating"}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "_id": 0,
#        "sayıyı aşağı yuvarla": {"$floor": "$kitap hakkındaki bilgiler.rating"}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"soyisim": "yalın"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "_id": 0,
#        "kişisel bilgiler.kitap okuma oranı": 1,
#        "sayıyı aşağı yuvarla": {"$floor": "$kişisel bilgiler.kitap okuma oranı"}}}]):
#
#    print(i)







#for i in collection.aggregate([
#    {"$match": {"_id": 11}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "_id": 0,
#        "sayıyı yukarı yuvarla": {"$ceil": "$rating"}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 12}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "sayıyı yukarı yuvarla": {"$ceil": "$rating"}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 13}},
#    {"$project": {
#        "kitap adı": 1,
#        "_id": 0,
#        "sayıyı yukarı yuvarla": {"$ceil": "$rating"}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "sayıyı yukarı yuvarla": {"$ceil": "$kitap hakkındaki bilgiler.rating"}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"soyisim": "yalın"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "kişisel bilgiler.kitap okuma oranı": 1,
#        "sayıyı yukarı yuvarla": {"$ceil": "$kişisel bilgiler.kitap okuma oranı"}}}]):
#
#    print(i)







#for i in collection.aggregate([
#    {"$match": {"_id": 11}},
#    {"$project": {
#        "kitap adı": 1,
#        "_id": 0,
#        "kalan miktarı göster1": {"$mod": ["$normal fiyatı", 3]},
#        "kalan miktarı göster2": {"$mod": ["$zamlı fiyatı", 7]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 12}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "kalan miktarı göster1": {"$mod": ["$normal fiyatı", 9]},
#        "kalan miktarı göster2": {"$mod": ["$zamlı fiyatı", 13]},
#        "kalan miktarı göster3": {"$mod": ["$zamlı fiyatı", "$normal fiyatı"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 13}},
#    {"$project": {
#        "kitap adı": 1,
#        "_id": 0,
#        "kalan miktarı göster1": {"$mod": ["$normal fiyatı", 4]},
#        "kalan miktarı göster2": {"$mod": ["$zamlı fiyatı", 8]},
#        "kalan miktarı göster3": {"$mod": ["$zamlı fiyatı", "$normal fiyatı"]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {}},
#    {"$project": {
#        "_id": 0,
#        "yayım tarihi": 1,
#        "kitap adı": 1,
#        "kalan miktarı göster1": {"$mod": ["$kitap hakkındaki bilgiler.sayfa sayısı", 6]},
#        "kalan miktarı göster2": {"$mod": ["$kitap hakkındaki bilgiler.basım adedi", 120000]},
#        "kalan miktarı göster3": {"$mod": ["$kitap hakkındaki bilgiler.satış adedi", 160000]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"soyisim": "yalın"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "_id": 0,
#        "kalan miktarı göster1": {"$mod": ["$kişisel bilgiler.yaş", 6]},
#        "kalan miktarı göster2": {"$mod": ["$kişisel bilgiler.boy", 9]},
#        "kalan miktarı göster3": {"$mod": ["$kişisel bilgiler.kilo", 14]}}}]):
#
#    print(i)







#for i in collection.aggregate([
#    {"$match": {"_id": 16}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "_id": 0,
#        "karekökü": {"$sqrt": "$ödül sayısı"}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 17}},
#    {"$project": {
#        "kitap adı": 1,
#        "_id": 0,
#        "karekökü": {"$sqrt": "$ödül sayısı"}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 18}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "karekökü": {"$sqrt": "$ödül sayısı"}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"soyisim": "yalın"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "karekökü": {"$sqrt": "$kişisel bilgiler.yaş"}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "_id": 0,
#        "karekökü1": {"$sqrt": "$kişisel bilgiler.boy"},
#        "karekökü2": {"$sqrt": "$kişisel bilgiler.kilo"}}}]):
#
#    print(i)







#for i in collection.aggregate([
#    {"$match": {"_id": 11}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "normal fiyatı": 1,
#        "zamlı fiyatı": 1,
#        "rating": 1,
#        "_id": 0,
#        "sayının üssü1": {"$pow": ["$normal fiyatı", 3]},
#        "sayının üssü2": {"$pow": ["$zamlı fiyatı", 3]},
#        "sayının üssü3": {"$pow": ["$rating", 3]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 12}},
#    {"$project": {
#        "kitap adı": 1,
#        "yayım tarihi": 1,
#        "normal fiyatı": 1,
#        "zamlı fiyatı": 1,
#        "rating": 1,
#        "_id": 0,
#        "sayının üssü1": {"$pow": ["$normal fiyatı", 4]},
#        "sayının üssü2": {"$pow": ["$zamlı fiyatı", 5]},
#        "sayının üssü3": {"$pow": ["$rating", 6]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 13}},
#    {"$project": {
#        "kitap adı": 1,
#        "_id": 0,
#        "sayının üssü1": {"$pow": ["$normal fiyatı", 2]},
#        "sayının üssü2": {"$pow": ["$zamlı fiyatı", 2]},
#        "sayının üssü3": {"$pow": ["$rating", 2]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {}},
#    {"$project": {
#        "sayının üssü1": {"$pow": ["$kitap hakkındaki bilgiler.sayfa sayısı", 2]},
#        "sayının üssü2": {"$pow": ["$kitap hakkındaki bilgiler.rating", 3]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"soyisim": "yalın"}},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "_id": 0,
#        "sayının üssü": {"$pow": ["$kişisel bilgiler.yaş", 5]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 14}},
#    {"$project": {
#        "kitap adı": 1,
#        "_id": 0,
#        "sayının üssü": {"$pow": [{"$add": ["$kitap hakkındaki bilgiler.basım adedi",
#                                            "$kitap hakkındaki bilgiler.satış adedi"]}, 2]}}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 15}},
#    {"$project": {
#        "kitap adı": 1,
#        "_id": 0,
#        "sayının üssü": {"$pow": [{"$subtract": ["$kitap hakkındaki bilgiler.basım adedi",
#                                                 "$kitap hakkındaki bilgiler.satış adedi"]}, 3]}}}]):
#
#    print(i)

#for i in collection.find(
#        {"soyisim": "yalın"},
#        {"kişisel bilgiler.yaş": 1,
#        "kişisel bilgiler.kitap okuma oranı": 1,
#         "kişisel bilgiler.memleketi": 1}):
#    print(i)


#for i in collection.distinct("isim"):
#    print(i)

#for i in collection.distinct("kişisel bilgiler.yaş"):
#    print(i)

#for i in collection.distinct("en sevdiği film"):
#    print(i)

#for i in collection.distinct("burcu"):
#    print(i)

#for i in collection.distinct("tam isim.takma adı"):
#    print(i)

#for i in collection.distinct("ögrenci bilgiler.yemek"):
#    print(i)

#for i in collection.distinct("aile bireyleri.baba"):
#    print(i)

#print(collection.count_documents({"soyisim": {"$eq": "yalın"}}))

#print(collection.count_documents({"en sevdiği yemek": {"$eq": "kebap"}}))

#print(collection.count_documents({"en sevdiği yemek": {"$ne": "kebap"}}))

#print(collection.count_documents({"kitap hakkındaki bilgiler.sayfa sayısı": {"$eq": 650}}))

#print(database.list_collection_names())

#print(database.get_collection("öğrenciler"))

#print(database.create_collection("müdürler"))

#for i in database.list_collections():
#    print(i)

#print(database.list_collection_names())

#print(database.drop_collection("öğretmenler"))

#for i in collection.list_indexes():
#    print(i)

#print(collection.count_documents({}))

#print(collection.delete_one({"aylık okul harçlığı": {"$eq": 1600}}))

#print(collection.delete_many({"vize": {"$gte": 50}, "final": {"$gte": 50}}).deleted_count)

#print(collection.delete_many({"sınıfı": {"$in": ["8-A", "7-A", "6-A"]}}).deleted_count)

#print(collection.delete_many({"yaş": {"$lte": 30}}).deleted_count)

#print(collection.delete_one({"$and": [{"isim": "ibrahim"}, {"soyisim": "esen"}]}))

#print(collection.delete_many({"$or": [{"yaş": {"$eq": 32}}, {"yaş": {"$eq": 36}}]}))

#print(collection.delete_one({"$and": [{"isim": "turan"}, {"notlar": {"$in": [80, 90]}}]}))

#print(collection.delete_many({"$and": [{"isim": "turan"}, {"notlar": {"$in": [80]}}]}))

#print(collection.delete_many({"isim": {"$eq": "turan"}}))

#print(collection.delete_many({"$and": [{"isim": "ibrahim"}, {"hobiler": {"$nin": ["seyahat"]}}]}))

#print(collection.delete_many({"$and": [{"soyisim": "yalın"},
#                                       {"kişisel bilgiler.memleketi": {"$nin": ["sivas"]}}]}))

#print(collection.delete_many({"$and": [{"soyisim": "yalın"},
#                                       {"kişisel bilgiler.kitap okuma oranı": {"$gt": 80}}]}))

#print(collection.delete_many({"$and": [{"isim": "orkan"}, {"kişisel bilgiler.yaş": {"$eq": 23}}]}))

#print(collection.delete_many({"$or": [{"friends.mahalle arkadaşı": {"$eq": "erman"}},
#                                      {"kişisel bilgiler.yabancı diller": {"$in": ["çince", "rusça"]}}]}))

#for i in collection.find().skip(22).limit(2):
#    print(i)

#print(collection.count_documents({"soyisim": "başer"}))

#print(collection.count_documents({"sınıfı": {"$in": ["3-A", "4-A", "5-A"]}}))

#print(collection.estimated_document_count())

#for i in collection.find({"sınıfı": {"$in": ["3-A", "4-A", "5-A"]}}):
#    pprint(i)

#print(collection.find({"isim": "ibrahim"}).__sizeof__())

#for i in collection.find().next():
#    print(i)

#for i in collection.find({"sınıfı": {"$exists": True}}):
#    print(i)

#for i in collection.find({"burcu": {"$exists": True}}):
#    print(i)

#for i in collection.find({"tam isim.adı": {"$exists": True}}):
#    print(i)

#for i in collection.find({"kitap adı": {"$exists": True}}):
#    print(i)

#for i in collection.find({"ödül sayısı": {"$exists": True}}):
#    print(i)

#for i in collection.find({"yayım tarihi": {"$exists": True}}):
#    print(i)

#for i in collection.find({"points": {"$exists": True}}):
#    print(i)

#for i in collection.find().limit(4):
#    print(i)

#for i in collection.find({}).sort({"kitap adı": -1}):
#    print(i)

#for i in collection.find().sort({"yayım tarihi": 1}):
#    print(i)

#print(collection.replace_one({"yayım tarihi": "ağustos2001"},
#                             {"yayım tarihi": "ağustos1997", "kitap adı": "simyacı"}))

#print(collection.replace_one({"yayım tarihi": "haziran2022"},
#                             {"yayım tarihi": "haziran1995", "kitap adı": "fareler ve insanlar"}))

#print(collection.find_one_and_replace({"kitap adı": "savaş ve barış"},
#                                {"kitap adı": "uçurtma avcısı", "yayım tarihi": "aralık1991"}))

#for i in collection.aggregate([
#    {"$match": {"sınıfı": "3-A"}},
#    {"$limit": 2},
#    {"$project": {
#        "isim": 1,
#        "soyisim": 1,
#        "_id": 0}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"_id": 3}},
#    {"$project": {
#        "tam isim.adı": 1,
#        "tam isim.soyadı": 1,
#        "tam isim.göbek adı": 1,
#        "tam isim.takma adı": 1}}]):
#
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"sınıfı": "3-A"}},
#    {"$count": "soyisim"}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"isim": "umut"}},
#    {"$count": "ismi umut olanların sayısı"}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"soyisim": "ökten"}},
#    {"$count": "soyismi ökten olanların sayısı"}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"yaş": 39}},
#    {"$count": "yaşı 39 olanların sayısı"}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"memleketi": "denizli"}},
#    {"$count": "memleketi denizli olanların sayısı"}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"memleketi": "sakarya"}},
#    {"$count": "memleketi sakarya olanların sayısı"}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"memleketi": "erzincan"}},
#    {"$count": "memleketi erzincan olanların sayısı"}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"sınıfı": {"$gte": "3-A"}}},
#    {"$group": {"_id": "$category",  "toplam": {"$sum": "$yaş"}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"kitap adı": {"$gte": "a"}}},
#    {"$group": {"_id": "$category", "toplam": {"$sum": "$rating"}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"kitap adı": {"$gte": "a"}}},
#    {"$group": {"_id": "$category", "toplam": {"$sum": "$normal fiyatı"}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"yayım tarihi": {"$gt": "abc"}}},
#    {"$group": {"_id": "$category", "toplam": {"$sum": "$zamlı fiyatı"}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"yayım tarihi": {"$gt": "abc"}}},
#    {"$group": {"_id": "$category", "toplam": {"$sum": "$normal fiyatı"}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"isim": {"$eq": "hasan"}}},
#    {"$group": {"_id": "$category", "toplam": {"$sum": "$puanlar.vize"}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"isim": {"$ne": "hasan"}}},
#    {"$group": {"_id": "$category", "toplam": {"$sum": "$puanlar.vize"}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"soyisim": "inci"}},
#    {"$group": {"_id": "$category", "toplam": {"$sum": "$puanlar.sözlü"}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"soyisim": {"$ne": "inci"}}},
#    {"$group": {"_id": "$category", "toplam": {"$sum": "$puanlar.sözlü"}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"isim": "hasan"}},
#    {"$group": {"_id": "$category", "toplam": {"$sum": "$puanlar.final"}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"isim": {"$ne": "hasan"}}},
#    {"$group": {"_id": "$category", "toplam": {"$sum": "$puanlar.final"}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"isim": {"$ne": "hasan"}}},
#    {"$group": {"_id": "$category", "ortalama": {"$avg": "$puanlar.final"}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"isim": {"$ne": "hasan"}}},
#    {"$group": {"_id": "$category", "en büyük": {"$max": "$puanlar.final"}}}]):
#    print(i)

#for i in collection.aggregate([
#    {"$match": {"isim": {"$ne": "hasan"}}},
#    {"$group": {"_id": "$category", "en küçük": {"$min": "$puanlar.final"}}}]):
#    print(i)

#collection.update_one({"isim": "berkay"}, {"$currentDate": {"tarih": True}})

#collection.update_many({"isim": "hasan"}, {"$currentDate": {"tarih": True}})

#collection.update_many({"isim": "hasan"}, {"$currentDate": {"puanlar.date": True}})

#collection.update_one({"soyisim": "şişman"}, {"$currentDate": {"notlar.tarih": True}})

#collection.update_one({"öğretmen isimleri.ingilizce öğretmeni": "yılmaz"},
#                      {"$currentDate": {"öğretmen isimleri.tarih": True}})

#collection.update_one({"_id": ObjectId("661fbbea1cd1c262e3ddccd2")},
#                     {"$currentDate": {"lessons.tarih": True}})

#collection.update_many({"sınıfı": "4-A"},
#                       {"$currentDate": {"aile bireyleri.tarih": True}})

#collection.update_one({"isim": "ibrahim"},
#                       {"$currentDate": {"notlar.tarih": {"$type": "date"}}})

#collection.update_one({"isim": "merve"},
#                      {"$currentDate": {"renkler.date": True}})


#collection.update_one({"isim": "ayşe"},
#                      {"$currentDate": {"tarih": {"$type": "date"}}})





















