from .BaseController import *
from view.BookView import *
from model.BooksModel import *

class BookController(BaseController):
	def __init__(self):
		self.View = BookView()
		self.Model = BooksModel()

	def updateData(self):
		detailData = self.View.updateData()
		BookCheck = self.Model.bookCheck(detailData[0])
		if BookCheck:
			result = self.Model.updateData(detailData)
			self.response(result)
		else:
			self.View.failure()

	def deleteData(self):
		id_data = self.View.deleteData()
		BookCheck = self.Model.bookCheck(id_data)
		if BookCheck:
			result = self.Model.deleteData(id_data)
			self.response(result)
		else:
			self.View.failure()

	def main(self, option):
		if option==0:
			exit()
		elif option == 1:
			self.getData()	
		elif option == 2:
			self.insertData()
		elif option == 3:
			self.deleteData()
		elif option == 4:
			self.updateData()
		elif option == 5:
			self.searchData()