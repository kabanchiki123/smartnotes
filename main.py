from PyQt6.QtWidgets import *

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


window.setLayout(main_line)
window.show()
app.exec()