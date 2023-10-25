import CLI_BOT.Helpers
import CLI_BOT.Models.models  


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command.strip() in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(username_phone(args, contacts))
        elif command == "all":
            text = ""
            for k, v in contacts.items():
                text += f"{k} {v}\n"
            print(text)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()