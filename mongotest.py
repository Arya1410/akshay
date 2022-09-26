import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:arya1410@cluster0.kuvji5y.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={
    "name" : "akshay",
    "emailid" : "akshaychaudhari555@gmail.com",
    "surname" : "chaudhari"
}
db1 =client["mongotest"]
coll = db1['test']
coll.insert_one(d)
