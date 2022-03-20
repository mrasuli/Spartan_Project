#
# # # http://127.0.0.1:5000/spartan_add/
# # @spartan_app.route('/spartan_add', methods=['POST'])
# # def add_spartan():
# #     # spartan_data = request.json
# #     # spartan_id = spartan_data["s_id"]
# #     # spartan_fn = spartan_data["f_name"]
# #     # spartan_ln = spartan_data["l_name"]
# #     # # spartan_by = spartan_data["b_year"]
# #     # # spartan_bm = spartan_data["b_month"]
# #     # # spartan_bd = spartan_data["b_day"]
# #     # # spartan_course = spartan_data["s_course"]
# #     # # spartan_stream = spartan_data["s_stream"]
# #
# #     return f"The Spartan will be added to the database."
#
#
# #http://127.0.0.1:5000/spartan/1
# @spartan_app.route('/spartan/<spartan_id>', methods=['GET'])
# def spartan_getter(spartan_id):
#     # to check the db, read from a file, etc
#     # data = f"To get a spartans id"
#     return f"You are asking for information about spartan ID: {spartan_id}"