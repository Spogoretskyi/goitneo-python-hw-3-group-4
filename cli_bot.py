def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name please."
        except IndexError:
            return "Give me name and phone please."
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    name = ''.join(name)
    if is_contact_exists(name, contacts):
        raise IndexError
    contacts[name] = phone
    return "Contact added."


@input_error
def username_phone(args, contacts):
    name = args
    name = ''.join(name)
    if is_contact_exists(name, contacts):
        return contacts[name]
    else:
        raise KeyError


@input_error
def change_username_phone(args, contacts):
    name, phone = args
    name = ''.join(name)
    phone = ''.join(phone)
    if is_contact_exists(name, contacts):
        contacts[name] = phone
        return "Phone was changed."
    else:
        raise KeyError


def is_contact_exists(name, contacts):
     if contacts.get(name) != None:
         return True
     return False


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