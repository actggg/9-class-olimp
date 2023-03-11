import re  # Регулярные выражения.
import sys
from statistics import mode
from urllib.request import urlopen
import nltk
import requests  # Загрузка новостей с сайта.
from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QTableWidget, QTableWidgetItem
from bs4 import BeautifulSoup

from prediction import pred


def know_text_in_link(link):
    resp = requests.get(link)
    if 300 > resp.status_code >= 200:
        html = urlopen(link).read()
        soup = BeautifulSoup(html, features="html.parser")
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out
        # get text
        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text
    return f'Ошибка программы {resp.status_code}'


classes = ['business', 'entertainment', 'politics', 'medical', 'graphics', 'historical', 'food', 'space', 'sport',
           'technologie']


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.setWindowTitle("Классификатор по тематикам")
        self.text_button.clicked.connect(self.text_helper)
        self.link_button.clicked.connect(self.link_helper)
        self.file_button.clicked.connect(self.file_helper)
        nltk.download("stopwords")  # поддерживает удаление стоп-слов
        nltk.download('punkt')  # делит текст на список предложений
        nltk.download('wordnet')  # проводит лемматизацию
        nltk.download('omw-1.4')

    def file_helper(self):
        with open(self.file_input.text(), 'r', encoding='utf8') as f:
            k = f.read().split()
            r = 0
            s = []
            for i in k:
                r += 1
                print(f'Обрабатывает ссылку номер {r}')
                if know_text_in_link(i) != 0:
                    rist = [classes[pred([str(know_text_in_link(i))])[0]],
                            classes[pred([str(know_text_in_link(i))])[1]],
                            classes[pred([str(know_text_in_link(i))])[2]]]
                    if rist.count(mode(rist)) != 1:
                        t = mode(rist)
                    else:
                        t = '-'
                    method_class = {'link': i,
                                    'Method_1': classes[pred([str(know_text_in_link(i))])[0]],
                                    'Method_2': classes[pred([str(know_text_in_link(i))])[1]],
                                    'Method_3': classes[pred([str(know_text_in_link(i))])[2]],
                                    'sum': t}
                    s.append(method_class)
            self.table = Table(s)
            self.table.show()

    def link_helper(self):
        s = []
        rist = [classes[pred([str(know_text_in_link(self.link_input.text()))])[0]],
                classes[pred([str(know_text_in_link(self.link_input.text()))])[1]],
                classes[pred([str(know_text_in_link(self.link_input.text()))])[2]]]
        if rist.count(mode(rist)) != 1:
            t = mode(rist)
        else:
            t = '-'
        method_class = {'link': self.link_input.text(),
                        'Method_1': classes[pred([str(know_text_in_link(self.link_input.text()))])[0]],
                        'Method_2': classes[pred([str(know_text_in_link(self.link_input.text()))])[1]],
                        'Method_3': classes[pred([str(know_text_in_link(self.link_input.text()))])[2]],
                        'sum': t}
        s.append(method_class)
        self.table = Table(s)
        self.table.show()

    def text_helper(self):
        p = pred([str(self.text_input.toPlainText())])[0]
        p2 = pred([str(self.text_input.toPlainText())])[1]
        p3 = pred([str(self.text_input.toPlainText())])[2]
        rist = [p,
                p2,
                p3]
        if rist.count(mode(rist)) > 1:
            t = classes[mode(rist)]
        else:
            t = '-'
        method_class = {'link': self.text_input.toPlainText(),
                        'Method_1': classes[p],
                        'Method_2': classes[p2],
                        'Method_3': classes[p3],
                        'sum': str(t)
                        }
        self.table = Table([method_class])
        self.table.show()


class Table(QMainWindow):
    # Override class constructor
    def __init__(self, metods):
        # You must call the super class method
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(650, 100 + len(metods) * 50))  # Set sizes
        self.setWindowTitle("Результаты с классификацией")  # Set the window title
        central_widget = QWidget(self)  # Create a central widget
        self.setCentralWidget(central_widget)  # Install the central widget

        grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(grid_layout)  # Set this layout in central widget

        table = QTableWidget(self)  # Create a table
        table.setColumnCount(5)  # Set three columns
        table.setRowCount(len(metods))  # and one row

        # Set the table headers
        table.setHorizontalHeaderLabels(["Адрес/текст", "GaussianNB", "SVM", "LogReg", 'Итого:'])

        # Set the tooltips to headings
        table.horizontalHeaderItem(1).setToolTip("Column 1 ")
        table.horizontalHeaderItem(2).setToolTip("Column 2 ")
        table.horizontalHeaderItem(3).setToolTip("Column 3 ")
        table.horizontalHeaderItem(4).setToolTip("sum")

        # Set the alignment to the headers
        for i in range(len(metods)):
            table.setItem(i, 0, QTableWidgetItem(metods[i]['link']))
            table.setItem(i, 1, QTableWidgetItem(metods[i]['Method_1']))
            table.setItem(i, 2, QTableWidgetItem(metods[i]['Method_2']))
            table.setItem(i, 3, QTableWidgetItem(metods[i]['Method_3']))
            table.setItem(i, 4, QTableWidgetItem(metods[i]['sum']))


        table.resizeColumnsToContents()
        self.btn = QPushButton('Сохранить результат', self)
        self.btn.resize(150, 50)
        self.btn.move(500, 10)
        grid_layout.addWidget(table, 650, 100 + len(metods) * 50)  # Adding the table to the grid


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
