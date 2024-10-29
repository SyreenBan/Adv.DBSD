from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

# List of pets, showing related kind information
@app.route("/")
@app.route("/list")
def get_list():
    rows = database.retrieve_pet_list()
    return render_template("list.html", rows=rows)

# Create a new pet with a dropdown to select kind
@app.route("/create", methods=['GET', 'POST'])
def get_post_create():

    if request.method == 'GET':
        kinds = database.retrieve_kinds()
        # print (kinds)
        return render_template("create.html", kinds=kinds)
    
    if request.method == 'POST':
        data = dict(request.form)
        print(data)
        try:
            data["age"] = int(data["age"])
        except:
            data["age"] = 0
        print(data)

        pet_list = database.create_pet(data)
        return redirect(url_for('get_list'))

# Update an existing pet, allows kind to be changed
@app.route("/update/<id>", methods=['GET', 'POST'])
def get_update(id):
    if request.method == 'GET':

        kinds = database.retrieve_kinds()
        pet = database.retrieve_pet_obj(id) 

        if pet is None:
            return "Pet not found", 
        
        print(pet)
        return render_template("update.html", pet=pet, kinds=kinds)
    
    if request.method == 'POST':
        data = dict(request.form)        
        try:
            data["Age"] = int(data["Age"])  # Ensure the field matches the database schema
        except (ValueError, KeyError):
            data["Age"] = 0
        
        if "Kind_id" in data:
            data["Kind_id"] = ObjectId(data["Kind_id"])
        # print(data)
        database.update_pet(id, data)  # Assuming update_pet is defined to work with MongoDB
        
        return redirect(url_for('get_list'))  # Redirect to the list of pets after updating


# List of kinds
@app.route("/kind/list")
def list_kinds():
    kinds = database.retrieve_kinds()
    print(kinds)
    return render_template("kind_list.html", kinds=kinds)

