from PyQt5 import QtWidgets
from window import Ui_MainWindow
import sys
from conn import Func

con = Func()

class Interface(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.window.pushButton_2.clicked.connect(self.get_count)
        self.window.pushButton_3.clicked.connect(self.get_property)
        self.window.pushButton.clicked.connect(self.add_property)
        
    
    def get_count(self):
        count = con.func_get_num()
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('count of property')
        msg_box.setText(f'кол-во имуществ: {count}')
        msg_box.exec()

    def get_property(self):
        p_id = int(self.window.lineEdit_5.text())
        data = con.func_get_prop(p_id)
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle(f'data of property{p_id}')
        msg_box.setText(f'''
                        owner: {data[1]}
                        type: {data[2]}
                        zalog: {data[3]}
                        year: {data[4]}
                        gos_num: {data[5]}

''')
        msg_box.exec()

    def add_property(self):
        p_owner = self.window.lineEdit.text()
        p_type = self.window.lineEdit_2.text()
        p_year = int(self.window.lineEdit_3.text())
        p_gos_num = self.window.lineEdit_4.text()
        try:
            con.func_create_prop(p_owner, p_type, p_year, p_gos_num)
            print('property was created!')
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle('create property')
            msg_box.setText(f'property was created!')
            msg_box.exec()
        except Exception as e:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle('error')
            msg_box.setText(f'error: {e}')
            msg_box.exec()

    def _show_error_message(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle("Ошибка")
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Interface()
    myapp.show()
    sys.exit(app.exec())