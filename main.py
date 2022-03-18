from flask import Flask, request, jsonify
import management
from spartan import Spartans


spartans_app = Flask(__name__)
# this will create an app object from the flask


# http://localhost:5000/
@spartans_app.route('/', methods=['GET'])
def homepage():
    homepage_content = "Welcome to the Spartan's Management System! \n" \
           "What is an API?\n" \
           "API is the acronym for Application Programming Interface, " \
           "which is a software intermediary that allows two applications to talk to each other. " \
           "Each time you use an app like Facebook, send an instant message, or check the weather on your phone, you're using an API. \n"
    return homepage_content

# we will creat a URI named spdb/spartans and we will define the method as get. Flask will call the function getAllSp as argument.
# now we will develop a rest service to get an employee with a given id
# the bellow code will find the spartan id with the given id and send the json object to the data.
# the request.json will contain the JSON object set in the client request.

#localhost:5000/spartan/add/
@spartans_app.route('/spartan/add', methods = ['POST'])
def spartan_add():
    spartan_data = request.json

    if len(spartan_data["first_name"]) >= 2:
        sp_fn = spartan_data["first_name"]
    else:
        return "Error, the Spartans First Name should be at least 2 Characters"

    if len(spartan_data["last_name"]) >= 2:
        sp_ln = spartan_data["last_name"]
    else:
        return "ERROR, the Spartans last name should have at least 2 characters."

    if int(spartan_data["birth_year"]) in range(1900, 2004):
        sp_by = spartan_data["birth_year"]
    else:
        return "ERROR, the Spartans birth year should be a number between 1900 and 2004."

    if int(spartan_data["birth_month"]) in range(1, 13):
        sp_bm = spartan_data["birth_month"]
    else:
        return "ERROR, the Spartans birth month should be a number between 1 and 12."

    if int(spartan_data["birth_day"]) in range(1, 32):
        sp_bd = spartan_data["birth_day"]
    else:
        return "ERROR, the Spartans birth day should be a number between 1 and 31."

    if len(spartan_data["course"]) >= 2:
        sp_course = spartan_data["course"]
    else:
        return "ERROR, the Spartans Course name should have at least 2 characters."

    if len(spartan_data["stream"]) >= 2:
        sp_stream = spartan_data["stream"]
    else:
        return "ERROR, the Spartans Stream name should have at least 2 characters."

    if management.check_if_id_db(spartan_data["sparta_id"]):
        return "ID already in database."
    else:
        spartan_id = spartan_data["sparta_id"]
        tempo_spartan = Spartans(spartan_id, sp_fn, sp_ln, sp_bd, sp_bm, sp_by, sp_course, sp_stream)
        management.create_spartan_ob(tempo_spartan)
        management.save_to_json()
        return "Entry saved."


#localhost:5000/spartan/1
@spartans_app.route('/spartan/<spartan_id>', methods =['GET'])
def spartan_get(spartan_id):
    data = jsonify(management.create_spartan_ob(spartan_id))
    return data


#localhost:5000/spartan/list
@spartans_app.route('/spartan', methods=['GET'])
def sp_list():
    sp_db = management.display_db()
    return sp_db



if __name__ == "__main__":

    spartans_app.run()