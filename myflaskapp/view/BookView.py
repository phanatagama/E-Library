from .BaseView import * 

class BookView(BaseView):

	def insertData(self):
		judul = input('[+] Masukkan Judul Buku > ')
		pengarang = input('[+] Masukkan Pengarang Buku > ')
		penerbit = input('[+] Masukkan Penerbit Buku > ')
		tahun = int(input('[+] Masukkan Tahun Buku > '))
		rak = int(input('[+] Masukkan Rak Buku >'))
		return judul,pengarang,penerbit,tahun,rak

	def updateData(self):
		id_book = int(input('[+] Masukkan id buku yang ingin diubah > '))	
		judul,pengarang,penerbit,tahun,rak = self.insertData()
		return id_book,judul,pengarang,penerbit,tahun,rak

	def deleteData(self):
		id_buku = int(input('[+] Masukkan id buku yang ingin dihapus > '))
		return id_buku

	def searchData(self):
		judul = input('[+] Masukkan Judul Buku > ')
		return judul