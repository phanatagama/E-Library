from core import *
from controller.StaffController import *

staff = StaffController()
if staff.login():
	while True:
		MyApp = App()
		MyApp.run()