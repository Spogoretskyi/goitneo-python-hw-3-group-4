from Decorators.input_error_decorator import input_error 
from Models.models import AddressBook, Record  


class Bot_helper:
    def __init__(self, addressBook : AddressBook):
        self.addressBook = addressBook

    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

    @input_error
    def add_contact(self, args):
        name, phone = args
        name = ''.join(name)
        record = Record(name)
        record.add_phone(phone)
        return self.addressBook.add_record(record)

    @input_error
    def get_phone(self, args):
        name = args
        name = ''.join(name)
        return self.addressBook.find(name)

    @input_error
    def change_phone(self, args):
        name, phone = args
        name = ''.join(name)
        phone = ''.join(phone)
        return self.addressBook.edit_phone(name, phone)
        
    @input_error
    def add_birthday(self, args):
        name, birthday = args
        name = ''.join(name)
        birthday = ''.join(birthday)
        return self.addressBook.add_birthday(name, birthday)

    @input_error
    def show_birthday(self, args):
        name = args
        name = ''.join(name)
        return self.addressBook.show_birthday(name)
    
    def all(self):
        return self.addressBook

    def birthdays(self):
        return self.addressBook.get_birthdays_per_week()