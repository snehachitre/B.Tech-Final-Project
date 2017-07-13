'''Contributors: "Sonal Dolas"<ssonaldd@gmail.com>
	      "Sneha Chitre"<csadhana27@gmail.com>
	      "Nupura Walawalkar"<greatnups@gmail.com>'''
	
import xmlrpclib
import unittest             
from unittest import TestCase

		
class test_data(unittest.TestCase):
	
	'''SetUp method connects to the server'''
	def setUp(self):
		self.server = xmlrpclib.Server("http://localhost:7081")
		self.dbname = ["kapil","2000-01"]
		self.client_id = self.server.getConnection(self.dbname)
		
	def test_type_getStateNames(self):
		print "We are in test_getStateNames"
		result = self.server.data.getStateNames(self.client_id)
		if type(result)==list:
			print result
		else:
			print "improper list"
		assert result
			
	def test_right_getStateNames(self):
		result = self.server.data.getStateNames(self.client_id)
		assert result
		
	def test_wrongdata_getStateNames(self):
		self.client_id=[-89, 'ss', 78.25]
		for index in self.client_id:
			result = self.server.data.getStateNames(self.client_id[index])
			assert result
			index=index+1
			
				
	def test_multi_getStateNames(self):
		i=0
		while i<2:
			result = self.server.data.getStateNames(self.client_id)
			assert result
			i=i+1
		
	def test_type_getCityNames(self):
		print "We are in test_getStateNames"
		self.queryParams = ['Maharashtra']
		result = self.server.data.getCityNames(self.queryParams,self.client_id)
		if type(result)==list:
			print result
		else:
			print "improper list"
		
		assert result
			
	def test_right_getCityNames(self):
		self.queryParams = ['Maharashtra']
		result = self.server.data.getCityNames(self.queryParams,self.client_id)
		assert result
		
	def test_wrongdata_getCityNames(self):
		self.queryParams = ['Mah','12','54.88', ' ']
		for index in self.queryParams:
			result = self.server.data.getCityNames(self.queryParams[index],self.client_id)
			assert result
			index=index+1
			
	def test_multi_getCityNames(self):
		self.queryParams = ['Maharashtra']
		i=0
		while i<2:
			result = self.server.data.getCityNames(self.queryParams,self.client_id)
			print result
			assert result
			i=i+1
	
	'''tearDown closes the connection.'''	
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)
	

if __name__ == '__main__':
		import unittest
		unittest.main()
