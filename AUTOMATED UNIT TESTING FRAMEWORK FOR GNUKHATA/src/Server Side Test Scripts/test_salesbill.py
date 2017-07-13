import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
from time import strftime
import xmlrpclib,datetime

class test_salesbill(unittest.TestCase):
	
	'''SetUp method makes connection to server'''
	def setUp(self):
		print "setup"
		self.server = xmlrpclib.Server("http://localhost:7081",allow_none=True);
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.today_date = datetime.date.today().strftime('%Y-%m-%d')
		
	def test_right_setSalesBill(self):
		'''if self.queryparams not in self.server.salesbill.getSalesBill():
			result = self.server.salesbill.setSalesBill(self.client_id)
			assert result'''
		self.queryParams_master=["501",self.today_date,self.today_date,"abc","Cheque","123456","SBI","33.8","","1000.75","",""]
		self.queryParams_details=["501","501","501","3000","","600","","7.25"]
		self.queryParams_customer=["1234","","","","","","","","","600","","","","",""]		
		result=self.server.salesbill.setSalesBill(self.queryParams_master,self.queryParams_details,self.queryParams_customer,self.client_id)
		assert result	
	def test_type_setSalesBill(self):
		self.queryParams_master=443
		self.queryParams_details=324
		self.queryParams_customer=65
		result=self.server.salesbill.setSalesBill(self.queryParams_master,self.queryParams_details,self.queryParams_customer,self.client_id)
		assert result
	
	def test_wrongdata_setSalesBill(self):
		self.queryParams_master=["",self.today_date,self.today_date,"abc","Cheque","123456","SBI","33.8","","1000.75","",""]
		self.queryParams_details=["","502","502","3000","","600","","7.25"]
		self.queryParams_customer=["abc","","","","","","","","","600","","","","",""]	
		result=self.server.salesbill.setSalesBill(self.queryParams_master,self.queryParams_details,self.queryParams_customer,self.client_id)
		assert result
		
	def test_multiple_setSalesBill(self):
		self.queryParams_master=["503",self.today_date,self.today_date,"abc","Cheque","123456","SBI","33.8","","1000.75","",""]
		self.queryParams_details=["503","503","503","3000","","600","","7.25"]
		self.queryParams_customer=["1235","","","","","","","","","600","","","","",""]	
		i=0
		while i<2:
			result=self.server.salesbill.setSalesBill(self.queryParams_master,self.queryParams_details,self.queryParams_customer,self.client_id)
			assert result
			i=i+1
	
	def test_right_getSalesMaster(self):
		self.queryParams_master=["501",self.today_date,self.today_date,"abc","Cheque","123456","SBI","33.8","","1000.75","",""]
		results=self.server.salesbill.getSalesBill(self.queryParams_master,self.client_id)
		assert result
	
	def test_type_getSalesMaster(self):
		self.queryParams_master=sdsd
		results=self.server.salesbill.getSalesBill(self.queryParams_master,self.client_id)
		assert result
		
	def test_wrongdata_getSalesMaster(self):
		self.queryParams_master=["",self.today_date,self.today_date,"abc","Cheque","123456","SBI","33.8","","1000.75","",""]
		results=self.server.salesbill.getSalesBill(self.queryParams_master,self.client_id)
		assert result
	
	def test_multiple_getSalesMaster(self):
		self.queryParams_master=["502",self.today_date,self.today_date,"abc","Cheque","123456","SBI","33.8","","1000.75","",""]
		i=0
		while i<2:
			results=self.server.salesbill.getSalesBill(self.queryParams_master,self.client_id)
			assert result
			i=i+1
			
	def test_right_getSalesDetails(self):
		self.queryParams_details=["501","503","503","3000","","600","","7.25"]
		result=self.server.salesbill.getSalesBill(self.queryParams_details,self.client_id)
		assert result
		
	def test_type_getSalesDetails(self):
		self.queryParams=849
		result=self.server.salesbill.getSalesBill(self.queryParams_details,self.client_id)
		assert result
		
	def test_wrongdata_getSalesDetails(self):
		self.queryParams_details=["502","503","503","3000","","600","","7.25"]
		result=self.server.salesbill.getSalesBill(self.queryParams_details,self.client_id)
		assert result
	
	def test_multiple_getSalesDetails(self):
		self.queryParams_details=["503","503","503","3000","","600","","7.25"]
		i=0
		while i<2:
			result=self.server.salesbill.getSalesBill(self.queryParams_details,self.client_id)
			assert result
			i=i+1
	
	def test_right_getSalesDetailsByProductCode(self):
		self.queryParams_details=["501","501","501","3000","","600","","7.25"]
		result=self.server.salesbill.getSalesDetailsByProductCode(self.queryParams_details,self.client_id)
		assert result
		
	def test_type_getSalesDetailsByProductCode(self):
		self.queryParams_details=343
		result=self.server.salesbill.getSalesDetailsByProductCode(self.queryParams_details,self.client_id)
		assert result
		
	def test_wrongdata_getSalesDetailsByProductCode(self):
		self.queryParams_details=["504","504","504","3000","","600","","7.25"]
		result=self.server.salesbill.getSalesDetailsByProductCode(self.queryParams_details,self.client_id)
		assert result
	
	def test_multiple_getSalesDetailsByProductCode(self):
		self.queryParams_details=["501","501","501","3000","","600","","7.25"]
		i=0
		while i<2:
			result=self.server.salesbill.getSalesDetailsByProductCode(self.queryParams_details,self.client_id)
			assert result
			i=i+1
	
	def test_right_editSalesBill(self):
		self.queryParams_master=["501",self.today_date,self.today_date,"def","CHEQUE","123456","SBI","33.8","Flat Discount","1000.75","",""]
		self.queryParams_details=["501","501","501","3500","","700","","7.25"]
		self.queryParams_customer=["1234","","","","","","","","","600","","","","",""]	
		result=self.server.salesbill.editSalesBill(self.queryParams_master,self.queryParams_details,self.queryParams_customer,self.client_id)
		assert result
	
	def test_type_editSalesBill(self):
		self.queryParams_master=443
		self.queryParams_details=324
		self.queryParams_customer=65
		result=self.server.salesbill.editSalesBill(self.queryParams_master,self.queryParams_details,self.queryParams_customer,self.client_id)
		assert result
	
	def test_wrongdata_editSalesBill(self):
		self.queryParams_master=["",self.today_date,self.today_date,"abc","Cheque","123456","SBI","33.8","","1000.75","",""]
		self.queryParams_details=["","502","502","3000","","600","","7.25"]
		self.queryParams_customer=["abc","","","","","","","","","600","","","","",""]	
		result=self.server.salesbill.editSalesBill(self.queryParams_master,self.queryParams_details,self.queryParams_customer,self.client_id)
		assert result
	
	def test_multiple_editSalesBill(self):
		self.queryParams_master=["505",self.today_date,self.today_date,"def","CHEQUE","123456","SBI","33.8","","1000.75","",""]
		self.queryParams_details=["505","505","505","3500","","700","","7.25"]
		self.queryParams_customer=["1234","","","","","","","","","600","","","","",""]
		i=0
		while i<2:
			result=self.server.salesbill.editSalesBill(self.queryParams_master,self.queryParams_details,self.queryParams_customer,self.client_id)
			assert result
			i=i+1
	
	'''tearDown closes the connection.'''	
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)

		
if __name__ == '__main__':
	import unittest
	unittest.main()
