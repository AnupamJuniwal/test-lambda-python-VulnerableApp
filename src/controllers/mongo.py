import os
from operator import itemgetter

myMongoDb = None
handler_name = 'mongo'

def mongo_insert_one(data, _args):
    name, address = itemgetter('name', 'address')(data)
    print("Name : {}, address : {}".format(name, address))
    mycol = myMongoDb["customers"]
    mydict = {"name": name, "address": address}
    res = mycol.insert_one(mydict)
    print("insert_one response : {}".format(res))
    return res


def mongo_insert_many(data, _args):
    name1, address1, name2, address2 = itemgetter('name1', 'address1', 'name2', 'address2')(data)
    print("Name1 : {}, Address1 : {}\nName2 : {}, Address2 : {}".format(name1, address1, name2, address2))
    mycol = myMongoDb["customers"]
    mylist = [
        {"name": name1, "address": address1},
        {"name": name2, "address": address2}
    ]
    res = mycol.insert_many(mylist)
    print("insert_many response : {}".format(res))
    return res


def mongo_find_one(data, _args):
    name = itemgetter("name")(data)
    print("Name : {}".format(name))
    mycol = myMongoDb["customers"]
    res = mycol.find_one({"name": name})
    print("find_one response : {}".format(res))
    return res


def mongo_find(data, _args):
    name = itemgetter("name")(data)
    print("Name : {}".format(name))
    mycol = myMongoDb["customers"]
    mydoc = mycol.find({"name": name}, {"_id": 0})
    res = []
    print("find response : ")
    for x in mydoc:
        print(x)
        res.append(str(x))
    return res


def mongo_delete_one(data, _args):
    address = itemgetter("address")(data)
    print("Name : {}".format(address))
    mycol = myMongoDb["customers"]
    res = mycol.delete_one({"address": address})
    print("delete_one response : {}".format(res.raw_result))
    return res.raw_result


def mongo_delete_many(data, _args):
    address = itemgetter("address")(data)
    print("Name : {}".format(address))
    mycol = myMongoDb["customers"]
    res = mycol.delete_many({"address": {"$regex": address}})
    print("delete_many response : {}".format(res.raw_result))
    return res.raw_result


def mongo_update_one(data, _args):
    name, address = itemgetter("name", "address")(data)
    print("Name : {}, address : {}".format(name, address))
    mycol = myMongoDb["customers"]
    res = mycol.update_one({"name": name}, {"$set": {"address": address}})
    print("update_one response : {}".format(res.raw_result))
    return res.raw_result


def mongo_update_many(data, _args):
    name, address = itemgetter("name", "address")(data)
    print("Name : {}, address : {}".format(name, address))
    mycol = myMongoDb["customers"]
    res = mycol.update_many({"name": name}, {"$set": {"address": address}})
    print("update_many response : {}".format(res.raw_result))
    return res.raw_result

switcher = {
    'insert_one': mongo_insert_one,
    'insert_many': mongo_insert_many,
    'find_one': mongo_find_one,
    'find': mongo_find,
    'delete_one': mongo_delete_one,
    'delete_many': mongo_delete_many,
    'update_one': mongo_update_one,
    'update_many': mongo_update_many
}

def get_instance():
    global myMongoDb
    if myMongoDb is not None:
        return myMongoDb
    try:
        import pymongo
        myMongoClient = pymongo.MongoClient(os.environ.get('MONGO_URI'))
        myMongoDb = myMongoClient["mydatabase"]
        print("MongoClient instance created: {} {}".format(myMongoClient, myMongoDb))
        return myMongoDb
    except Exception as e:
        print("Error in Mongo instance creation, please check MongoClient is installed and mongo configuration is correct")
        print("Exception : {}".format(e.__str__()))


def handler(args):
    type, q = args
    get_instance()
    data = switcher[type](q, args)
    return data
