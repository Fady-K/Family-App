import database
#######################
UPDATE_PROMPT = """
A) Update age
B) Update address
C) Update mobile
D) Update email

Your choice: """

MENU_PROMPT = """ --- Family App ---
1) Add a new kin
2) See all kins
3) Find a kin by name (First, Last)
4) Update
5) Display the oldest kin
6) Display the youngest kin
7) Delete a kin
8) Clear all kins
9) Exit

Your selection: """


CLEAR_PROMPT = """This will remove all kins!!
Are you sure? (y/n) : """


def update():
    user_input = input(UPDATE_PROMPT).upper()
    if user_input == "A":
        first_name = input("First_name: ")
        last_name = input("Last_name: ")
        new_age = int(input("NEW_age: "))
        database.update_age(first_name, last_name, new_age)
        print(f"{'#' * 20}\n!!UPDATED {first_name} {last_name} SUCCESSFULLY!!\n{'#' * 20}".upper())

    elif user_input == "B":
        first_name = input("First_name: ")
        last_name = input("Last_name: ")
        new_address = input("NEW_address: ")
        database.update_address(first_name, last_name, new_address)
        print(f"{'#' * 20}\n!!UPDATED {first_name} {last_name} SUCCESSFULLY!!\n{'#' * 20}".upper())

    elif user_input == "C":
        first_name = input("First_name: ")
        last_name = input("Last_name: ")
        new_mobile = input("NEW_mobile: ")
        database.update_mobile(first_name, last_name, new_mobile)
        print(f"{'#' * 20}\n!!UPDATED {first_name} {last_name} SUCCESSFULLY!!\n{'#' * 20}".upper())

    elif user_input == "D":
        first_name = input("First_name: ")
        last_name = input("Last_name: ")
        new_email = input("NEW_email: ")
        database.update_email(first_name, last_name, new_email)
        print(f"{'#' * 20}\n!!UPDATED {first_name} {last_name} SUCCESSFULLY!!\n{'#' * 20}".upper())

    else:
        print(f"{'#' * 20}\nInvalid Try Again!\n{'#' * 20}")


def clear():
    if (q := input(CLEAR_PROMPT).lower()) == "y":
        database.clear_table()
        print(f"{'#' * 20}\n!! Table is clear !!\n{'#' * 20}")
    elif q == "n":
        pass
    else:
        pass


def menu():
    database.create_table()
    while (user_input := input(MENU_PROMPT)) != "9":  # WALRUS operator := helps to assign variable to value "inside experssion"
        if user_input == "1":
            first_name = input("First_name: ")
            last_name = input("Last_name: ")
            kinship = input("Kinship: ").capitalize()
            age = input("Age: ")
            address = input("Address: ").upper()
            mobile = input("Mobile: ")
            email = input("Email: ")

            database.add_kin(first_name, last_name, kinship, age, address, mobile, email)
            print(f"{'#' * 20}\n!! successful !!\n{'#' * 20}".upper())

        elif user_input == "2":
            print(f"{'#' * 20}\n{database.get_all_kins()}\n{'#' * 20}")

        elif user_input == "3":
            first_name = input("First_name: ").replace(" ", "")
            last_name = input("Last_name: ").replace(" ", "")
            kin = database.get_kin_by_name(first_name, last_name)
            print(f"{'#' * 20}\n{kin}\n{'#' * 20}")

        elif user_input == "4":
            update()

        elif user_input == "5":
            kin = database.get_oldest_kin()
            print(f"{'#' * 20}\nThe Oldest: {kin[1]} {kin[2]}\n{'#' * 20}")

        elif user_input == "6":
            kin = database.get_youngest_kin()
            print(f"{'#' * 20}\nThe Youngest: {kin[1]} {kin[2]}\n{'#' * 20}")

        elif user_input == "7":
            first_name = input("First_name: ")
            last_name = input("Last_name: ")
            database.delete_kin(first_name, last_name)
            print(f"{'#' * 20}!! {first_name} {last_name} successfully deleted !!{'#' * 20}".upper())

        elif user_input == "8":
            clear()

        else:
            print(f"{'#' * 20}\nInvalid Try Again!\n{'#' * 20}")


menu()
