from spartan import Spartans
import json

all_spartans_dict = {}

def get_all():
    list = {}
    with open("data.json", "r") as json_file:
        list = json.load(json_file)
    return list

def create(newSpartan):
    spartanToCreate = Spartans(newSpartan["spartan_id"], newSpartan["first_name"], newSpartan["last_name"],
                            newSpartan["birth_year"], newSpartan["birth_month"], newSpartan["birth_day"],
                            newSpartan["sp_course"], newSpartan["sp_stream"])

    if len(spartanToCreate.get_first_name()) < 2:
        return "Error: first name needs to have at least 2 characters"

    if len(spartanToCreate.get_last_name()) < 2:
        return "Error: last name needs to have at least 2 characters"

    load_jsonfile()
    all_spartans_dict[spartanToCreate.get_spartan_id()] = spartanToCreate
    save_to_jsonfile()
    return "Spartan has been saved"

def get_spartan(spartan_id):
    load_jsonfile()
    spartan = all_spartans_dict[int(spartan_id)]
    return spartan

def remove_spartan(spartan_id):
    load_jsonfile()
    del all_spartans_dict[int(spartan_id)]
    save_to_jsonfile()

def save_to_jsonfile():
    global all_spartans_dict
    temp_spartans = {}

    for spartan_id in all_spartans_dict:
        spartan = all_spartans_dict[spartan_id]
        spartan_dict = vars(spartan)
        temp_spartans[spartan_id] = spartan_dict

    with open("data.json", "w") as json_file:
        json.dump(temp_spartans, json_file)

    print("Data is stored in data.json")

def load_jsonfile():
    global all_spartans_dict

    temp_dict = {}
    all_spartans_dict = {}
    with open("data.json", "r") as json_file:
        temp_dict = json.load(json_file)

    for key_id in temp_dict:
        spartan = temp_dict[key_id]

        temp_spartan = Spartans(spartan["spartan_id"], spartan["first_name"],
                                spartan["last_name"], spartan["birth_year"],
                                spartan["birth_month"], spartan["birth_day"],
                                spartan["sp_course"], spartan["sp_stream"])

        all_spartans_dict[temp_spartan.get_spartan_id()] = temp_spartan