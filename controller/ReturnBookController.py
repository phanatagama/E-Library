from .BorrowController import *
# from .BaseController import *
from view.ReturnBookView import *
from model.ReturnBookModel import *


class ReturnBookController(BaseController):
	def __init__(self):
		self.View = ReturnBookView()
		self.Model = ReturnBookModel()

	def returnbook(self):
		BorrowController().getData()
		id_peminjaman = self.View.getDataPeminjam()
		check = self.Model.checker(id_peminjaman)
		if check:
			tanggal_pinjam, today, denda = self.Model.calculate(id_peminjaman)
			self.View.detail(tanggal_pinjam, today, denda)
			BorrowController().deleteData(check)
			# self.insertData(check,today,denda)
		else:
			self.View.failure()

	def insertData(self, *data):
		self.Model.insertData(data)

	def main(self):
		self.returnbook()
		# self.insertData()
