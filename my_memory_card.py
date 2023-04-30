from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import * 

app = QApplication([])
main_win = QWidget()
main_win.resize(500, 300)


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question() 

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')

    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

    lb1.setText(q.question)
    lb2.setText(q.right_answer) 
    show_question() 

def show_correct(otv):
    lb2.setText(otv)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Не верно!')
            print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
    
def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
    num = randint(0, len(questions_list) - 1)
    q = questions_list[num]
    ask(q) 

main_win.score = 0
main_win.total = 0

questions_list = [] 
questions_list.append(Question('Вопрос 1', 'Правильный ответ', 'Не правильный', 'Не правильный', 'Не правильный'))
questions_list.append(Question('Вопрос 2', 'Правильный ответ', 'Не правильный', 'Не правильный', 'Не правильный'))
questions_list.append(Question('Вопрос 3', 'Правильный ответ', 'Не правильный', 'Не правильный', 'Не правильный'))

button = QPushButton('Ответить') 
lb1 = QLabel('Текст вопроса') 

RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
RadioGroupBox.setLayout(layout_ans1) 

AnsGroupBox = QGroupBox("Результат теста")
lb1 = QLabel('Верно\не верно')
lb2 = QLabel('Ответ') 

layout_res = QVBoxLayout()
layout_res.addWidget(lb1)
layout_res.addWidget(lb2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 

layout_line1.addWidget(lb1)
layout_line2.addWidget(AnsGroupBox)  
layout_line2.addWidget(RadioGroupBox)   
AnsGroupBox.hide() 

layout_line3.addWidget(button) 
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

main_win.setLayout(layout_card)

button.clicked.connect(click_OK) 
next_question()

main_win.show()
app.exec()
