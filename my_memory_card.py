#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox
from random import shuffle, randint
from math import floor

class Question():
    def __init__(self, question_text, right_answer, wrong1, wrong2, wrong3):
        self.question_text = question_text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
win = QWidget()
win.setWindowTitle('Memory card')
win.resize(600, 400)

def next_question():
    win.cur_question = randint(0, len(questions_list)-1)
    ask(questions_list[win.cur_question])
    win.total += 1
    print('Статистика')
    print('Всего вопросов:', win.total)
    print('Правильных ответов:', win.score)

def show_result():
    radio_group.hide()
    ans_group.show()
    ans_button.setText('Следующий вопрос')

def show_question():
    ans_group.hide()
    radio_group.show()
    ans_button.setText('Ответить')
    RadioAnsGroup.setExclusive(False)
    qrb1.setChecked(False)
    qrb2.setChecked(False)
    qrb3.setChecked(False)
    qrb4.setChecked(False)
    RadioAnsGroup.setExclusive(True)

def click_ok():
    if ans_button.text() == 'Ответить':
        check_answer()
    elif ans_button.text() == 'Следующий вопрос':
        next_question()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question_text)
    l2.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        show_result()
        win.score += 1
    else:
        show_correct('Неправильно')
        show_result()
    print('Статистика')
    print('Всего вопросов:', win.total)
    print('Правильных ответов:', win.score)
    print('Рейтинг:', floor(win.score/win.total*100), '%')
def show_correct(res):
    l1.setText(res)

question = QLabel('Какой  национальности не существует?')
ans_button = QPushButton('Ответить')

radio_group = QGroupBox('Варианты ответов')
qrb1 = QRadioButton('Энцы')
qrb2 = QRadioButton('Чулымцы')
qrb3 = QRadioButton('Смурфы')
qrb4 = QRadioButton('Алеуты')
v1 = QVBoxLayout()
v2 = QVBoxLayout()
v1.addWidget(qrb1)
v1.addWidget(qrb3)
v2.addWidget(qrb2)
v2.addWidget(qrb4)
main_h = QHBoxLayout()
main_h.addLayout(v1)
main_h.addLayout(v2)
radio_group.setLayout(main_h)
RadioAnsGroup = QButtonGroup()
RadioAnsGroup.addButton(qrb1)
RadioAnsGroup.addButton(qrb2)
RadioAnsGroup.addButton(qrb3)
RadioAnsGroup.addButton(qrb4)
answers = [qrb1, qrb2, qrb3, qrb4]

ans_group = QGroupBox('Результаты текста')
l1 = QLabel('Правильно/Неправильно')
l2 = QLabel('Правильный ответ')
v3 = QVBoxLayout()
v3.addWidget(l1)
v3.addWidget(l2, alignment = Qt.AlignCenter)
ans_group.setLayout(v3)
ans_group.hide()

h2 = QVBoxLayout()
h2.addWidget(question, alignment = Qt.AlignCenter)
h2.addWidget(radio_group)
h2.addWidget(ans_group)
h2.addWidget(ans_button)
win.setLayout(h2)


questions_list = list()
win.cur_question = -1
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Где находится Нидерланды?', 'Европа', 'Азия', 'Африка', 'Антарктида'))
questions_list.append(Question('Столица Англии', 'Лондон', 'Люксембург', 'Вена', 'Албания'))
questions_list.append(Question('Столица Бразилии', 'Бразилиа', 'Рио-де-Жанейро', 'Свердловск', 'Шри-Ланка'))
questions_list.append(Question('Город с населением более 5 млн. человек', 'Москва', 'Иркутск', 'Нижний новгород', 'Волгоград'))
questions_list.append(Question('Город который не находится на территории Беларуси', 'Вильнюс', 'Гомель', 'Пинск', 'Витебск'))
questions_list.append(Question('С какой из этих стран Россия не имеет сухопутной границы', 'Литва', 'Латвия', 'Эстония', 'Швеция'))
questions_list.append(Question('Площадь Люксембурга', '2 586 км²', '4 574 км²', '8 335 км²', '2 587 км²'))
questions_list.append(Question('Столица Люксембурга', 'Люксембург', 'Андорра', 'Афины', 'Нью-Йорк'))
questions_list.append(Question('Столица Беларуси', 'Минск', 'Гомель', 'Пинск', 'Рига'))
questions_list.append(Question('Столица Китая', 'Пекин', 'Шанхай', 'Токио', 'Сеул'))


ans_button.clicked.connect(click_ok)

win.score = 0
win.total = 0
next_question()

win.show()
app.exec_()
