import os
import json
from time import sleep



class proccessAutoCloser():
	
	def __init__(self):

		self.proccessesNames = json.load(open('static.json', 'r'))

		return self.task_killing()


	def task_killing(self):

		for item in self.proccessesNames:

			os.system(f'taskkill /f /im "{item}"')
			#print(f'o item da vez é {item}')

		sleep(10)
		return self.__init__()



if __name__ == '__main__':
	proccessAutoCloser()
