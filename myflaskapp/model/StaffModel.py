from .BaseModel import *

class StaffModel(BaseModel):
	def __init__(self):
		super().__init__()
		self.table_head = ["id", "nama", "nip", "email", "contact", "alamat","pass"]
		self.table_name = 'staff'

	def getData(self, email):
		query = f"SELECT pass FROM {self.table_name} WHERE {self.table_head[3]}='{email}'"
		try:
			return self.database.fetchall(query)[0][0]
		except Exception as e:
			return False