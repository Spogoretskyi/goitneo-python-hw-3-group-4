import datetime
import re
from collections import UserDict, defaultdict


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
    def __init__(self, birthday):
        super().__init__(birthday)

    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return self.value == other.value


class Record:
    __phone_not_exists = "Phone does not exist in the list."
    __date_format = "%d.%m.%Y"

    def __init__(self, name, birthday = None):
        self.name = Name(name)
        self.phones = []
        if birthday != None:
            self.__process_birthday(self, birthday)
        
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
    
    def add_birthday(self, birthday):
        if self.birthday != None:
            return "Birthday was added previously."
        self.__process_birthday(self, birthday)

    def show_birthday(self):
        return self.birthday
        
    def __process_birthday(self, birthday):
        try:
           self.birthday = Birthday(datetime.datetime.strptime(birthday, self.__date_format))
        except ValueError:
            return "Incorrect data format, should be DD.MM.YYYY"

    def __phone_exists(self, phone):
        return phone in self.phones
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, {'birthday:' + self.birthday.value: if self.birthday != None}"


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
    
    def add_birthday(self, name, birthday):
        nm = Name(name)
        if self.__has_key(nm):
            self.data[nm].add_birthday(birthday)
            return "Birthday was added."
        return self.__name_not_exists
    
    def show_birthday(self, name):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].show_birthday()
        return  self.__name_not_exists
        
    def get_birthdays_per_week(self):
        birthdays_per_week = defaultdict(list)
        current_year = datetime.today().year
        current_date = datetime.today().date()

        for value in self.data.values():
            if value.birthday != None:
                name = value.name.value
                birthday = value.birthday.value
                birthday_this_year = birthday.replace(year = current_year)

        if birthday_this_year < current_date:
            birthday_this_year.replace(year = current_year + 1)

        delta_days = (birthday_this_year - current_date).days
        if delta_days < 7 and delta_days > 0:
            day = self.__get_day(value.birthday.value)

            if day in ("Saturday", "Sunday"):
                day = "Monday"
            
            birthdays_per_week[day].append(name)
        return birthdays_per_week

    def __get_day(date):
        return date.strftime("%A")

    def __has_key(self, value):
        return value in self.data.keys()
    
    def __str__(self):
         return "Address Book:\n" + '\n'.join([f'{value}' for value in self.data.values()])