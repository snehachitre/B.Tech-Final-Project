'''Contributors: "Sonal Dolas"<ssonaldd@gmail.com>
	      "Sneha Chitre"<csadhana27@gmail.com>
	      "Nupura Walawalkar"<greatnups@gmail.com>'''
	
import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
from time import strftime
import xmlrpclib,datetime



class test_customizable(unittest.TestCase):
	
	'''SetUp method connects to the server'''
	def setUp(self):
		print "setup"
		self.server = xmlrpclib.Server("http://localhost:7081", allow_none=True);
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.queryPramas_master=['35','abcxyz','this is a text']
		self.queryParamas_details=['12','35','huy','40','35']
		
	def test_type_setCustomizable(self):
		result = self.server.customizable.setCustomizable(self.queryPramas_master,self.queryParamas_details,self.client_id)
		if type(result)==bool:
			print "ok"
		else:
			print "assert error"
		print result
		assert result
		
	
	def test_right_setCustomizable(self):
		result = self.server.customizable.setCustomizable(self.queryPramas_master,self.queryParamas_details,self.client_id)
		assert result
		
	def test_wrongdata_setCustomizable(self):
		self.queryPramas_master=['','','']
		self.queryParamas_details=['','','','','']
		result = self.server.customizable.setCustomizable(self.queryPramas_master,self.queryParamas_details,self.client_id)
		assert result

	def test_multi_setCustomizable(self):
		i=0
		while i<2:
			result = self.server.customizable.setCustomizable(self.queryPramas_master,self.queryParamas_details,self.client_id)
			assert result
			i=i+1
		
	def test_type_getCustomCode(self):
		result = self.server.customizable.getCustomCode(self.client_id)
		if type(result)==str:
			print "ok"
		else:
			print "error"
		print result
		assert result
		
		
	def test_right_getCustomCode(self):
		result = self.server.customizable.getCustomCode(self.client_id)
		assert result
		
	def test_multi_getCustomCode(self):
		i=0
		while i<2:
			result = self.server.customizable.getCustomCode(self.client_id)
			assert result
			i=i+1
		
	def test_wrongdata_getCustomCode(self):
		self.client_id = ['']
		result = self.server.customizable.getCustomCode(self.client_id)
		assert result

'''tearDown closes the connection.'''
	def tearDown(self):
		print "cleaning up test_customer"

if __name__ == '__main__':
	import unittest
	unittest.main()	
