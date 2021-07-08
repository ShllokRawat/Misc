import os
import glob
import shutil
'''
["music", "video", "documents"]
[[".mp3", ".wav"], [".mov"], [".pdf"]]
'''
class Organizer:

	def __init__(self, folders, extensions):
		'''
		Args

		folders  (list): list of folder names you want to create
		extensions (list): list of extensions corresponding to folders
		'''
		self.folders = folders
		self.extensions = extensions
		for f in folders:
			try:
				os.mkdir(f)
			except:
				print("Directory Exists")

	def get_extensions_for_folder(self, folder_name):
		'''
		get_extensions_for_folder('music')
		[".mp3", ".wav"]
		'''
		for i in range(0, len(self.folders)):
			if self.folders[i] == folder_name:
				return self.extensions[i]

	def get_files_for_folder(self, folder_name):
		exts = self.get_extensions_for_folder(folder_name) #music -> [".mp3", ".wav"]
		files = []
		for ext in exts:
			string_ext = "*" + ext # "*.mp3"
			files += glob.glob(string_ext)
		return files

	def move_files(self, folder_name):
		files = self.get_files_for_folder(folder_name)
		for file in files:
			shutil.move(file, folder_name)
























