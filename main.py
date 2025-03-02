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
main_line.addLayout(v1)

def show_note():
    key = notatku_list.currentItem().text()
    pole.setText(notes[key]["текст"])
    tags_list.clear
    tags_list.addItems(notes[key]["текст"])

notatku_list.itemClicked.connect(show_note)



window.setLayout(main_line)
window.show()
app.exec()