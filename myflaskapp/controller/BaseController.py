class BaseController:

	def response(self,result):
		if result == 1:
			self.View.succes(result)
		else:
			self.View.failure()

	def insertData(self):
		detailData = self.View.insertData()
		result = self.Model.insertData(detailData)
		self.response(result)
		
	def getData(self):
		table_head = self.Model.table_head
		table_body = self.Model.getData()
		self.View.showData(table_head, table_body)

	def deleteData(self):
		id_data = self.View.deleteData()
		result = self.Model.deleteData(id_data)
		self.response(result)

	def updateData(self):
		detailData = self.View.updateData()
		result = self.Model.updateData(detailData)
		self.response(result)

	def searchData(self):
		detailData = self.View.searchData()
		table_head = self.Model.table_head
		table_body = self.Model.searchData(detailData)
		self.View.showData(table_head, table_body)