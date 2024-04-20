def read_txt(filename):
    note_book = []
    fields = ["ID", "Заголовок", "Дата", "Заметка"]

    with open(filename, "r", encoding="utf-8") as ntbk:
        for line in ntbk:
            if len(line) > 5:
                record = dict(zip(fields, line.split(";")))
                note_book.append(record)
    # print(note_book)
    return note_book


# 1
def showAll(note_book):
  
    for i in range(len(note_book)):
        if i == 0:
            for key in note_book[i]:
                if key != 'Заметка':
                    print(key.ljust(15), end="")
            print("\n")
        for y in note_book[i]:
            if y != 'Заметка':
                print(note_book[i][y].strip().ljust(15), end="")
        print("\n")



    # for i in range(len(note_book)):
    #     if i == 0:
    #         for j in note_book[i].keys():
    #             print(j.ljust(15), end="")
    #         print("\n")
    #     for y in note_book[i].values():
    #         print(y.strip().ljust(15), end="")
    #     print("\n")        

def show_last_array_item(array):
    last_item_index = len(array) - 1
    print(array[last_item_index])

def show_text_of_note(array):
    for i in range(len(array)):
        for j in array[i]:
            if j == "Заметка":
                print(array[i][j])
    print("\n")

# 2
def find_by_ID(note_book, ID):
    list1 = []
    for i in note_book:
        if i.get("ID") == ID:
            # list1.append(i["Заметка"])
            list1.append(i)
    if len(list1) == 0:
        list1 = [
            {
                "Заметок с таким ID нет в спиcке!": "Заметок с таким ID нет в спиcке!!!"
            }
        ]
    return list1




# 3
def find_by_title(note_book, title):
    # result = {}
    list1 = []
    for i in note_book:
        if i.get("Заголовок") == title:
            # result = i
            list1.append(i)
            # break
    if len(list1) == 0:
        list1 = [
            {"Заметок с таким названием нет в спиcке!": "The requested title is missing!"}
        ]
    return list1


# 4
def find_by_date(note_book, date):
    list1 = []
    for i in note_book:
        temp = i.get("Дата").split(",")
        # print(temp)
        if temp[0] == date:
            list1.append(i)
    if len(list1) == 0:
        list1 = [
            {"Заметок с указанной датой нет в спиcке!": "The requested date is missing!"}
        ]
    return list1

# 5
def add_note(note_book, user_data):
    fields1 = ["ID", "Заголовок", "Дата", "Заметка"]
    data = user_data.replace("_", ";", 3).split(";")
    result = dict(zip(fields1, data))
    print(result)
    note_book.append(result)


# 6
def change_note(note_book, title, new_note):
    list_of_notes = find_by_title(note_book, title)
    # print(list_of_notes)
    if len(list_of_notes) > 1:
        print(
            f"С данным заголовкам найдено {len(list_of_notes)} заметок.\nУкажите порядковый номер заметки для редактирования, в диапазоне от 1 до {len(list_of_notes)}."
        )
        showAll(list_of_notes)
        n = int(input())
        ind = note_book.index(list_of_notes[n - 1])
    else:
        ind = note_book.index(list_of_notes[0])
    note_book[ind]["Заметка"] = new_note
    return note_book[ind]


# 7
def delete_by_ID(note_book, ID):
    list_of_notes = find_by_ID(note_book, ID)
    ind = note_book.index(list_of_notes[0])
    print(ind)
    return note_book.pop(ind)


# 8
def write_txt(filename, note_book):

    with open(filename, "w", encoding="utf-8") as nbout:
        for i in range(len(note_book)):


            s = ""
            for v in note_book[i].values():
                s += v + ";"
            if len(s) > 5:
                nbout.write(
                    f"{s[:-1]}" + "\n"
                ) 

