
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('bmi.ui', self)
		self.btnCalculate.clicked.connect(self.onClick)

	def onClick(self):
		try:
			height = float(self.edtHeight.text())
		except ValueError as e:
			print('Not valid height.')
			return
		try:
			weight = float(self.edtWeight.text())
		except Exception as e:
			print('Not valid weight.')
		bmi = weight / height ** 2
		self.lblBMI.setText(str(bmi))
		


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec())