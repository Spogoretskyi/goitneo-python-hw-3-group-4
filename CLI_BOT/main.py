from Helpers.cli_bot_helper import Bot_helper 
from Models.models import AddressBook  


def main():
    helper = Bot_helper(AddressBook())
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = helper.parse_input(user_input)

        if command.strip() in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(helper.add_contact(args))
        elif command == "change":
            print(helper.change_phone(args))
        elif command == "phone":
            print(helper.get_phone(args))
        elif command == "add-birthday":
            print(helper.add_birthday(args))
        elif command == "show-birthday":
            print(helper.show_birthday(args))
        elif command == "all":
            print(helper.all())
        elif command == "birthdays":
            print(helper.birthdays())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()