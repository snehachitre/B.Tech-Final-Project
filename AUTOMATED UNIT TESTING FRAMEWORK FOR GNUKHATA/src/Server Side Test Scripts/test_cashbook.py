'''
Contributors: Sneha S. Chitre <csadhana27@gmail.com>
		Sonal D. Dolas <ssonaldd@gmail.com>
		Nupura S. Walawalkar <greatnups@gmail.com>	
'''
import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
import xmlrpclib,datetime

class test_cashbook(unittest.TestCase):

	def setUp(self):
		self.server = xmlrpclib.Server("http://localhost:7081",allow_none=True)
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.accountcode=self.server.account.setAccount()
	
	def test_right_setCashBook(self):
		self.queryParams_master=["nupura",self.today_date,self.today_date,"gnukhata"]
		self.queryParams_details=["abc","100","100","100.123456"]
		result=self.server.cashbook.setCashBook(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	
	def test_type_setCashBook(self):
		self.queryParams_master=5478
		self.queryParams_details=["abcdef","100","100","100.123456"]
		result=self.server.cashbook.setCashBook(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	
	def test_wrongdata_setCashBook(self):
		self.queryParams_master=["abcdef",self.today_date,self.today_date,"gnukhata"]
		self.queryParams_details=["abcdef","100.73","100.857","100.56284727349"]
	    result=self.server.cashbook.setCashBook(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	
	def test_multiple_setCashBook(self):
		self.queryParams_master=["nupura",self.today_date,self.today_date,"gnukhata"]
		self.queryParams_details=["abc","100","100","100.123456"]
		i=0
		while i<2:
			result=self.server.cashbook.setCashBook(self.queryParams_master,self.queryParams_details,self.client_id)
			assert result
			i=i+1
	def test_right_editCashBook(self):			
		self.queryParams_master=["nupura",self.today_date,self.today_date,"gnu"]
		self.queryParams_details=["abc","100","100","100.123456"]
		result=self.server.cashbook.editCashBook(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	def test_type_editVoucher(self):
		self.queryParams_master=783
		self.queryParams_details=df
		result=self.server.cashbook.editCashBook(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	def test_wrongdata_editVoucher(self):
		self.today_date1=datetime.date.today().strftime('%D-%m-%y')
		self.queryParams_master=["nupura",self.today_date1,self.today_date,"gnu"]
		self.queryParams_details=["abc","100","100","100.123456"]
		result=self.server.cashbook.editCashbook(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	def test_multiple_editVoucher(self):
		self.queryParams_master=["nupura",self.today_date,self.today_date,"gnu"]
		self.queryParams_details=["abc","100","100","100.123456"]
		i=0
		while i<2:
			result=self.server.cashbook.editCashBook(self.queryParams_master,self.queryParams_details,self.client_id)
			assert result
			i=i+1
	def test_right_getVoucher(self):	
		self.queryParams_master=["nupura",self.today_date,self.today_date,"gnu"]
        result=self.server.cashbook.getVoucher(self.queryParams,self.client_id)
		assert result
		#self.failIf(type(result[0])!=Integer & type(result[1]!=String) & type(result[2]!=String) & type(result[3]!=String) & type(result[4]!=String) & type(result[5]!=Float) & type(res1[6]!=String))	
	def test_type_getVoucher(self):
		self.queryParams_maaster=456
		result=self.server.cashbook.getVoucher(self.queryParams_master,self.client_id)
		assert result
	def test_wrongdata_getVoucher(self):
		self.queryParams_master=["nupura",self.today_date,self.today_date,"gnu"]
		result=self.server.cashbook.getVoucher(self.queryParams_master,self.client_id)
		assert result
	def test_multiple_getVoucher(self):
		self.queryParams_master=["nupura",self.today_date,self.today_date,"gnu"]
		i=0
		while i<2:
			result=self.server.cashbook.getVoucher(self.queryParams_master,self.client_id)
			assert result
			i=i+1
	def tearDown(self):
		print "cleaning up test_cashbook"

if __name__ == '__main__':
	import unittest
	unittest.main()	