'''Contributors: "Sonal Dolas"<ssonaldd@gmail.com>
	      "Sneha Chitre"<csadhana27@gmail.com>
	      "Nupura Walawalkar"<greatnups@gmail.com>'''
	
import xmlrpclib
import unittest             
from unittest import TestCase

class test_contravoucher(unittest.TestCase): 
	
	'''SetUp method connects to the server'''
	def setUp(self):
		        self.server = xmlrpclib.Server("http://localhost:7081")
		      	self.dbname = ["testdb3","2003-04"]
			self.client_id = self.server.getConnection(self.dbname)
			
	def test_type_getContraAccounts(self):
		result=self.server.contravoucher.getContraAccounts(self.client_id)
		self.failIf(type(result!=list))
			
	def test_conn_getContraAccounts(self):
		result = self.server.data.getStateNames(self.client_id)
		assert result
		
	def test_wrongdata_getContraAccounts(self):
		self.client_id=[-89, 'ss', 78.25, '']
		for index in self.client_id:
			result=self.server.contravoucher.getContraAccounts(index)
			assert result
		
	def test_multi_getContraAccounts(self):
		i=0
		while i<5:
			self.queryParams = ['Maharashtra']
			result = self.server.data.getStateNames(self.client_id)
			assert result
			i=i+1
			
		
	'''tearDown closes the connection.'''
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)
	

if __name__ == '__main__':
		import unittest
		unittest.main()
