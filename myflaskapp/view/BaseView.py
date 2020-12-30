from prettytable import PrettyTable

class BaseView:
	def menu(self):
		option = int(input("""
Selamat Datang Di Sistem Administrasi Perpustakaan Universitas
Layanan yang tersedia:
[1] Tampilkan Buku
[2] Tambah Buku
[3] Hapus Buku
[4] Ubah Buku
[5] Cari Buku
[6] Peminjaman
[7] Pengembalian
[8] Riwayat Peminjaman
[0] exit
[+] Masukkan Pilihan > """))
		return option

	def showData(self, table_head, data):
		table = PrettyTable()
		table.field_names = table_head
		for row in data:
			table.add_row(list(row))
		print(table)

	def succes(self, data):
		print(f"[*] {data} Berhasil melakukan perubahan.")

	def failure(self):
		print("[!] Gagal, periksa kembali data yang anda masukkan.")
