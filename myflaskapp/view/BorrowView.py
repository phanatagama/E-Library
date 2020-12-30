from datetime import datetime
from .BaseView import *

class BorrowView(BaseView):
	"""docstring for BorrowView"""
	def insertData(self):
		id_book = input('[+] Masukkan ID Buku > ')
		id_students = input('[+] Masukkan ID Mahasiswa > ')
		id_staff = '1'
		now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		return id_book,id_students,id_staff,now