from collections import UserDict
from colorama import init, Fore

init()

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)
    
    def validate(self, phone):
        if not (phone.isdigit() and len(phone) == 10):
            raise ValueError(f"{Fore.RED}Error{Fore.RESET}: короткий номер телефону має містити 10 цифр.")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
            return True
        except ValueError as e:
            print(e)
            return False
    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError(f"Phone {old_phone} not found in record.")
    def delete_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError(f"Phone {phone} not found in record.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record
        
    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values()) if self.data else "Address book is empty."

# для тестування
def main():
    book = AddressBook()

    # Створення та додавання нового запису для John
    john_record = Record("John")
    # спроба додати короткий телефон
    print(f"{Fore.YELLOW}спроба додати короткий телефон{Fore.RESET}")
    john_record.add_phone("123")
    
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)
    
    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # перевірка чи додалися 2 записи
    print(f"{Fore.BLUE}перевірка чи додалися 2 записи{Fore.RESET}\n{book}")


    print(f"{Fore.BLUE}вивід перебором {Fore.RESET}")
    for name, record in book.data.items():
        print(record)

    print(f"{Fore.BLUE}вивід відредагованого{Fore.RESET}")
    john = book.find("John")
    john.edit_phone("5555555555", "1112223333")
    print(john) 


    print(f"{Fore.BLUE}test пошуку{Fore.RESET} чий це телефон - 1112223333")
    found_phone = john.find_phone("1112223333")
    print(f"{john.name}: {found_phone}")

    print(f"{Fore.BLUE}test видалення Jane{Fore.RESET}")
    book.delete("Jane")
    jane = book.find("Jane")
    if jane is None:
        print("Jane's record has been deleted.")
    print(f"{Fore.BLUE}Address book після видалення:{Fore.RESET}\n{book}")

if __name__ == "__main__":
    main()