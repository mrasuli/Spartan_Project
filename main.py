from flask import Flask, request, jsonify
import management

spartan_app = Flask(__name__)

# http://127.0.0.1:5000
@spartan_app.route('/', methods=['GET'])
def home_page():
    home_page_content = "This is the landing page!"
    return home_page_content

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
    return f"You are looking for: {spartan}"

# http://127.0.0.1:5000/spartan/1
@spartan_app.route('/spartan/<spartan_id>', methods=['DELETE'])
def remove_spartan(spartan_id):
    management.remove_spartan(spartan_id)
    return f"You are removing a Spartan ID: {spartan_id}"

# http://127.0.0.1:5000/spartan
@spartan_app.route('/spartan', methods=['GET'])
def spartan_list():
    all_spartans = management.get_all()
    return f"You are looking for the list of spartans: {all_spartans}"

if __name__ == "__main__":

    spartan_app.run(debug=True)