import pymongo
myclient=pymongo.MongoClient("mongodb+srv://zano:7275456455@cluster0.05tdw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#Check Connection
# print(myclient)

#Databse Selection/Creation
mydb=myclient["PythonTutorial"]

#Collection Selection/Creation  --  Table
mycol=mydb["FirstCollection"]

#Inserting One Data
# mydict={"name":"John","address":"NY"}
# x=mycol.insert_one(mydict)
# print(x.inserted_id)

#Inserting Multiple by loop
# mydict=[{"name":"John","address":"NY"},{"name":"Abs","address":"USA"}]
# for i in mydict:
#     mycol.insert_one(i)


#Insert Multiple
# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
# x=mycol.insert_many(mylist)
# print(x.inserted_ids)


# Inserting your own ID
# mylist = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
# mycol.insert_many(mylist)

#Fetching one object/row
# x=mycol.find_one()
# print(x)

# Fetching all object/row
# x=mycol.find()
# for obj in x:
#     print(obj)

#Fetching Specific Keys
# x=mycol.find({},{"_id":0,"name":0})
# for obj in x:
#     print(obj)

#Fetching specific Object
# myquery={"name":"Viola"}
# x=mycol.find(myquery)
# for obj in x:
#     print(obj)

#Deleting Specific Object
# myquery={"name":"Viola"}
# mycol.delete_one(myquery)

#Deleting multiple Specific Object
# myquery={"name":"Chuck"}
# mycol.delete_many(myquery)

#Deleting Whole Collection/Table
# mycol.drop()

#Update One
# myquery={"name":"Viola"}
# newvalues={"$set":{"address":"Canyon 123"}}

# mycol.update_one(myquery,newvalues)

#Fetching all values
# myresult=mycol.find()
# for obj in myresult:
#     print(obj)

#Finding Values that start after O
# myquery={"address":{"$gt":"O"}}
# x=mycol.find(myquery)
# for obj in x:
#     print(obj)

#Finding Values that start With O
# myquery={"address":{"$regex":"^O"}}
# x=mycol.find(myquery)
# for obj in x:
#     print(obj)

#Finding Values in Sorted Order
x=mycol.find().sort("name")
for obj in x:
    print(obj)
