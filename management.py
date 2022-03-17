from spartan import Spartans

def read_option_a():
    while True:
        user_option = input(
            "This is a list of your options: \n 1): Add a Spartan  \n 2): Remove a Spartan \n 3): List the Employees \n 4): Update Employee Data \n 5): Exit the app\n 6): save to JSON file\n 7): load from JSON")
        user_option = user_option.strip()
        if user_option in ["add", "remove", "update", "list", "exit", "save", "load"]:
            return user_option
        else:
            print("Error, You should select one of the options in the list")