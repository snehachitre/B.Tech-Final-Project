'''Contributors: "Sonal Dolas"<ssonaldd@gmail.com>
	      "Sneha Chitre"<csadhana27@gmail.com>
	      "Nupura Walawalkar"<greatnups@gmail.com>'''
	
import xmlrpclib
import unittest             
from unittest import TestCase

		
class test_purchasebill(unittest.TestCase):

	'''SetUp method makes connection to server'''
	def setUp(self):
		self.server = xmlrpclib.Server("http://localhost:7081")
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.queryParams_master=['12','2011-02-03','2011-02-03','ddd','CASH','1234567890','SBI','2','Flat Discount','10','TAX','10']
		self.queryParams_product=['20','15','HAT','this is text','10','20','2','5']
		self.queryParams_details=['12','15','2','Flat Discount','10','TAX','10']
		self.queryParams_vendor=['abc','this is address','mumbai','400042','maharashtra','India','15478963','this is fax','15478','3','','abc@bbc.com','ahbty jju']
		
	def test_right_setPurchaseBill(self):
		result=self.server.purchasebill.setPurchaseBill(self.queryParams_master,self.queryParams_details,self.queryParams_product,self.queryParams_vendor, self.client_id)
		assert result
		
	def test_type_setPurchaseBill(self):
		result=self.server.purchasebill.setPurchaseBill(self.queryParams_master,self.queryParams_details,self.queryParams_product,self.queryParams_vendor, self.client_id)
		if type(result)==bool:
			print "correct"
		else:
			print "incorrect"	
		assert result	
		
	def test_multi_setPurchaseBill(self):
		i=0
		while i<2:
			result=self.server.purchasebill.setPurchaseBill(self.queryParams_master,self.queryParams_details,self.queryParams_product,self.queryParams_vendor, self.client_id)
			assert result	
			i=i+1
		
	def test_wrongdata_setPurchaseBill(self):
		self.queryParams_master=[]
		self.queryParams_details=[]
		self.queryParams_product=[]
		self.queryParams_vendor=[]
		result=self.server.purchasebill.setPurchaseBill(self.queryParams_master,self.queryParams_details,self.queryParams_product,self.queryParams_vendor, self.client_id)
		assert result
	
	def test_right_getPurchaseMaster(self):
		self.queryParams=['10','2011-05-10','12','sss','CASH','124578','SBI','0','20','tax']
		result=self.server.purchasebill.getPurchaseMaster(self.queryParams, self.client_id)
		assert result	
		
	def test_type_getPurchaseMaster(self):
		self.queryParams=['10','2011-05-10','12','sss','CASH','124578','SBI','0','20','tax']
		result=self.server.purchasebill.getPurchaseMaster(self.queryParams, self.client_id)
		if type(result)==list:
			print "correct"
		else:
			print "incorrect"
		assert result		
		
	def test_multi_getPurchaseMaster(self):
		self.queryParams=['10','2011-05-10','12','sss','CASH','124578','SBI','0','20','tax']
		i=0
		while i<2:
			result=self.server.purchasebill.getPurchaseMaster(self.queryParams, self.client_id)
			assert result	
			i=i+1
	
	def test_wrong_getPurchaseMaster(self):	
		self.queryParams=['','','','','','','','','','']
		result=self.server.purchasebill.getPurchaseMaster(self.queryParams, self.client_id)
		assert result
	
	def test_right_getPurchaseDetails(self):
		self.queryParams=['10','20','12','10','tax','200']
		result=self.server.purchasebill.getPurchaseDetails(self.queryParams, self.client_id)
		print result
		assert result	
		
	def test_type_getPurchaseDetails(self):
		self.queryParams=['10','20','12','10','tax','200']
		result=self.server.purchasebill.getPurchaseDetails(self.queryParams, self.client_id)
		if type(result)==list:
			print "correct"
		else:
			print "incorrect"
		assert result	
		
	def test_multi_getPurchaseDetails(self):
		self.queryParams=['10','20','12','10','tax','200']
		i=0
		while i<2:
			result=self.server.purchasebill.getPurchaseDetails(self.queryParams, self.client_id)
			assert result	
			i=i+1
		
	def test_wrongdata_getPurchaseDetails(self):
		self.queryParams=['','','','','','']
		result=self.server.purchasebill.getPurchaseDetails(self.queryParams, self.client_id)
		print result
		assert result

	
	def test_right_getPurchaseDetailsByProductCode(self):
		self.queryParams=['10','20','12','10','tax','200']
		result=self.server.purchasebill.getPurchaseDetailsByProductCode(self.queryParams, self.client_id)
		assert result	
		
	def test_type_getPurchaseDetailsByProductCode(self):
		self.queryParams=['10','20','12','10','tax','200']
		result=self.server.purchasebill.getPurchaseDetailsByProductCode(self.queryParams, self.client_id)
		if type(result)==list:
			print "correct"
		else:
			print "incorrect"
		assert result	
		
	def test_multi_getPurchaseDetailsByProductCode(self):
		self.queryParams=['10','20','12','10','tax','200']
		i=0
		while i<2:
			result=self.server.purchasebill.getPurchaseDetailsByProductCode(self.queryParams, self.client_id)
			assert result	
			i=i+1
		
	def test_wrongdata_getPurchaseDetailsByProductCode(self):
		self.queryParams=['','','','','','']
		result=self.server.purchasebill.getPurchaseDetailsByProductCode(self.queryParams, self.client_id)
		assert result	

	def test_right_editPurchaseBill(self):
		self.queryParams=['10','2011-05-10','12','sss','CASH','124578','SBI','0','20','tax']
		result=self.server.purchasebill.editPurchaseBill(self.queryParams, self.client_id)
		assert result
		
	def test_type_editPurchaseBill(self):
		self.queryParams=['10','2011-05-10','12','sss','CASH','124578','SBI','0','20','tax']
		result=self.server.purchasebill.editPurchaseBill(self.queryParams, self.client_id)
		if type(result)==bool:
			print "correct"
		else:
			print "incorrect"
		assert result
		
	def test_multi_editPurchaseBill(self):
		self.queryParams=['10','2011-05-10','12','sss','CASH','124578','SBI','0','20','tax']
		i=0
		while i<2:
			result=self.server.purchasebill.editPurchaseBill(self.queryParams, self.client_id)
			assert result	
			i=i+1
			
	def test_right_getAmount(self):
		self.queryParams=['10','2011-05-10','12','sss','CASH','124578','SBI','0','20','tax']
		result=self.server.purchasebill.getAmount(self.queryParams, self.client_id)
		assert result		
			
	def test_type_getAmount(self):
		self.queryParams=['10','2011-05-10','12','sss','CASH','124578','SBI','0','20','tax']
		result=self.server.purchasebill.getAmount(self.queryParams, self.client_id)
		if type(result)==list:
			print "correct"
		else:
			print "incorrect"
		assert result	
		
	def test_multi_getAmount(self):
		self.queryParams=['10','2011-05-10','12','sss','CASH','124578','SBI','0','20','tax']
		i=0
		while i<2:
			result=self.server.purchasebill.getAmount(self.queryParams, self.client_id)
			assert result		
			i=i+1
		
	def test_wrongdata_getAmount(self):
		self.queryParams=['','','','','','','','','','']
		result=self.server.purchasebill.getAmount(self.queryParams, self.client_id)
		assert result	

	'''tearDown closes the connection.'''	
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)
		
if __name__ == '__main__':
	import unittest
	unittest.main()			
		
		
