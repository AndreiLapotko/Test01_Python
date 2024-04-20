from functions import (
    read_txt,
    showAll,
    show_last_array_item,
    show_text_of_note,
    find_by_ID,
    find_by_title,
    find_by_date,
    add_note,
    write_txt,
    change_note,
    delete_by_ID,
)
import datetime


def work_with_notebook():
    choice = show_menu()

    note_book = read_txt("notebook.csv")

    while choice != 9:
        if choice == 1:
            showAll(note_book)

        elif choice == 2:
            ID = input("ID: ")
            show_text_of_note(find_by_ID(note_book, ID))
            # showAll(find_by_ID(note_book, ID))

        elif choice == 3:
            title = input("Заголовок: ")
            
            print(*find_by_title(note_book, title), sep="\t")


        elif choice == 4:
            date = input("Введите дату в формате dd.mm.YYYY: ")
            show_text_of_note(find_by_date(note_book, date))
           

        elif choice == 5:
            ID = len(note_book)
            current_time = datetime.datetime.now()
            # time_stamp = current_time.day + '-' + current_time.month + '-' + current_time.year + ' ' + current_time.hour + ':' + current_time.minute
            time_stamp = current_time.strftime("%d.%m.%Y, %H:%M:%S")
            
            title = input("Введите заголовок: ")
            text = input("Введите текст заметки: ")
            user_data = str(ID) + '_' + title + '_' + time_stamp + '_' + text

            add_note(note_book, user_data)
            write_txt("notebook.csv", note_book)

        elif choice == 6:
            ID = input("Заголовок: ")
            new_note = input("Новая заметка: ")
            print(change_note(note_book, ID, new_note))

        elif choice == 7:
            # ID = int(input("ID: "))
            ID = input("ID: ")
            print(delete_by_ID(note_book, ID))

        elif choice == 8:
            write_txt("notebook.csv", note_book)

        choice = show_menu()


def show_menu():
    print(
        "\nВыберите необходимое действие:\n"
        "1. Отобразить список всех заметок.\n"
        "2. Найти заметку по ID.\n"
        "3. Найти заметку по заголовку.\n"
        "4. Найти заметку по дате.\n"
        "5. Создать заметку.\n"
        "6. Редактировать существующую заметку.\n"
        "7. Удаление заметки по ID.\n"
        "8. Сохранить заметки в текстовом формате.\n"
        "9. Закончить работу.\n"
    )
    choice = int(input())
    return choice
