from CLI_BOT.Helpers.cli_bot_helper import bot_helper as helper
from CLI_BOT.Models.models import AddressBook  


def main():
    addressBook = AddressBook()
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
            print(helper.add_contact(args, addressBook))
        elif command == "change":
            print(helper.change_phone(args, addressBook))
        elif command == "phone":
            print(helper.get_phone(args, addressBook))
        elif command == "all":
            print(helper.all(args, addressBook))
        elif command == "add-birthday":
            print(helper.add_birthday(args, addressBook))
        elif command == "show-birthday":
            print(helper.show_birthday(args, addressBook))
        elif command == "birthdays":
            print(helper.birthdays(args, addressBook))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()