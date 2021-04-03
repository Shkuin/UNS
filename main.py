from PySide2 import QtCore, QtGui, QtWidgets
import sys
from ui import Ui_Form
import openpyxl







class Window(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.browse_folder)
        self.pushButton.clicked.connect(self.lt)



    def browse_folder(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        self.path = filename[0]
        self.label_9.setText(f'Таблица: {self.path}')
        

    def lt(self):
        self.wb = openpyxl.load_workbook(self.path) 
        self.lst_name  = self.lineEdit_2.text()
        self.new_column = self.lineEdit.text()
        self.column_search = self.lineEdit_3.text()
        self.column_value_1 = self.lineEdit_4.text()
        self.column_value_2 = self.lineEdit_5.text()
        self.row_start = int(self.lineEdit_6.text())
        self.row_end = int(self.lineEdit_7.text())
        self.l1 = []
        self.l2 = []
        self.data = []
        self.l3 = []
        self.l4 = []
        sheet = self.wb[self.lst_name]
        for i in sheet[self.column_search][self.row_start-1: self.row_end+1]:
            if i.value!=None:
                if sheet[self.column_value_1][i.row-1].value!=None or sheet[self.column_value_2][i.row-1].value!=None:
                    self.l1.append(i.value)


        for x in self.l1:
            if self.l1.count(x)>1:
                self.l2.append(x)

        self.l2 = list(set(self.l2))


        for i in self.l2:
            data_dict = {}
            for x in sheet[self.column_search][self.row_start-1: self.row_end+1]:
                if x.value == 0:
                    continue
            
                else:
                    if str(i) == str(x.value):
                        data_dict[x.row] = x.value

            self.data.append(data_dict)

        for i in self.data:
            i_value = 0
            j_value = 0
            l_help = []
            for k in i:
            
                if sheet[self.column_value_1][k-1].value==None:
                    i_value += 0

                else:
                    i_value += sheet[self.column_value_1][k-1].value

                if sheet[self.column_value_2][k-1].value==None:
                    j_value += 0

                else:
                    j_value += sheet[self.column_value_2][k-1].value

                l_help.append(k)
                if len(l_help)>1:
                    edit = min(l_help)
                    delete = max(l_help) 


            self.l4.append([i_value, j_value, i[k], edit, delete])




        sheet[self.new_column][0].value = 'РЕЗУЛЬТАТ'
        for x in self.l4:

            sheet[self.column_value_1][x[3]-1].value = x[0] 
            sheet[self.column_value_2][x[3]-1].value = x[1]
            sheet[self.new_column][x[3]-1].value = x[1]*x[0]
            sheet[self.column_value_1][x[4]-1].value = ''
            sheet[self.column_value_2][x[4]-1].value = ''
            sheet[self.column_search][x[4]-1].value = ''
            self.wb.save(self.path)
        

    



app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
window = Window()  # Создаём объект класса ExampleApp
window.show()  # Показываем окно
sys.exit(app.exec_()) # и запускаем приложение

def print(self):
    decoratis = 123 
    dwj = str(input('Enter the c: '))