import re
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)

    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return self.value == other.value


class Phone(Field):
    __pattern = r'^\d{10}$'

    def __init__(self, phone):
        if not re.match(self.__pattern, phone):
            raise ValueError("Phone should contains 10 digits only")
        super().__init__(phone)

    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return self.value == other.value


class Record:
    __phone_not_exists = "Phone does not exist in the list."

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phn = Phone(phone)
        if self.__phone_exists(phn):
            return "Phone exists in the list."
        self.phones.append(phn)
        return "Phone was added."

    def remove_phone(self, phone):
        phn = Phone(phone)
        if self.__phone_exists(phn):
            self.phones.remove(phn)
            return "Phone was removed."
        return self.__phone_not_exists

    def edit_phone(self, phone, new_phone):
        phn = Phone(phone)
        if self.__phone_exists(phn):
            self.phones.remove(phn)
            self.phones.append(Phone(new_phone))
            return "Phone was edited."
        return self.__phone_not_exists

    def find_phone(self, phone):
        phn = Phone(phone)
        if self.__phone_exists(phn):
            return phn
        return self.__phone_not_exists

    def __phone_exists(self, phone):
        return phone in self.phones
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    __name_not_exists = "Name not exists in the Address Book."
    
    def add_record(self, data):
        if data in self.data.values():
            return "Record has already exists in the Address Book."
        self.data[data.name] = data
        return "Record was added."

    def find(self, name):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm]
        return self.__name_not_exists

    def delete(self, name):
        nm = Name(name)
        if self.__has_key(nm):
            self.data.pop(nm)
            return "Record was removed."
        return self.__name_not_exists

    def __has_key(self, value):
        return value in self.data.keys()
    
    def __str__(self):
         return "Address Book:\n" + '\n'.join([f'{value}' for value in self.data.values()])