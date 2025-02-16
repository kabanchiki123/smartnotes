from PyQt6.QtWidgets import*


app = QApplication([])

window = QWidget()



main_line = QHBoxLayout()


spusokzamitok_lbl = QLabel("Список заміток")

pole_txt = QTextEdit()
notes_list = QListWidget()
create_note_btn =QPushButton("Створити замітку")
delete_note_btn =QPushButton("Видалити замітку")

main_line.addWidget(pole_txt)

A1 = QVBoxLayout()
A1.addWidget(spusokzamitok_lbl)
A1.addWidget(notes_list)
A1.addWidget(create_note_btn)
A1.addWidget(delete_note_btn)

spusoktegiv_lbl = QLabel("Список тегів")
pole_txt2 = QTextEdit()
teg_list = QLineEdit()
add_to_note_btn = QPushButton("Додати до замітки")
open_from_note_btn = QPushButton("Відкріпити від замітки")
search_for_teg_note_btn = QPushButton("Шукати замітки до тегу")

main_line.addWidget(pole_txt2)
A1 = QVBoxLayout()
A1.addWidget(spusoktegiv_lbl)
A1.addWidget(teg_list)
A1.addWidget(add_to_note_btn)
A1.addWidget(open_from_note_btn)
A1.addWidget(search_for_teg_note_btn)

window.setLayout(main_line)
main_line.addLayout(A1)


window.show()
app.exec()
