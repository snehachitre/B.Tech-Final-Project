'''Contributors: "Sonal Dolas"<ssonaldd@gmail.com>
	      "Sneha Chitre"<csadhana27@gmail.com>
	      "Nupura Walawalkar"<greatnups@gmail.com>'''
	
import xmlrpclib
import unittest             
from unittest import TestCase

class test_receivable(unittest.TestCase): 

	'''SetUp method makes connection to server'''
	def setUp(self):
		self.server = xmlrpclib.Server("http://localhost:7081")
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.queryParams_master=['2','2000-01-22','2000-01-20','text']
		self.queryParams_details=['asdf','123','12','11','452658']
		self.vouchertype='receivable'	
		self.amt=452658
		self.queryParams=['3','1998-05-30','eded','456789','yes bank','text','12','12','2','4587']
		self.queryParams1=['458']
		
	def test_type_setReceivable(self):
		result = self.server.receivable.setReceivable(self.queryParams_master,self.queryParams_details,self.vouchertype,self.amt,self.client_id)
		if type(result)==bool:
			print result
		else:
			print "improper list"
		assert result
		
	def test_right_setReceivable(self):
		result = self.server.receivable.setReceivable(self.queryParams_master,self.queryParams_details,self.vouchertype,self.amt,self.client_id)
		assert result

	def test_wrongdata_setReceivable(self):
		self.queryParams_master=[]
		self.queryParams_details=[]
		self.vouchertype=[]
		self.amt=[]
		result = self.server.receivable.setReceivable(self.queryParams_master,self.queryParams_details,self.vouchertype,self.amt,self.client_id)
		assert result
		
	def test_multi_setReceivable(self):
		if self.queryParams_master[0] not in self.server.receivable.getReceivable(self.queryParams,self.client_id):
			i=0
			while i<5:		
				result = self.server.receivable.setReceivable(self.queryParams_master,self.queryParams_details,self.vouchertype,self.amt,self.client_id)
				assert result
				i=i+1
		else:
			print "same vouchercode is not allowed"

	def test_type_getReceivable(self):
		result = self.server.receivable.getReceivable(self.queryParams,self.client_id)
		if type(result)==list:
			print result
		else:
			print "improper list"
		assert result
		
	def test_right_getReceivable(self):
		result = self.server.receivable.getReceivable(self.queryParams,self.client_id)
		assert result
	
	def test_wrongdata_setReceivable(self):
		self.queryParams=[]
		result = self.server.receivable.getReceivable(self.queryParams,self.client_id)
		assert result
		

	def test_multi_getReceivable(self):
		if self.queryParams_master[0] not in self.server.receivable.getReceivable(self.queryParams,self.client_id):
			i=0
			while i<5:		
				result = self.server.receivable.getReceivable(self.queryParams,self.client_id)
				assert result
				i=i+1
		else:
			print "same vouchercode is not allowed"
			
	def test_type_getReceivableByReferenceNo(self):
		result = self.server.receivable.getReceivableByReferenceNo(self.queryParams,self.client_id)
		if type(result)==list:
			print result
		else:
			print "improper list"
		assert result
	
	def test_right_getReceivableByReferenceNo(self):
		result = self.server.receivable.getReceivableByReferenceNo(self.queryParams,self.client_id)
		assert result
		
	def test_wrongdata_getReceivableByReferenceNo:
		self.queryParams=[]
		result = self.server.receivable.getReceivableByReferenceNo(self.queryParams,self.client_id)
		assert result

	def test_multi_getReceivableByReferenceNo(self):
		if self.queryParams_master[0] not in self.server.receivable.getReceivable(self.queryParams,self.client_id):
			i=0
			while i<5:		
				result = self.server.receivable.getReceivableByReferenceNo(self.queryParams,self.client_id)
				assert result
				i=i+1
		else:
			print "same vouchercode is not allowed"
			
	def test_type_getReceivableBalance(self):
		result = self.server.receivable.getReceivableBalance(self.queryParams1,self.client_id)
		if type(result)==list:
			print result
		else:
			print "improper list"
		assert result
	
	def test_right_getReceivableBalance(self):
		result = self.server.receivable.getReceivableBalance(self.queryParams1,self.client_id)
		assert result
		
	def test_wrongdata_getReceivableBalance
		self.queryParams1=[]
		result = self.server.receivable.getReceivableBalance(self.queryParams1,self.client_id)
		assert result

	def test_multi_getReceivableBalance(self):
		if self.queryParams_master[0] not in self.server.receivable.getReceivable(self.queryParams,self.client_id):
			i=0
			while i<5:		
				result = self.server.receivable.getReceivableBalance(self.queryParams1,self.client_id)
				assert result
				i=i+1
		else:
			print "same vouchercode is not allowed"
			
	def test_type_editReceivable(self):
		result = self.server.receivable.editReceivable(self.queryParams_master,self.queryParams_details,self.vouchertype,self.amt,self.client_id)
		if type(result)==bool:
			print result
		else:
			print "improper list"
		assert result
			
			
	def test_right_editReceivable(self):
		result = self.server.receivable.editReceivable(self.queryParams_master,self.queryParams_details,self.vouchertype,self.amt,self.client_id)
		assert result
		
	def test_wrongdata_editReceivable(self):
		self.queryParams_master=[]
		self.queryParams_details=[]
		self.vouchertype=[]
		self.amt=[]
		result = self.server.receivable.editReceivable(self.queryParams_master,self.queryParams_details,self.vouchertype,self.amt,self.client_id)
		assert result	

	def test_multi_editReceivable(self):
		if self.queryParams_master[0] not in self.server.receivable.getReceivable(self.queryParams,self.client_id):
			i=0
			while i<5:
				result = self.server.receivable.editReceivable(self.queryParams_master,self.queryParams_details,self.vouchertype,self.amt,self.client_id)
				assert result
		else:
			print "same vouchercode is not allowed"
			
	'''tearDown closes the connection.'''	
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)

if __name__ == '__main__':
		import unittest
		unittest.main()
