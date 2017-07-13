'''
Contributors: Sneha S. Chitre <csadhana27@gmail.com>
		Sonal D. Dolas <ssonaldd@gmail.com>
		Nupura S. Walawalkar <greatnups@gmail.com>	
'''
import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
import xmlrpclib,datetime

class test_project(unittest.TestCase):

	def setUp(self):
		print "setup"
		self.server = xmlrpclib.Server("http://localhost:7081");
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.queryParams_sp=["33","utfg","gnu","description","1"]
		
		print "setUp method of test_project."

	def test_type_setProject(self):
		#print "We are in test_type_setProject"
		result = self.server.project.setProject(self.client_id)
		if type(result)==bool:
			print result
			print "ok"
			
		else:
			print "improper boolean"
		assert result	
	
	
	def test_right_setProject(self):
		result = self.server.project.setProject(self.queryParams_sp)
		assert result

	def test_wrongdata_setProject(self):
		self.queryParams_wsp=["","utfg","gnu","description","bc"]
		
		result = self.server.project.setProject(self.queryParams_wsp)
		assert result
	

	def test_multi_setProject(self):
		i=0
		while i<5:
			result = self.server.project.setProject(self.queryParams_sp)
			assert result
			i=i+1	

	def test_type_editProject(self):
		#print "We are in test_type_setProject"
		result = self.server.project.editProject(self.client_id)
		if type(result)==bool:
			print result
			print "ok"
			
		else:
			print "improper boolean"
		assert result	
	
	
	def test_right_editProject(self):
		self.queryParams_sp=["35","ut","gnuk","descri","2"]
		result = self.server.project.editProject(self.queryParams_sp)
		assert result

	def test_wrongdata_editProject(self):
		self.queryParams_wsp=["","utfg","gnu","description","bc"]
		
		result = self.server.project.editProject(self.queryParams_wsp)
		assert result
	

	def test_multi_editProject(self):
		i=0
		while i<5:
			result = self.server.project.editProject(self.queryParams_sp)
			assert result
			i=i+1	

if __name__ == '__main__':
	import unittest
	unittest.main()		
