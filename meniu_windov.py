from PyQt5.QtWidgets import*

#вікно меню
menu_window = QWidget()

# текстові віджети
lb_question = QLabel("Введіть запитання")
lb_right_answer = QLabel("Введіть правильну відповідь")
lb_wrong_answer1 = QLabel("Введіть першу неправильну відповідь")
lb_wrong_answer2 = QLabel("Введіть другу неправильну відповідь")
lb_wrong_answer3 = QLabel("Введіть третю неправильну відповідь")

# віджети, в які користувач буде вписувати нові слова
le_question = QLineEdit()
le_right_answer = QLineEdit()
le_wrong_answer1 = QLineEdit()
le_wrong_answer2 = QLineEdit()
le_wrong_answer3 = QLineEdit()
lb_header_statistics = QLineEdit("СТАТИСТИКА")
lb_statistics = QLineEdit()

# віджети кнопки
btn_back = QPushButton("Назад")
btn_add_question = QPushButton("Додати питання")
btn_clear = QPushButton("Очистити")

# кріпимо на першу вертикальну палку текстові віджети
vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_question)
vl_labels.addWidget(lb_right_answer)
vl_labels.addWidget(lb_wrong_answer1)
vl_labels.addWidget(lb_wrong_answer2)
vl_labels.addWidget(lb_wrong_answer3)

# кріпимо на другу вертикальну палку віджети, в які користувач буде вписувати слова
vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_answer)
vl_lineEdits.addWidget(le_wrong_answer1)
vl_lineEdits.addWidget(le_wrong_answer2)
vl_lineEdits.addWidget(le_wrong_answer3)

# кріпимо на горизонтальній палці попередні дві вертикальні
hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_lineEdits)

# кріпимо дві кнопки на горизонтальну палку
hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_question)
hl_buttons.addWidget(btn_clear)

# створюємо основну вертикальну палку, на яку кріпимо все що створили
vl_main = QVBoxLayout()
vl_main.addLayout(hl_question)
vl_main.addLayout(hl_buttons)
vl_main.addWidget(lb_header_statistics)
vl_main.addWidget(lb_statistics)
vl_main.addWidget(btn_back)

# вставляємо основну вертикальну палку у вікно
menu_window.setLayout(vl_main)
menu_window.resize(400, 300)


