from .BaseController import *
from view.StaffView import *
from model.StaffModel import *

class StaffController(BaseController):
	def __init__(self):
		self.View = StaffView()
		self.Model = StaffModel()

	def login(self):
		detailData = self.View.insertData()
		Password = self.Model.getData(detailData[0])
		if Password == False:
			print('Email yang Anda Gunakan Salah')
			return self.login()
		else:
			if detailData[1] == Password:
				os.system('cls')
				return True
			else:
				print('Password yang Anda Masukkan Salah')
				return self.login()
			
		

