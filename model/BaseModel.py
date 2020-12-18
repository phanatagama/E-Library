from core.Database import *

class BaseModel:
	"""docstring for BaseModel"""
	def __init__(self):
		self.database = Database()

	def insertData(self, data):
		query = f"""INSERT INTO {self.table_name} {str(tuple(self.table_head[1:])).replace("'","")} VALUES {data};"""
		return self.database.execute(query)
		
	def deleteData(self, id_item):
		query = f"DELETE FROM {self.table_name} WHERE id={id_item}"
		return self.database.execute(query)

	def getData(self):
		query = f'SELECT * FROM {self.table_name}'
		return self.database.fetchall(query)

	def checker(self, id_students):
		query = f'SELECT * FROM borrow WHERE id_students={id_students}'
		try:
			return self.database.fetchall(query)[0][0]
		except Exception as e:
			return False

	def bookCheck(self, id_book):
		query = f'SELECT * FROM books WHERE id={id_book}'
		try:
			return self.database.fetchall(query)[0][0]
		except Exception as e:
			return False