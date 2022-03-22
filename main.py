from flask import Flask, request, jsonify
import management

spartan_app = Flask(__name__)

# http://127.0.0.1:5000
@spartan_app.route('/', methods=['GET'])
def home_page():
    home_page_content = "This is the landing page! \n" \
                        "" \
                        "What is an API? \n" \
                        "" \
                        "API stands for “Application Programming Interface.” " \
                        "An API is a software intermediary that allows two applications to talk to each other.  " \
                        "In other words, an API is the messenger that delivers your request to the provider that you’re requesting it from and then delivers the response back to you."
    return home_page_content


# this is the method for adding a new spartan. We have the request and get the variable and serialise it to json.
# it is passed on to the create function
#http://127.0.0.1:5000/spartan/add
@spartan_app.route('/spartan/add', methods=['POST'])
def add_spartan():
    data = request.get_json()
    result = management.create(data)
    return result
    # this will always return the condition if it is wrong and when it is right

# http://127.0.0.1:5000/spartan/1
@spartan_app.route('/spartan/<spartan_id>')
def spartan_get(spartan_id):
    spartan = management.get_spartan(spartan_id)
    return f"You are looking for spartan with ID {spartan}"

# both add and remove can have the same route but only using different methods

# http://127.0.0.1:5000/spartan/1
@spartan_app.route('/spartan/<spartan_id>', methods=['DELETE'])
def remove_spartan(spartan_id):
    management.remove_spartan(spartan_id)
    return f"You are removing a Spartan ID: {spartan_id}"


# http://127.0.0.1:5000/spartanslist
@spartan_app.route('/spartans/list', methods=['GET'])
def spartan_list():
    all_spartans = management.get_all_spartans()
    return f"You are looking for the list of spartans {all_spartans}"


if __name__ == "__main__":

    spartan_app.run(debug=True)
