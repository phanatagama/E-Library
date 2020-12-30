from datetime import datetime
from .BaseView import *

class ReturnBookView(BaseView):
	"""docstring for BorrowView"""
	def getDataPeminjam(self):
		id_students = input('[+] Masukkan id Mahasiswa yang Meminjam > ')
		return id_students

	def detail(self, tanggal_pinjam, tanggal_kembali,denda):
		print(f"""[+] Tanggal Pinjam {tanggal_pinjam}
[+] Tanggal Kembali : {tanggal_kembali}
[+] Total Denda : {denda}""")

	# def insertData(self):
	# 	id_book = input('[+] Masukkan ID Buku > ')
	# 	id_students = input('[+] Masukkan ID Mahasiswa > ')
	# 	id_staff = input('[+] Masukkan ID Staff) > ')
	# 	now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	# 	return id_book,id_students,id_staff,now
