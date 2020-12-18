from .BaseModel import *

class BorrowModel(BaseModel):
	"""docstring for BorrowModel"""
	def __init__(self):
		super().__init__()
		self.table_head = ["id_peminjam", "id_buku", "id_students", "id_staff","tanggal_pinjam"]
		self.table_name = 'borrow'

	def studentCheck(self, id_students):
		query = f'SELECT * FROM students WHERE id={id_students}'
		try:
			return self.database.fetchall(query)[0][0]
		except Exception as e:
			return False

