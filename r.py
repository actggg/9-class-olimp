from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import sys
from PyQt5.QtWidgets import QFileDialog, QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5 import uic, QtWidgets



method_class = {'Method_1': '-',
            'Method_2': '-',
            'Method_3': '-',
            'Method_4': '-'}




try:
    class MainWidget(QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('untitled.ui', self)
            self.text_button.clicked.connect(self.count)
            self.link_button.clicked.connect(self.count)
            self.file_button.clicked.connect(self.file)
            self.method_class = {'link': '-',
                            'Method_1': '-',
                            'Method_2': '-',
                            'Method_3': '-',
                            'Method_4': '-'}
            print(self.file_input.text())
        def file(self):
            print(self.file_input.text())
            with open(self.file_input.text(), 'r', encoding='utf8') as f:
                k = f.read().split()
                print(k)
                s = []
                for i in k:
                    print(i)
                    method_class = {'link': i,
                            'Method_1': '-',
                            'Method_2': '-',
                            'Method_3': '-',
                            'Method_4': '-'}
                    s.append(method_class)
                print(s)
                self.table = Table(s)
                self.table.show()


        def count(self):
            self.table = Table(self.method_class)
            self.table.show()


    class Table(QMainWindow):
        # Override class constructor
        def __init__(self, metods):
            # You must call the super class method
            QMainWindow.__init__(self)

            self.setMinimumSize(QSize(600, 200))  # Set sizes
            self.setWindowTitle("Работа с QTableWidget")  # Set the window title
            central_widget = QWidget(self)  # Create a central widget
            self.setCentralWidget(central_widget)  # Install the central widget

            grid_layout = QGridLayout(self)  # Create QGridLayout
            central_widget.setLayout(grid_layout)  # Set this layout in central widget

            table = QTableWidget(self)  # Create a table
            table.setColumnCount(5)  # Set three columns
            table.setRowCount(len(metods))  # and one row

            # Set the table headers
            table.setHorizontalHeaderLabels(["link", "Method 1", "Method 2", "Method 3", 'Method 4'])

            # Set the tooltips to headings
            table.horizontalHeaderItem(1).setToolTip("Column 1 ")
            table.horizontalHeaderItem(2).setToolTip("Column 2 ")
            table.horizontalHeaderItem(3).setToolTip("Column 3 ")
            table.horizontalHeaderItem(4).setToolTip("Column 4 ")

            # Set the alignment to the headers
            table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
            table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
            table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
            for i in range(len(metods)):
                table.setItem(i, 0, QTableWidgetItem(metods[i]['link']))
                table.setItem(i, 1, QTableWidgetItem(metods[i]['Method_1']))
                table.setItem(i, 2, QTableWidgetItem(metods[i]['Method_2']))
                table.setItem(i, 3, QTableWidgetItem(metods[i]['Method_3']))
                table.setItem(i, 4, QTableWidgetItem(metods[i]['Method_4']))

                '''
                table.setItem(0, 1, QTableWidgetItem("Text in column 1"))
                table.setItem(0, 2, QTableWidgetItem("Text in column 2"))
                table.setItem(0, 3, QTableWidgetItem("Text in column 3"))
                table.setItem(0, 4, QTableWidgetItem("Text in column 4"))
                table.setItem(1, 1, QTableWidgetItem("Text in column 1"))
                table.setItem(1, 2, QTableWidgetItem("Text in column 2"))
                table.setItem(1, 3, QTableWidgetItem("Text in column 3"))
                table.setItem(1, 4, QTableWidgetItem("Text in column 4"))
                '''

            # Do the resize of the columns by content
            table.resizeColumnsToContents()
            '''
            self.btn = QPushButton('Сохранить', self)
            self.btn.resize(150, 50)
            self.btn.move(100, 50)
            '''

            grid_layout.addWidget(table, 500, 200)  # Adding the table to the grid
except Exception as e:
    print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())