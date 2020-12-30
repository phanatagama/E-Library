from controller.BookController import *
from controller.BorrowController import *
from controller.ReturnBookController import *
from controller.RiwayatController import *
from view.BaseView import *
from core.Database import *
import os

class App(BaseView):
	def __init__(self):
		self.BookController = BookController()
		self.BorrowController = BorrowController()
		self.ReturnBookController = ReturnBookController()
		self.RiwayatController = RiwayatController()
		self.database = Database()

	def run(self):
		#while True:
			option = self.menu()
			os.system('cls')
			if option ==1 or option==2 or option==3 or option==4 or option==5:
				self.BookController.main(option)
			elif option==6:
				self.BorrowController.main()
			elif option==7:
				self.ReturnBookController.main()
			elif option==8:
				self.RiwayatController.main()
			elif option==0:
				exit()