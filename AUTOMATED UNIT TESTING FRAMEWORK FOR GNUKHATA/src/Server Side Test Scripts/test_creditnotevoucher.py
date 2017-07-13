import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
from time import strftime
import xmlrpclib,datetime


class test_creditnotevoucher(unittest.TestCase):
	
	'''SetUp method connects to the server'''
	def setUp(self):
		print "setup"
		self.server = xmlrpclib.Server("http://localhost:7081", allow_none=True);
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.queryParams_master=['1','12-2-1998','2-2-1998','ddffr sww']
		self.queryParams_details=['2','154','885','4578']
		self.queryParams=['3','55','15-5-1998','book type','154875','yes bank','kijjo','458','895','458712']
		
	def test_type_setCreditNote(self):
		result = self.server.creditnotevoucher.setCreditNote(self.queryParams_master,self.queryParams_details,self.client_id)
		self.failIf(type(result!=bool))
		
	def test_right_setCreditNote(self):
		result = self.server.creditnotevoucher.setCreditNote(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
		
	def test_multiple_setCreditNote(self):
		if self.queryParams_master[0] not in self.server.creditnotevoucher.getCreditNote(self.queryParams,self.client_id):
			i=0
			while i<5:
				result = self.server.creditnotevoucher.setCreditNote(self.queryParams_master,self.queryParams_details,self.client_id)
				assert result
				i=i+1
		else:
			print "same voucher code is not allowed"
			
	def test_wrong_setCreditNote(self):
		self.queryParams_master=['','','','']
		self.queryParams_details=['','','','']
		result = self.server.creditnotevoucher.setCreditNote(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
		
	def test_type_editCreditNote(self):
		result = self.server.creditnotevoucher.editCreditNote(self.queryParams_master,self.queryParams_details,self.client_id)
		self.failIf(type(result!=bool))
		
	def test_right_editCreditNote(self):
		result = self.server.creditnotevoucher.editCreditNote(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	
	def test_multiple_editCreditNote(self):
		if self.queryParams_master[0] not in self.server.creditnotevoucher.getCreditNote(self.queryParams,self.client_id):
			i=0
			while i<5:
				result = self.server.creditnotevoucher.editCreditNote(self.queryParams_master,self.queryParams_details,self.client_id)
				assert result
				i=i+1
		else:
			print "same voucher code is not allowed"		
	
	def test_wrong_editCreditNote(self):
		self.queryParams_master=['','','','']
		self.queryParams_details=['','','','']
		result = self.server.creditnotevoucher.editCreditNote(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	
	
	def test_type_getCreditNote(self):
		result = self.server.creditnotevoucher.getCreditNote(self.queryParams,self.client_id)
		self.failIf(type(result!=list))
		
	def test_right_getCreditNote(self):
		result = self.server.creditnotevoucher.getCreditNote(self.queryParams,self.client_id)
		assert result
	
	def test_multiple_getCreditNote(self):
		if self.queryParams_master[0] not in self.server.creditnotevoucher.getCreditNote(self.queryParams,self.client_id):
			i=0
			while i<5:
				result = self.server.creditnotevoucher.getCreditNote(self.queryParams,self.client_id)
				assert result
				i=i+1
		else:
			print "same voucher code is not allowed"
	
	def test_wrong_getCreditNote(self):
		self.queryParams=['','','','','','','','','','']
		result = self.server.creditnotevoucher.getCreditNote(self.queryParams,self.client_id)
		assert result

	'''tearDown closes the connection.'''
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)
	
	
if __name__ == '__main__':
		import unittest
		unittest.main()	
		
