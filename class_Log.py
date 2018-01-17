#!/usr/bin/python
#-*- coding: utf-8 -*-

from datetime import *
class logger():
	"""Gestion des logs"""
	def __init__(self, log_name):
		self.log_name = log_name

	def info(self, msg):
		"""Log d'information"""
		timing = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		file = open(self.log_name, "a+")
		file.write(timing + "  [INFO] " + msg)
		file.write("\n")
		file.close()
		
	def error(self, msg):
		"""log d'erreur"""
		timing = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		file = open(self.log_name, "a+")
		file.write(timing + " [ERROR] " + msg)
		file.write("\n")
		file.close()