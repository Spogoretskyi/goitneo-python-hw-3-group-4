from CLI_BOT.Decorators.input_error_decorator import input_error 
from CLI_BOT.Models.models import AddressBook, Record  


class Bot_helper: 
    def parse_input(user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

    @input_error
    def add_contact(args, addressBook : AddressBook):
        name, phone = args
        name = ''.join(name)
        record = Record(name)
        record.add_phone(phone)
        return addressBook.add_record(record)

    @input_error
    def get_phone(args, addressBook : AddressBook):
        name = args
        name = ''.join(name)
        return addressBook.find(name)

    @input_error
    def change_phone(args, addressBook : AddressBook):
        name, phone = args
        name = ''.join(name)
        phone = ''.join(phone)
        return addressBook.edit_phone(name, phone)
        
    @input_error
    def add_birthday(args, addressBook : AddressBook):
        name, birthday = args
        name = ''.join(name)
        birthday = ''.join(birthday)
        return addressBook.add_birthday(name, birthday)

    @input_error
    def show_birthday(args, addressBook : AddressBook):
        name = args
        name = ''.join(name)
        return addressBook.show_birthday(name)
    
    def all(addressBook : AddressBook):
        return addressBook

    def birthdays(addressBook : AddressBook):
        return addressBook.get_birthdays_per_week()