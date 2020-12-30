from .BaseView import * 

class StaffView(BaseView):
	def insertData(self):
		email = input("Masukkan Email: ")
		password = input("Masukkan Password: ")
		return email, password