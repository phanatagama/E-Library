from .BaseModel import *

class BooksModel(BaseModel):
	def __init__(self):
		super().__init__()
		self.table_head = ["id_buku", "judul", "pengarang", "penerbit", "tahun"]
		self.table_name = 'books'

	def updateData(self, data):
		query = f"UPDATE {self.table_name} SET {self.table_head[1]}='{data[1]}',{self.table_head[2]}='{data[2]}',{self.table_head[3]}='{data[3]}',{self.table_head[4]}='{data[4]}' WHERE id = {data[0]}"
		return self.database.execute(query)

	def searchData(self,judul):
		query = f"SELECT * FROM {self.table_name} WHERE {self.table_head[1]} LIKE '%{judul}%'"
		return self.database.fetchall(query)