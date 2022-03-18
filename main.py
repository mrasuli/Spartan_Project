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

#localhost:5000/spartan/1
@spartans_app.route('/spartan/<spartan_id>', methods =['GET'])
def spartan_get(spartan_id):
    data = jsonify(management.create_spartan_ob(spartan_id))
    return data


if __name__ == "__main__":

    spartans_app.run()