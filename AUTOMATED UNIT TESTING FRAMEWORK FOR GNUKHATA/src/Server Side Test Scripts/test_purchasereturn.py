'''Contributors: "Sonal Dolas"<ssonaldd@gmail.com>
	      "Sneha Chitre"<csadhana27@gmail.com>
	      "Nupura Walawalkar"<greatnups@gmail.com>'''
	
import xmlrpclib
import unittest             
from unittest import TestCase

		
class test_purchasereturn(unittest.TestCase):
	
	'''SetUp method makes connection to server'''
	def setUp(self):
		self.server = xmlrpclib.Server("http://localhost:7081")
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.queryParams_master=['1','2011-02-04','abc','200','10']
		self.queryParams_details=['1','22','20','2','2','12','12','10']
		self.amountpaid=200
		
	def test_right_setPurchaseReturn(self):
		result=self.server.purchasereturn.setPurchaseReturn(self.queryParams_master,self.queryParams_details,self.amountpaid, self.client_id)
		assert result
		
	
	def test_type_setPurchaseReturn(self):
		result=self.server.purchasereturn.setPurchaseReturn(self.queryParams_master,self.queryParams_details,self.amountpaid, self.client_id)
		if type(result)==bool:
			print "ok"
		else:
			print "incorrect type"
		assert result
		
	def test_multi_setPurchaseReturn(self):
		i=0
		while i<2:
			result=self.server.purchasereturn.setPurchaseReturn(self.queryParams_master,self.queryParams_details,self.amountpaid, self.client_id)
			assert result
			i=i+1
	
	def test_wrongdata_setPurchaseReturn(self):
		self.queryParams_master=[]
		self.queryParams_details=[]
		self.amountpaid=[]
		result=self.server.purchasereturn.setPurchaseReturn(self.queryParams_master,self.queryParams_details,self.amountpaid, self.client_id)
		assert result
		
	
	def test_right_getPurchaseReturn(self):
		self.queryParams=['11aa','2011-03-08','hiiijj','booktype','12345678','SBI','22','20','2','2','12','12','10']
		result=self.server.purchasereturn.getPurchaseReturn(self.queryParams, self.client_id)
		assert result
		
	def test_type_getPurchaseReturn(self):
		self.queryParams=['11aa','2011-03-08','hiiijj','booktype','12345678','SBI','22','20','2','2','12','12','10']
		result=self.server.purchasereturn.getPurchaseReturn(self.queryParams, self.client_id)
		if type(result)==list:
			print "ok"
		else:
			print "incorrect type"
		assert result
		
	def test_multi_getPurchaseReturn(self):
		self.queryParams=['11aa','2011-03-08','hiiijj','booktype','12345678','SBI','22','20','2','2','12','12','10']
		i=0
		while i<2:
			result=self.server.purchasereturn.getPurchaseReturn(self.queryParams, self.client_id)
			assert result
			i=i+1	
	
	def test_wrongdata_getPurchaseReturn(self):
		self.queryParams=[]
		result=self.server.purchasereturn.getPurchaseReturn(self.queryParams, self.client_id)
		assert result
	
	def test_right_getPrevPurchaseReturn(self):
		self.queryParams=['11aa','2011-03-08','hiiijj','booktype','12345678','SBI','22','20','2','2','12','12','10']
		result=self.server.purchasereturn.getPrevPurchaseReturn(self.queryParams, self.client_id)
		assert result
		
	def test_type_getPrevPurchaseReturn(self):
		self.queryParams=['11aa','2011-03-08','hiiijj','booktype','12345678','SBI','22','20','2','2','12','12','10']
		result=self.server.purchasereturn.getPrevPurchaseReturn(self.queryParams, self.client_id)
		if type(result)==list:
			print "ok"
		else:
			print "incorrect type"
		assert result	
		
	def test_multi_getPrevPurchaseReturn(self):
		self.queryParams=['11aa','2011-03-08','hiiijj','booktype','12345678','SBI','22','20','2','2','12','12','10']
		i=0
		while i<2:
			result=self.server.purchasereturn.getPrevPurchaseReturn(self.queryParams, self.client_id)
			assert result	
			i=i+1
			
	def test_right_getPurchaseReturnQuantity(self):
		self.queryParams=['22','r','20']
		result=self.server.purchasereturn.getPurchaseReturnQuantity(self.queryParams, self.client_id)
		assert result
	
	def test_type_getPurchaseReturnQuantity(self):
		self.queryParams=['22','r','20']
		result=self.server.purchasereturn.getPurchaseReturnQuantity(self.queryParams, self.client_id)
		if type(result)==list:
			print "ok"
		else:
			print "incorrect type"
		assert result	
		
	def test_multi_getPurchaseReturnQuantity(self):
		self.queryParams=['22','r','20']
		i=0
		while i<2:
			result=self.server.purchasereturn.getPurchaseReturnQuantity(self.queryParams, self.client_id)
			assert result
			i=i+1
		
	def test_wrongdata_getPurchaseReturnQuantity(self):
		self.queryParams=[]
		result=self.server.purchasereturn.getPurchaseReturnQuantity(self.queryParams, self.client_id)
		assert result

	'''tearDown closes the connection.'''	
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)
		
if __name__ == '__main__':
	import unittest
	unittest.main()	
