from flask import Flask, request, jsonify

flask_object = Flask(__name__)

# http://127.0.0.1:5000
@flask_object.route('/', methods=['GET'])
def homepage():
    return "Welcome to the Spartan's Management System! "

# http://127.0.0.1:5000/spartan/1
@flask_object.route('/spartan/<spartan_id>', methods=['GET'])
def spartan_getter(spartan_id):
    return f"Get the information about spartan's ID: {spartan_id}"

#
@flask_object.route('/spartan/<spartan_id>', methods=['GET'])
def spartan_record_getter(spartan_id):
    spartan_data = jsonify(id=spartan_id, f_n="first_name", l_n="last_name", b_y="birth_year",
    b_m="birth_month", b_d="birth_day", sp_course="course", sp_stream="stream")
    return f"Your asking for information about spartan ID: {spartan_id}"


if __name__ == "__main__":

    flask_object.run()