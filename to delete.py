# http://127.0.0.1:5000/spartan_add
@flask_object.route('/spartan_add', methods = ["POST"])
def add_spartans():
    spartan_data = request.json
    spartan_id = spartan_data['spartan_id']
    first_name = spartan_data['f_name']
    last_name = spartan_data['l_name']
    birth_year = spartan_data['b_year']
    birth_month = spartan_data['b_month']
    birth_day = spartan_data['b_day']
    sp_course = spartan_data['course']
    sp_stream = spartan_data['stream']
    # call the methods that will create the employee record
    return f"The Spartans ({spartan_id}-{first_name} - {last_name}- {birth_year} - {birth_month} - {birth_day}- {sp_course} - {sp_stream})" \
           f" will be added to the database."
# http://127.0.0.1:5000/spdb/spartans/101
# @spartans_app.route('/spdb/spartans/<spId>',methods=['GET'])
# def getSp(spId):
#     data = [ sp for sp in sp_DB if (sp['id'] == spId) ]
#     return jsonify({'spartan': data})
#
#
# @spartans_app.route('/spdb/spartans/<empId>',methods=['PUT'])
# def updateSp(spId):
#     Spartan = [ sp for sp in sp_DB if (sp['id'] == spId) ]
#     if 'first_name' in request.json :
#         Spartan[0]['first_name'] = request.json['first_name']
#     if 'last_name' in request.json:
#         Spartan[0]['Last_name'] = request.json['last_name']
#     return jsonify({'spartan': Spartan[0]})



# # http://127.0.0.1:5000/spartan_record/1
# @flask_object.route('/spartan/<spartan_id>', methods=['GET'])
# def spartan_record_getter(spartan_id):
#     sp_data = jsonify(id=spartan_id, f_n="first_name", l_n="last_name", b_y="birth_year",
#     b_m="birth_month", b_d="birth_day", sp_course="course", sp_stream="stream")
#     return f"Your asking for information about spartan ID: {spartan_id}"
#
#
# # http://127.0.0.1:5000/spartan/add
# @flask_object.route('/spartan_add', methods = ["POST"])
# def add_spartans():
#     spartan_data = request.json
#     spartan_id = spartan_data['spartan_id']
#     first_name = spartan_data['f_name']
#     last_name = spartan_data['l_name']
#     birth_year = spartan_data['b_year']
#     birth_month = spartan_data['b_month']
#     birth_day = spartan_data['b_day']
#     sp_course = spartan_data['course']
#     sp_stream = spartan_data['stream']
#     # call the methods that will create the employee record
#     return f"The Spartans ({spartan_id}-{first_name} - {last_name}- {birth_year} - {birth_month} - {birth_day}- {sp_course} - {sp_stream})" \
#            f" will be added to the database."

# #http://127.0.0.1:5000/spartan/remove?id=2
# @flask_object.route('/spartan/remove', methods=['POST'])
# def remove_spartan():
