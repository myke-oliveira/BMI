
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
			QMessageBox.question(self, 'Value Error', 'Not valid height', QMessageBox.Ok, QMessageBox.Ok)
			return
		try:
			weight = float(self.edtWeight.text())
		except ValueError as e:
			QMessageBox.question(self, 'Value Error', 'Not valid weight', QMessageBox.Ok, QMessageBox.Ok)
			return
		bmi = weight / height ** 2
		self.lblBMI.setText(f'{bmi:5.4}')
		if bmi < 18.5:
			desc = 'Underweight'
		elif bmi < 25:
			desc = 'Normal weight'
		elif bmi < 30:
			desc = 'Over weight'
		elif bmi < 35:
			desc = 'Obese class 1'
		elif bmi < 40:
			desc = 'Obese class 2'
		else:
			desc = 'Obese class 3'
		self.lblDescription.setText(desc)
		


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec())