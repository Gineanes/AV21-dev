from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from ModuloCadastro import inserir
from ModuloData import converterData

class TelaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        carregador = QUiLoader()
        self.tela = carregador.load("Tela.ui")
        self.componentes()
    
    def componentes(self):
        self.comboBox = self.tela.findChild(QtWidgets.QComboBox, "comboBox")
        self.lineEdit = self.tela.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.lineEdit_2 = self.tela.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        self.comboBox_2 = self.tela.findChild(QtWidgets.QComboBox, "comboBox_2")
        self.dateEdit = self.tela.findChild(QtWidgets.QDateEdit, "dateEdit")
        self.pushButton = self.tela.findChild(QtWidgets.QPushButton,"pushButton")
        self.pushButton.clicked.connect(self.cadastrarProducao)

    def cadastrarProducao(self):
        tpmf = self.comboBox.currentText()
        dc = self.lineEdit.text()
        val = self.lineEdit_2.text()
        cat = self.comboBox_2.currentText()
        dat = self.dateEdit.text()
        inserir(tpmf, dc, val, cat, converterData(dat))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    interface = TelaPrincipal()
    interface.tela.showMaximized()
    app.exec()