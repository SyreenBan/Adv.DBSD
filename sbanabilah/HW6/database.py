from pymongo import MongoClient
from bson import ObjectId

MONGO_URI = 'mongodb+srv://sbanabil:mAYdo4vAwDQGM7Ur@pets.alnef.mongodb.net/'
try:
    # Ensure SSL is enabled and TLS settings are compatible
    client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=False)
    print("Connected to MongoDB Atlas successfully!")

    pets_db = client.get_database("pets")  # Replace with your database name
    # Specify the database you want to check
        

except Exception as e:
    print("An error occurred while connecting to MongoDB:", e)

def create_database():
    pets_db = client.get_database("pets")

    pets_db.drop_collection("pet_collection")
    pets_db.drop_collection("kind_collection")

    pet_collection = pets_db.pet_collection
    kind_collection = pets_db.kind_collection
    
    kinds_result = kind_collection.insert_many([
        {"Kind_name": "Dog", "Food" : "Dog food", "Noise": "Bark"},
        {"Kind_name": "Cat", "Food" : "Cat food", "Noise": "Meow"},
        {"Kind_name": "Fish", "Food" : "Fish flakes", "Noise": "Blub"}])
    
    Kind_id = kinds_result.inserted_ids

    pets_result = pet_collection.insert_many([
        {"Name": "Suzy", "Age": 3, "Owner": "Greg", "Kind_id": Kind_id[0]},
        {"Name": "Sandy", "Age": 2, "Owner": "Steve", "Kind_id": Kind_id[1]},
        {"Name": "Dorothy", "Age": 1,  "Owner": "Elizabeth", "Kind_id": Kind_id[2]},
        {"Name": "Heidi", "Age": 4,  "Owner": "David", "Kind_id": Kind_id[0]}])

def create_pet(data):
    pets_db = client.get_database("pets")
    pet_collection = pets_db.pet_collection
    try:
        data['Age'] = int(data['Age'])
        data['Kind_id'] = ObjectId(data['Kind_id'])
        result = pet_collection.insert_one(data)
        print(f"Inserted pet with id: {result.inserted_id}")
    except Exception as e:
        print(f"Error inserting pet: {e}")

def retrieve_pet_list():
    pets_db = client.get_database("pets")
    pet_collection = pets_db.pet_collection
    kind_collection = pets_db.kind_collection

    pets = pet_collection.find({})

    kinds = {kind['_id']: kind for kind in kind_collection.find({})}
    
    result = []
    for pet in pets:
        kind = kinds.get(pet['Kind_id'])
        if kind:
            item = (pet['_id'], pet['Name'], pet['Age'], pet['Owner'], kind['Kind_name'], kind['Food'], kind['Noise'])
            result.append(item)
    return result

def retrieve_pet_obj(id):
    pets_db = client.get_database("pets")
    pet_collection = pets_db.pet_collection
    
    try:
        pet = pet_collection.find_one({"_id": ObjectId(id)})
        print (pet)  
        if pet is not None:
            return pet  
        else:
            return None  
    except Exception as e:
        print(f"Error retrieving pet: {e}")
        return None  


def update_pet(id, update_data):
    pets_db = client.get_database("pets")
    pet_collection = pets_db.pet_collection

    try:
        # Update the pet with the given id
        result = pet_collection.update_one(
            {"_id": ObjectId(id)},  # Filter by the pet's ID
            {"$set": update_data}   # Update the fields specified in update_data
        )
        
        if result.modified_count > 0:
            print(f"Pet with id {id} updated successfully.")
        else:
            print(f"No pet found with id {id} or no changes made.")
    except Exception as e:
        print(f"Error updating pet: {e}")

def delete_pet(id):
    pets_db = client.get_database("pets")
    pet_collection = pets_db.pet_collection
    
    try:
        result = pet_collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            print(f"Pet with id {id} deleted successfully.")
        else:
            print(f"No pet found with id {id}.")
    except Exception as e:
        print(f"Error deleting pet: {e}")

def create_kind(data):
    pets_db = client.get_database("pets")
    kind_collection = pets_db.kind_collection
    try:
        result = kind_collection.insert_one(data)
        print(f"Inserted kind with id: {result.inserted_id}")
    except Exception as e:
        print(f"Error inserting pet: {e}")

def retrieve_kinds():
    pets_db = client.get_database("pets")
    kind_collection = pets_db.kind_collection
    
    kinds = kind_collection.find({})
    result = []
    for kind in kinds:
        item = (kind['_id'], kind['Kind_name'], kind['Food'], kind['Noise'])
        result.append(item)
    return result

def update_kind(id, update_data):
    pets_db = client.get_database("pets")
    kind_collection = pets_db.kind_collection
    
    try:
        result = kind_collection.update_one(
            {"_id": ObjectId(id)},  # Filter by the kind's ID
            {"$set": update_data}    # Update the fields specified in update_data
        )
        
        if result.modified_count > 0:
            print(f"Kind with id {id} updated successfully.")
        else:
            print(f"No kind found with id {id} or no changes made.")
    except Exception as e:
        print(f"Error updating kind: {e}")

def retrieve_kind(id):
    pets_db = client.get_database("pets")
    kind_collection = pets_db.kind_collection
    id = ObjectId(id)
    kind = kind_collection.find_one({"_id":id})
    kind["id"] = str(kind["_id"])
    del kind["_id"]
    return kind

def delete_kind(id):
    pets_db = client.get_database("pets")
    kind_collection = pets_db.kind_collection

    try:
        result = kind_collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            print(f"Kind with id {id} deleted successfully.")
        else:
            print(f"No kind found with id {id}.")
    except Exception as e:
        print(f"Error deleting kind: {e}")

create_database()
result_list = retrieve_pet_list()
# for item in result_list:
#     print(item)

# result_kind = retrieve_kinds()
# for item in result_kind:
#     print(item)