from PyQt6.QtWidgets import *
from file_helper import *

notes = read_from_file()
write_in_file(notes)

app = QApplication([])
window = QWidget()

pole = QTextEdit()
notes_list_lbl = QLabel("Cписок заміток")
notatku_list = QListWidget()
add_note_btn = QPushButton("Додати замітку")
delete_note_btn = QPushButton("Видалити")
save_note_btn = QPushButton("Зберегти")
search_tag_btn = QPushButton("Шукати тег по замітці")
add_tag_btn = QPushButton("Додати тег")
delete_tag_btn = QPushButton("Видалити")
tag_list_lbl = QLabel("Cписок заміток")
tags_list = QListWidget()
tag_input = QLineEdit()
main_line = QHBoxLayout()
main_line.addWidget(pole)

notatku_list.addItems(notes)

v1 = QVBoxLayout()
v1.addWidget(notes_list_lbl)
v1.addWidget(notatku_list)
v1.addWidget(save_note_btn)
v1.addWidget(delete_note_btn)
v1.addWidget(add_note_btn)
v1.addWidget(tag_list_lbl)
v1.addWidget(tags_list)
v1.addWidget(tag_input)
v1.addWidget(search_tag_btn)
v1.addWidget(add_tag_btn)
v1.addWidget(delete_tag_btn)
main_line.addLayout(v1)

def show_note():
    key = notatku_list.currentItem().text()
    text_status = len (pole.toPlainText())
    if text_status >= 1:
        pole.setText(notes[key]["текст"])
        tags_list.clear()
        tags_list.addItems(notes[key]["теги"])
    else:
        notes[key]["текст"] = "Немає тексту"
        pole.setText(notes[key]["текст"])
        tags_list.clear()
        tags_list.addItems(notes[key]["теги"])


notatku_list.itemClicked.connect(show_note)

def add_note():
    note_name, ok = QInputDialog.getText(window, "Нова нотатка", "Введіть нову нотатку")
    if ok == True:
        notes[note_name] = {
            "текст": "",
            "теги": [

            ]
        }
        notatku_list.clear
        notatku_list.addItems(notes)
        write_in_file(notes)

add_note_btn.clicked.connect(add_note)
notatku_list.itemClicked.connect(show_note)

def save_note_func():
    text = pole.toPlainText()
    note_key = notatku_list.currentItem().text()
    notes[note_key]["текст"] = text
    write_in_file(notes)

save_note_btn.clicked.connect(save_note_func)

def delete_note_func():
    key = notatku_list.currentItem().text()
    notes.pop(key)
    notatku_list.clear()
    notatku_list.addItems(notes)
    write_in_file(notes)
delete_note_btn.clicked.connect(delete_note_func)


def add_tag_func():
    tag_name, ok = QInputDialog.getText(window, "Новий тег", "Введіть новий тег")
    if ok == True:
        notes[tag_name] = {
            "текст": "",
            "теги": [

            ]
        }
        tags_list.clear
        tags_list.addItems(notes)
        write_in_file(notes)
add_tag_btn.clicked.connect(add_tag_func)


window.setLayout(main_line)
window.show()
app.exec()