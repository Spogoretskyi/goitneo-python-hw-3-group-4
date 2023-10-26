import datetime
import re
from collections import UserDict, defaultdict
from Exceptions.exceptions import DateError 


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
    

class Birthday(Field):
    __date_format = "%d.%m.%Y"

    def __init__(self, birthday):
        try:
           value = datetime.datetime.strptime(birthday, self.__date_format)
        except ValueError:
            raise DateError("Incorrect date, should be format 'd.m.Y'")
        super().__init__(value)

    def __str__(self):
        return f"{self.value.strftime(self.__date_format)}"


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        
    def add_phone(self, phone):
        phn = Phone(phone)
        if phn in self.phones:
            raise ValueError
        self.phones.append(phn)
        return "Phone was added."

    def remove_phone(self, phone):
        phn = Phone(phone)
        if self.__phone_exists(phn):
            self.phones.remove(phn)
            return "Phone was removed."
        raise KeyError

    def edit_phone(self, phone, new_phone):
        phn = Phone(phone)
        if self.__phone_exists(phn):
            self.phones.remove(phn)
            self.phones.append(Phone(new_phone))
            return "Phone was edited."
        raise KeyError

    def find_phone(self, phone):
        phn = Phone(phone)
        if self.__phone_exists(phn):
            return phn
        raise KeyError
    
    def add_birthday(self, birthday):
        if self.birthday:
            raise ValueError
        self.birthday = Birthday(birthday)
        return "Birthday was added."

    def show_birthday(self):
        return self.birthday

    def __phone_exists(self, phone):
        return phone in self.phones
    
    def __str__(self):
        brth = ""
        if self.birthday != None:
            brth += f", birthday: {self.birthday}."

        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{brth}"


class AddressBook(UserDict):
    def add_record(self, data):
        if data in self.data.values():
             raise ValueError
        self.data[data.name] = data
        return "Contact was added."

    def find(self, name):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm]
        return None
    
    def if_contact_exists(self, name):
        return self.__has_key(Name(name))
    
    def add_phone(self, name, phone):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].add_phone(phone)
        raise KeyError

    def edit_phone(self, name, phone, new_phone):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].edit_phone(phone, new_phone) 
        raise KeyError
    
    def remove_phone(self, name, phone):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].remove_phone(phone)
        raise KeyError

    def remove(self, name):
        nm = Name(name)
        if self.__has_key(nm):
            self.data.pop(nm)
            return "Record was removed."
        raise KeyError
    
    def add_birthday(self, name, birthday):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].add_birthday(birthday)
        raise KeyError
    
    def show_birthday(self, name):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].show_birthday()
        raise KeyError
        
    def get_birthdays_per_week(self):
        birthdays_per_week = defaultdict(list)
        current_year = datetime.datetime.today().year
        current_date = datetime.datetime.today().date()

        for value in self.data.values():
            if value.birthday != None:
                name = value.name.value
                birthday = value.birthday.value
                birthday_this_year = (birthday.replace(year = current_year)).date()

                if birthday_this_year < current_date:
                    birthday_this_year.replace(year = current_year + 1)

                delta_days = (birthday_this_year - current_date).days
                if delta_days < 7 and delta_days > 0:
                    day = AddressBook.__get_day(value.birthday.value)

                    if day in ("Saturday", "Sunday"):
                        day = "Monday"
                
                    birthdays_per_week[day].append(name)
        txt = ""
        for k, v in birthdays_per_week.items():
            txt += f"{k}: {'; '.join(n for n in v)}\n"        
        return txt

    def __get_day(date):
        return date.strftime("%A")

    def __has_key(self, value):
        return value in self.data.keys()
    
    def __str__(self):
         return "Address Book:\n" + '\n'.join([f'{value}' for value in self.data.values()])