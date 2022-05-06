import json
def checkKVL(id):
    section_no = id[2]
    with open('KVL.json', 'r') as file:
        kvl = file.read()
    kvl = json.loads(kvl)
    if section_no in kvl:
        key = kvl[section_no]
        #print(key)
        return True, key
    else:
        return False, ""