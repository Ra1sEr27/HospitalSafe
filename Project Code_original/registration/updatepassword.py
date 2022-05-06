import symcrytjson,pymongo,json,os
def updatepassword(wanteddoc,decdoc,hashedpassword,key):
    decdoc["password"] = hashedpassword
    updated_encypted_doc = symcrytjson.encryptjson(key,json.dumps(decdoc),"")
    updated_decdoc_string_sorted = json.dumps(decdoc, indent = 3)
    client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
    db = client['Hospital'] #connect to db
    staffcol = db["section{}-staff".format(decdoc["id"][2])]
    staffcol.delete_one(wanteddoc)
    staffcol.insert_one(updated_encypted_doc)
    #delete original local file name
    f = open('./section{}-staff/{}_{}.json'.format(decdoc["id"][2],decdoc["id"],decdoc["name"]), 'w') #delete local file
    f.close()
    os.remove(f.name)
    with open('./section{}-staff/{}_{}.json'.format(decdoc["id"][2],decdoc["id"],decdoc["name"]),'w') as file:
        file.write(updated_decdoc_string_sorted)