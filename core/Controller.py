class Controller(object):
	"""docstring for ClassName"""
	def models(self, Model):
		eval(f'from model.{Model} import {Model}')
		return Model()

	def views(self,View):
		eval(f'from view.{View} import {View}')
		return View()
	
	def controllers(self,Controller):
		eval(f'from controller.{Controller} import {Controller}')
		return Controller()
		