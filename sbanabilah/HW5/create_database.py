# from mongita import MongitaClientDisk

# client = MongitaClientDisk(host = "/workspaces/Adv.DBSD/sbanabilah/HW5/.mongita ")  
# db = client["mypetdatabase"]

# collection_pets = db["pet"] 

# collection_kinds = db["kind"] 


# def insert_many_pets(collection_pets, kind_id):
#     pets = [
#         {"name": "Suzy", "age": 3, "Owner": "Greg", "kind_id": kind_id[0]},
#         {"name": "Sandy", "age": 2, "Owner": "Steve", "kind_id": kind_id[1]},
#         {"name": "Dorothy", "age": 1,  "Owner": "Elizabeth", "kind_id": kind_id[2]},
#         {"name": "Heidi", "age": 4,  "Owner": "David", "kind_id": kind_id[0]}]
#     result = collection_pets.insert_many(pets)
#     return result


# def insert_many_kind (collection_kinds):
#     kinds = [
#         {"kind_name": "Dog", "food" : "Dog food", "noise": "Bark"},
#         {"kind_name": "Cat", "food" : "Cat food", "noise": "Meow"},
#         {"kind_name": "Fish", "food" : "Fish flakes", "noise": "Blub"}]

#     result = collection_kinds.insert_many(kinds)
#     return result.inserted_ids 

# kind_id = insert_many_kind (collection_kinds)
# pets = insert_many_pets(collection_pets, kind_id)

# for kind in collection_kinds.find({}):
#     print(kind)

# for pet in collection_pets.find({}):
#     print(pet)