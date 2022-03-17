from spartan import Spartans

def spartans_read_option():
    while True:
        user_option = input("This is a list of your options: \n 1): Add a Spartan  \n 2): Remove a Spartan \n 3): List the Spartans \n 4): Update a Sparatan's Data \n 5): Exit the app \n")
        user_option = user_option.strip()
        if user_option in ["add", "remove", "update", "list", "exit"]:
            return user_option
        else:
            print("Error, You should select one of the options in the list")


def read_spartans_id():
    while True:
        id_str = input("Please Enter the Spartan's ID:")
        id_str = id_str.strip()

        if id_str.isdigit():
            sp_id = int(id_str)
            if sp_id > 0:
                return sp_id
            else:
                print("Error, The Spartan's ID should be positive number")
        else:
            print("Error, The Spartan's ID should be a number")

def read_first_name():
    while True:
        first_name = input("Please Enter The Spartan's First Name:")
        first_name = first_name.strip()

        if len(first_name) >= 2:
            return first_name
        else:
            print("Error, The Employee First Name should be at least 2 Characters")


def read_last_name():
    while True:
        last_name = input("Please Enter The Spartan's Last Name:")
        last_name = last_name.strip()

        if len(last_name) >= 2:
            return last_name
        else:
            print("Error, The Spartan's Last Name should be at least 2 Characters")


def read_year():
    while True:
        year_str = input("Please Enter the Spartan's Birth Year:")
        year_str = year_str.strip()

        if year_str.isdigit():
            year = int(year_str)
            if (year >= 1900) and (year <= 2004):
                return year
            else:
                print("Error, The Spartan's Birth Year should be between 1900 and 2004")
        else:
            print("Error, The Spartan's Birth Year should be a number")


def read_month():
    while True:
        month_str = input("Please Enter the Spartan's Birth Month:")
        month_str = month_str.strip()

        if month_str.isdigit():
            month = int(month_str)
            if (month >= 1) and (month <= 12):
                return month
            else:
                print("Error, The Spartan's Birth Month should be between 1 and 12")
        else:
            print("Error, The Spartan's Birth Month should be a number")


def read_day():
    while True:
        day_str = input("Please Enter the Spartan's Birth Day:")
        day_str = day_str.strip()

        if day_str.isdigit():
            day = int(day_str)
            if (day >= 1) and (day <= 31):
                return day
            else:
                print("Error, The Spartan's Birth Day should be between 1 and 31")
        else:
            print("Error, The Spartan's Birth Day should be a number")

# both course and streams can be string and numbers
def read_spartans_course():
    while True:
        spartan_course = input(str("Please enter the Course you are in:"))
        spartan_course = spartan_course.strip()
        if len(spartan_course) >= 0:
            return spartan_course
        else:
            print("Error, the Course should be in characters")

def read_spartans_stream():
    while True:
        spartan_stream = input(str("Please enter the Stream you are in:"))
        spartan_stream = spartan_stream.strip()
        if len(spartan_stream) >= 0:
            return spartan_stream
        else:
            print("Error, the Stream should be in characters")


def create_spartan_ob():
        spartan_id = read_spartans_id()
        spartan_first_name = read_first_name()
        spartan_last_name = read_last_name()
        spartan_birth_year = read_year()
        spartan_birth_month = read_month()
        spartan_birth_day = read_day()
        spartan_course = read_spartans_course()
        spartan_stream = read_spartans_stream()

        spartan = Spartans(spartan_id, spartan_first_name, spartan_last_name, spartan_birth_year, spartan_birth_month,
                            spartan_birth_day, spartan_course, spartan_stream)

        return spartan


def print_all_spartan_data():
    for spartan_id_key in all_spartan_dict:
        print(f"The data of the employee with Employee_ID = {spartan_id_key}")
        print(all_spartan_dict[spartan_id_key])


def add_spartan():
    spartan = create_spartan_ob()
    spartans_db[spartan.get_spartan_id()] = spartan
    print("The Spartan was added to the list")

def remove_spartan():
    global employees_db
    remove_id_str = input("PLease enter the iD you would like to remove from the data base: ")
    if remove_id_str.isdigit() and int(remove_id_str) in spartans_db:
        remove_id = int(remove_id_str)
    del spartans_db[int(remove_id)]
    print(f"The Spartan with {remove_id} has now been removed from the database.")


def print_spartan_db():
    global spartan_db
    for entry in spartans_db:
        print(spartans_db[entry])


def read_option():
    while True:
        field_option = input("Please Enter the field you want to update: spartan_id, first_name, last_name, birth_year, "
        "birth_month, birth_day, sp_course, sp_stream:")
        field_option = field_option.strip()
        if field_option in ["spartan_id", "first_name", "last_name", "birth_year", "birth_month", "birth_day","sp_course", "sp_stream"]:
            return field_option
    else:
            print("Please enter one of the mentioned fields")


def update_spartans_data(spartan_id):
        field_option = read_option()
        if field_option == "first_name":
            new_first_name = read_first_name()
            all_spartan_dict[spartan_id].set_first_name = new_first_name
        elif field_option == "last_name":
            new_last_name = read_last_name()
            all_spartan_dict[spartan_id].set_last_name = new_last_name
        elif field_option == "birth_year":
            new_birth_year = read_year()
            all_spartan_dict[spartan_id].set_birth_year = new_birth_year
        elif field_option == "birth_month":
            new_birth_month = read_month()
            all_spartan_dict[spartan_id].set_birth_month = new_birth_month
        elif field_option == "birth_day":
            new_birth_day = read_day()
            all_spartan_dict[spartan_id].set_birth_day = new_birth_day
        elif field_option == "sp_course":
            new_sp_course = read_spartans_course()
            all_spartan_dict[spartan_id].set_sp_course = new_sp_course
        elif field_option == "sp_stream":
            new_sp_stream = read_spartans_stream()
            all_spartan_dict[spartan_id].set_sp_stream = new_sp_stream

        print(f"Field{field_option} for entry iD {spartan_id} has been changed.")



if __name__ == "__main__":

    all_spartan_dict = {}

    while True:
        option = spartans_read_option()
        # for the main options

        if option == "add":
            print("The user wants to add a Spartan")
            spartan_object = Spartans[create_spartan_ob]
            # log_file.write("you have added an employee.")

            spartan_id = spartan_object.get_spartan_id()
            all_spartan_dict[spartan_id] = spartan_object
            print(all_spartan_dict.get(spartan_id))
            print(all_spartan_dict)


        elif option == "remove":
            print("The user wants to remove a Spartan \n")
            employee_id = read_spartans_id()
            del all_spartan_dict[spartan_id]
            # log_file.write("you have removed an employee \n")

        elif option == "list":
            print("The user wants a list of the Spartans")
            for spartan_id in all_spartan_dict:
                employee_object = all_spartan_dict[spartan_id]
                print(all_spartan_dict[spartan_id])
            # log_file.write("You have listed the total number of employees \n")
            # print_all_employees_data()

        elif option == "update":
            print("The user wants to update the data of an employee")
            spartan_id = read_spartans_id()
            update_spartans_data(spartan_id)
            # log_file.write("you have updated an employee \n")

        elif option == "exit":
            # log_file.write("you have exited the Spartans Management System \n")
            print("Thanks, see you later")
            break
        # elif option == "save":
        #     print("The data will be saved to json file")
        #     save_to_json()
        # elif option == "load":
        #     print("the data will be loaded from a JSON file")
        #     load_from_json()
        else:
            print("Unknown option")
