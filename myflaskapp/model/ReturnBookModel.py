from .BaseModel import *
from datetime import datetime

class ReturnBookModel(BaseModel):
	"""docstring for ReturnBookModel"""
	def __init__(self):
		super().__init__()
		self.table_head = ["id_kembali", "id_borrow", "tanggal_kembali", "denda"]
		self.table_name = 'returnbook'

	def calculate(self,id_students):
		query = f'SELECT tanggal_pinjam FROM borrow WHERE id_students={id_students}'
		tanggal_pinjam = self.database.fetchall(query)[0][0]
		denda = 0
		keterlambatan = self.today() - tanggal_pinjam
		if keterlambatan.days > 3:
			denda = 2000*(keterlambatan.days-3)
		return tanggal_pinjam, self.today(), denda

	def today(self):
		return datetime.now().date()