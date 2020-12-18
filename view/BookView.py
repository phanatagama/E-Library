from .BaseView import * 

class BookView(BaseView):

	def insertData(self):
		judul = input('[+] Masukkan Judul Buku > ')
		pengarang = input('[+] Masukkan Pengarang Buku > ')
		penerbit = input('[+] Masukkan Penerbit Buku > ')
		tahun = int(input('[+] Masukkan Tahun Buku > '))
		return judul,pengarang,penerbit,tahun

	def updateData(self):
		id_book = int(input('[+] Masukkan id buku yang ingin diubah > '))	
		judul,pengarang,penerbit,tahun = self.insertData()
		return id_book,judul,pengarang,penerbit,tahun

	def deleteData(self):
		id_buku = int(input('[+] Masukkan id buku yang ingin dihapus > '))
		return id_buku

	def searchData(self):
		judul = input('[+] Masukkan Judul Buku > ')
		return judul