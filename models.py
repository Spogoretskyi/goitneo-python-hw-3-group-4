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
    __date_format = "%d.%m.%Y"

    def __init__(self, birthday):
        try:
           value = datetime.datetime.strptime(birthday, self.__date_format)
        except ValueError:
            return "Incorrect data format, should be d.m.Y"
        super().__init__(value)

    def __str__(self):
        return f"{self.value.strftime(self.__date_format)}"


class Record:
    __phone_not_exists = "Phone does not exist in the list."
    
    def __init__(self, name, birthday = None):
        self.name = Name(name)
        self.phones = []
        if birthday != None:
             self.birthday = Birthday(birthday)
        else:
            self.birthday = None
        
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
        if self.birthday:
            return "Birthday was added previously."
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
        return birthdays_per_week 

    def __get_day(date):
        return date.strftime("%A")

    def __has_key(self, value):
        return value in self.data.keys()
    
    def __str__(self):
         return "Address Book:\n" + '\n'.join([f'{value}' for value in self.data.values()])
    



  # Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_birthday("8.11.1994")
jane_record.add_birthday("8.11.1994")
book.add_record(jane_record)
jane_record.show_birthday()

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
#john.add_birthday("1994-8-11")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
#book.delete("Jane")

print(book)

alex = Record("Alex")
alex.add_phone("9994567890")
book.add_record(alex)

hanna = Record("Hanna")
hanna.add_phone("1234567890")
hanna.add_phone("5555555555")
hanna.add_birthday("29.10.1992")
book.add_record(hanna)

jake = Record("Jake") 
jake.add_phone("1155555511")
book.add_record(jake)

book.add_birthday("John", "30.10.1994")
book.add_birthday("Alex", "02.11.1990")
book.add_birthday("Jake", "31.03.1987")

print(book)
print(book.get_birthdays_per_week())