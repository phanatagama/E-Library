from .BaseController import *
from view.RiwayatView import *
from model.RiwayatModel import *

class RiwayatController(BaseController):
	def __init__(self):
		self.View = RiwayatView()
		self.Model = RiwayatModel()

	def main(self):
		self.getData()
