'''Contributors: "Sonal Dolas"<ssonaldd@gmail.com>
	      "Sneha Chitre"<csadhana27@gmail.com>
	      "Nupura Walawalkar"<greatnups@gmail.com>'''
	
import xmlrpclib
import unittest             
from unittest import TestCase

		
class test_vendor(unittest.TestCase):

	'''SetUp method makes connection to server'''
	def setUp(self):
		self.server = xmlrpclib.Server("http://localhost:7081")
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.queryParams=['sonal','mulund ','mumbai','400042','maharashtra','India','123456785','hui457','98','3','www.fgf.com','acd@ggg.com','jjj']
		
		
	def test_type_getVendor(self):
		self.queryParams=['code','1']
		result=self.server.vendor.getVendor(self.queryParams, self.client_id)
		if type(result)==list:
			print "ok"
		else:
			print "incorrect output"
		print result
		assert result
		
	def test_right_getVendor(self):
		self.queryParams=['code','12']
		result=self.server.vendor.getVendor(self.queryParams, self.client_id)
		print result
		assert result
		
	def test_multi_getVendor(self):
		self.queryParams=['code','12']
		i=0
		while i<2:
			result=self.server.vendor.getVendor(self.queryParams, self.client_id)
			assert result
			i=i+1
			
	test_wrongdata_getVendor(self):	
		self.queryParams=[]
		result=self.server.vendor.getVendor(self.queryParams, self.client_id)
		print result
		assert result

	def test_type_setVendor(self):
		
		result=self.server.vendor.setVendor(self.queryParams, self.client_id)
		if type(result)==bool:
			print "ok"
		else:
			print "incorrect output"
		print result
		assert result	
	
	def test_right_setVendor(self):
		
		result=self.server.vendor.setVendor(self.queryParams, self.client_id)
		print result
		assert result
		
	def test_multi_setVendor(self):
		
		i=0
		while i<2:
			result=self.server.vendor.setVendor(self.queryParams, self.client_id)
			assert result
			i=i+1		
			
	def test_wrongdata_setVendor(self):	
		self.queryParams=[]
		result=self.server.vendor.setVendor(self.queryParams, self.client_id)
		print result
		assert result	

	def test_type_editVendor(self):
		
		result=self.server.vendor.editVendor(self.queryParams, self.client_id)
		if type(result)==bool:
			print "ok"
		else:
			print "incorrect output"
		print result
		assert result
		
	
	def test_right_editVendor(self):
		
		result=self.server.vendor.editVendor(self.queryParams, self.client_id)	
		print result
		assert result
		
	def test_multi_editVendor(self):
		i=0
		while i<2:
			result=self.server.vendor.editVendor(self.queryParams, self.client_id)	
			assert result	
			i=i+0
			
	def test_wrongdata_editVendor(self):	
		self.queryParams=[]
		result=self.server.vendor.editVendor(self.queryParams, self.client_id)	
		print result
		assert result

	def test_type_getAllVendorNames(self):
		self.queryParams=['code','12']
		self.result_vendor=self.server.vendor.getVendor(self.queryParams, self.client_id)
		result=self.server.vendor.getAllVendorNames(self.result_vendor[1], self.client_id)
		if type(result)==list:
			print "ok"
		else:
			print "incorrect output"
		print result
		assert result
		
	
	def test_right_getAllVendorNames(self):
		self.queryParams=['code','12']
		self.result_vendor=self.server.vendor.getVendor(self.queryParams, self.client_id)
		result=self.server.vendor.getAllVendorNames(self.result_vendor[1], self.client_id)
		print result	
		assert result
		
		
	def test_multi_getAllVendorNames(self):
		self.queryParams=['code','12']
		self.result_vendor=self.server.vendor.getVendor(self.queryParams, self.client_id)
		i=0
		while i<2:
			result=self.server.vendor.getAllVendorNames(self.result_vendor[1], self.client_id)	
			assert result
			i=i+0
			
	def test_wrongdata_getAllVendorNames(self):	
		self.queryParams=[]
		self.result_vendor=self.server.vendor.getVendor(self.queryParams, self.client_id)
		result=self.server.vendor.getAllVendorNames(self.result_vendor[1], self.client_id)
		print result	
		assert result

	def test_type_getAllVendors(self):
		result=self.server.vendor.getAllVendors(self.client_id)
		if type(result)==bool:
			print "ok"
		else:
			print "incorrect output"
		print result
		assert result
		
	def test_right_getAllVendors(self):
		result=self.server.vendor.getAllVendors(self.client_id)
		print result
		assert result
		
	def test_multi_getAllVendors(self):
		i=0
		while i<2:
			result=self.server.vendor.getAllVendors(self.client_id)
			assert result
			i=i+1
		
	def test_wrongdata_getAllVendor(self):	
		self.client_id=[]
		result=self.server.vendor.getAllVendors(self.client_id)
		print result
		assert result
		
	'''tearDown closes the connection.'''	
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)


if __name__ == '__main__':
		import unittest
		unittest.main()
		
			
			
			
	
	
	
	
