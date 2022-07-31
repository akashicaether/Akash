import pymongo

client = pymongo.MongoClient("mongodb+srv://Akash:dranzer@Akash.rzvhg7f.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= { "Name" : "Akash", "Email" : "Akashd099@gmail.com", "Surname" : "Dey"}
db1 = client['mongo']
coll = db1['test']
coll.insert_one(d)