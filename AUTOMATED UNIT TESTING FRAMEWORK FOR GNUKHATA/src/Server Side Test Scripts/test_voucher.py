'''Contributors: "Sonal Dolas"<ssonaldd@gmail.com>
	      "Sneha Chitre"<csadhana27@gmail.com>
	      "Nupura Walawalkar"<greatnups@gmail.com>'''
	
import xmlrpclib
import unittest             
from unittest import TestCase

	
		
class test_voucher(unittest.TestCase):
	'''SetUp method makes connection to server'''
	def setUp(self):
		self.server = xmlrpclib.Server("http://localhost:7081")
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		
	def test_type_setVoucher(self):
		self.queryParams=['6','Payment']
		result=self.server.voucher.setVoucher(self.queryParams, self.client_id)
		if type(result)==bool:
			print "ok"
		else:
			print "incorrect output"
		print result
		assert result
	
	def test_right_setVoucher(self):
		self.queryParams=['10','Payment']
		result=self.server.voucher.setVoucher(self.queryParams, self.client_id)
		print result
		assert result
		
	def test_multi_setVoucher(self):
		self.queryParams=['5','Payment']
		i=0
		while i<2:
			result=self.server.voucher.setVoucher(self.queryParams, self.client_id)
			print result
			assert result
		i=i+1
	
	def test_wrongdata_setVoucher(self):
		self.queryParams=[]
		result=self.server.voucher.setVoucher(self.queryParams, self.client_id)
		print result
		assert result		

	def test_type_getVoucher(self):
		self.queryParams=['2','Receivable']
		result=self.server.voucher.getVoucher(self.queryParams, self.client_id)
		if type(result)==list:
			print "ok"
		else:
			print "incorrect output"
		print result
		assert result
		
	def test_right_getVoucher(self):
		self.queryParams=['11','Receivable']
		result=self.server.voucher.getVoucher(self.queryParams, self.client_id)
		print result
		assert result
		
	def test_multi_getVoucher(self):
		self.queryParams=['12','Receivable']
		i=0
		while i<2:
			result=self.server.voucher.getVoucher(self.queryParams, self.client_id)
			print result
			assert result
			i=i+1
			
	def test_wrongdata_getVoucher(self):
		self.queryParams=[]
		result=self.server.voucher.getVoucher(self.queryParams, self.client_id)
		print result
		assert result	

	def test_type_getVoucherCode(self):
		self.queryParams=['8']
		result=self.server.voucher.getVoucherCode(self.queryParams, self.client_id)
		if type(result)==list:
			print "ok"
		else:
			print "incorrect output"
		print result
		assert result
		
	def test_right_getVoucherCode(self):
		self.queryParams=['8']
		result=self.server.voucher.getVoucherCode(self.queryParams, self.client_id)
		print result
		assert result
		
	def test_multi_getVoucherCode(self):
		self.queryParams=['8']
		i=0
		while i<2:
			result=self.server.voucher.getVoucherCode(self.queryParams, self.client_id)
			print result
			assert result
			i=i+1
			
	def test_wrongdata_getVoucherCode(self):
		self.queryParams=[]
		result=self.server.voucher.getVoucherCode(self.queryParams, self.client_id)
		print result
		assert result
	
	def test_type_getSpecificVoucherCodes(self):
		self.queryParams=['Payment']
		result=self.server.voucher.getSpecificVoucherCodes(self.queryParams, self.client_id)
		if type(result)==list:
			print "ok"
		else:
			print "incorrect output"
		print result
		assert result
		
	def test_right_getSpecificVoucherCodes(self):
		self.queryParams=['Payment']
		result=self.server.voucher.getSpecificVoucherCodes(self.queryParams, self.client_id)
		print result
		assert result
		
	def test_multi_getSpecificVoucherCodes(self):
		self.queryParams=['Payment']
		i=0
		while i<2:
			result=self.server.voucher.getSpecificVoucherCodes(self.queryParams, self.client_id)
			print result
			assert result
			i=i+1
			
	def test_wrongdata_getSpecificVoucherCodes(self):
		self.queryParams=[]
		result=self.server.voucher.getSpecificVoucherCodes(self.queryParams, self.client_id)
		print result
		assert result

	'''tearDown closes the connection.'''	
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)


if __name__ == '__main__':
		import unittest
		unittest.main()
