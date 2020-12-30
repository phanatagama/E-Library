from .BaseModel import *

class RiwayatModel(BaseModel):
	def __init__(self):
		super().__init__()
		self.table_head = ["id", "judul buku", "student", "staff","tanggal pinjam"]
		self.table_name = 'riwayatpeminjaman'

	def getData(self):
		query = f'SELECT r.id, b.judul, s.nama, st.nama, r.tanggal_pinjam FROM books b, students s, staff st, riwayatpeminjaman r WHERE (b.id = r.id_buku) and (s.id = r.id_student) and (st.id = r.id_staff) ORDER BY r.id'
		return self.database.fetchall(query)