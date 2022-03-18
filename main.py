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


#localhost:5000/spartan/1
@spartans_app.route('/spartan/<spartan_id>', methods =['GET'])
def spartan_get(spartan_id):
    data = jsonify(management.create_spartan_ob(spartan_id))
    return data


if __name__ == "__main__":

    spartans_app.run()