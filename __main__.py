from typing import List
import csv

# FileNotFoundError
def read_file(file):
    try:
        with (open(file, 'r', encoding='UTF-8') as f):
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print('Файла нет. Сначала введите данные.\n')
        return []
def show_data(data: list):
    i=1
    for line in data:
        print(f"{i}. {line}", end='')
        i+=1

def save_data(file, data, num_contact, flag_2 ):
    if flag_2:
        temp = 'a'
        num_contact = int(len(data))
    else:
        temp = 'w'
    print('Введите данные контакта: ')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, temp, encoding='UTF-8') as f:
        data.insert(num_contact-1, (f'{first_name}, {last_name}, {patronymic}, {phone_number}\n'))
        for _ in data:
            f.write(_)

def search_data(contacts: List[str]):
    search_str = input('Введите фамилию для поиска: ')
    founded = []
    for contact in contacts:
        if search_str.lower()  in contact.split(', ')[1].lower():
            founded.append(contact)
    return founded

def remove_data(file, data, num_contact):
    with open(file, 'w', encoding='UTF-8') as f:
        c = data.pop(num_contact - 1)
        for i in data:
            f.write(i)
    return c

def rewrite_data(file, data, num_contact):
    with open(file, 'a', encoding='UTF-8') as f:
        f.write(data[num_contact - 1])

def main():
    file_name = 'phone_book.txt'
    file_name_2 = 'phone_book_2.txt'
    flag = True
    num_contact = None
    while flag:
        print('0 - Выход')
        print('1 - Запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - удалить контакт')
        print('5 - правка контакта')
        print('6 - переписать контакт в другой справочник')
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            save_data(file_name, [], None, True)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':
            data = read_file(file_name)
            show_data(data)
            num_contact = int(input("Выберите контакт для удаления: "))
            contact = remove_data(file_name, data, num_contact)
            print(contact)
        elif answer == '5':
            data = read_file(file_name)
            show_data(data)

            num_contact = int(input("Выберите контакт для правки: "))
            remove_data(file_name, data, num_contact)
            save_data(file_name, data, num_contact, False)
        elif answer == '6':
            data = read_file(file_name)
            show_data(data)
            num_contact = int(input("Выберите контакт для записи в другой справочник: "))
            rewrite_data(file_name_2, data, num_contact)


if __name__ == '__main__':
    main()