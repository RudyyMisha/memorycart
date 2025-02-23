from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

# 1) створюємо вікно
window = QWidget()
window.resize(600, 500)

# 2) створюємо віджети, які треба буде розмістити
btn_Menu = QPushButton("Меню")
btn_Sleep = QPushButton("Відпочити")
btn_OK = QPushButton("Відповісти")
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
lb_Question = QLabel("")

# 3) Панель з варіантами відповідей
RadioGroup = QButtonGroup() # для групування наших радіокнопок

rbtn_1 = QRadioButton("")
rbtn_2 = QRadioButton("")
rbtn_3 = QRadioButton("")
rbtn_4 = QRadioButton("")

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Розміщуємо варіанти відповідей у 2 стовпчики всередині коробки кнопок 
RadioGroupBox = QGroupBox("Варіанти відповідей")

# кріпимо перші 2 кнопки на першу вертикальну лінію
line_ans1 = QVBoxLayout()
line_ans1.addWidget(rbtn_1)
line_ans1.addWidget(rbtn_2)

# кріпимо останні 2 кнопки на другу вертикальну лінію
line_ans2 = QVBoxLayout()
line_ans2.addWidget(rbtn_3)
line_ans2.addWidget(rbtn_4)

# розміщуємо наші 2 вертикальні лінії на горизонтальній
line_ans_main = QHBoxLayout()
line_ans_main.addLayout(line_ans1)
line_ans_main.addLayout(line_ans2)

# вставляємо горизонтальну лінію з варіантами відповідей в коробку для кнопок
RadioGroupBox.setLayout(line_ans_main)

# 4) Панель з результатом
AnsGroupBox = QGroupBox("Результати тесту")
lb_Result = QLabel("")
lb_Correct = QLabel("")

# розміщуємо результат
line_result = QVBoxLayout()
line_result.addWidget(lb_Result)    
line_result.addWidget(lb_Correct)  
AnsGroupBox.setLayout(line_result)  
AnsGroupBox.hide()

# 5) розмістити всі віджети у вікні (зробимо наступного разу)
first_hor_line = QHBoxLayout()
first_hor_line.addWidget(btn_Menu)
first_hor_line.addStretch(1)
first_hor_line.addWidget(btn_Sleep)
first_hor_line.addWidget(box_Minutes)

second_hor_line = QHBoxLayout()
second_hor_line.addWidget(lb_Question)

third_hor_line = QHBoxLayout()
third_hor_line.addWidget(RadioGroupBox)
third_hor_line.addWidget(AnsGroupBox)

fourth_hor_line = QHBoxLayout()
fourth_hor_line.addWidget(btn_OK, stretch=2)

# тепер створені 4 палки розмістимо одну під одною
main_line = QVBoxLayout()
main_line.addLayout(first_hor_line)
main_line.addLayout(second_hor_line)
main_line.addLayout(third_hor_line)
main_line.addLayout(fourth_hor_line)
main_line.addSpacing(5)

window.setLayout(main_line)

window.show()

