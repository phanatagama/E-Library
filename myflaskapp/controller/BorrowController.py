from .BaseController import *
from view.BorrowView import *
from model.BorrowModel import *

class BorrowController(BaseController):
	def __init__(self):
		self.View = BorrowView()
		self.Model = BorrowModel()

	def deleteData(self,id_data):
		result = self.Model.deleteData(id_data)
		self.response(result)

	def insertData(self):
		detailData = self.View.insertData()
		BorrowCheck = self.Model.checker(detailData[1])
		StudentCheck = self.Model.studentCheck(detailData[1])
		BookCheck = self.Model.bookCheck(detailData[0])
		if BorrowCheck or not StudentCheck or not BookCheck:
			self.View.failure()
		else:
			result = self.Model.insertData(detailData)
			self.response(result)

	def main(self):
		self.getData()
		self.insertData()
