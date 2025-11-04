import sys, os, json


class Application:
	def __init__(self) -> None:
		self.config = None
		self.base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))

	def load_config(self) -> None:
		config_path = os.path.join(self.base_path, 'data', 'config.json')
		with open(config_path, 'r') as f:
			self.config = json.load(f)

	def execute_(self) -> None:
		pass


if __name__ == '__main__':
	main = Application()
	main.execute_()