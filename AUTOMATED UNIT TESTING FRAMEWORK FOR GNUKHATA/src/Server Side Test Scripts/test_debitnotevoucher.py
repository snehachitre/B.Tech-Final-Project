'''Contributors: "Sonal Dolas"<ssonaldd@gmail.com>
	      "Sneha Chitre"<csadhana27@gmail.com>
	      "Nupura Walawalkar"<greatnups@gmail.com>'''
	

import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
from time import strftime
import xmlrpclib,datetime

class test_debitnotevoucher(unittest.TestCase):
	
	'''SetUp method connects to the server'''
	def setUp(self):
	
		print "setup"
		self.server = xmlrpclib.Server("http://localhost:7081",allow_none=True);
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.today_date = datetime.date.today().strftime('%Y-%m-%d')
		
	def test_right_setDebitNote(self):
		self.queryParams_master=["701","501",self.today_date,self.today_date,"","1000","SBI","this is debit narration"]
		self.queryParams_details=["701","501","120","120","2100"]
		result=self.server.debitnotevoucher.setDebitNote(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	def test_type_setDebitNote(self):
		self.queryParams_master=245
		self.queryParams_details=vfvfad
		result=self.server.debitnotevoucher.setDebitNote(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	def test_wrongdata_setDebitNote(self):
		self.queryParams_master=["2147483649","501",self.today_date,self.today_date,"","1000","SBI","this is debit narration"]
		self.queryParams_details=["701","501","120","120","2100"]
		result=self.server.debitnotevoucher.setDebitNote(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	def test_multiple_setDebitNote(self):
		self.queryParams_master=["702","502",self.today_date,self.today_date,"","1000","SBI","this is debit narration"]
		self.queryParams_details=["702","502","120","120","2100"]
		i=0
		while i<2:
			result=self.server.debitnotevoucher.setDebitNote(self.queryParams_master,self.queryParams_details,self.client_id)
			assert result
			i=i+1
	def test_right_getDebitNote(self):
		self.queryParams_details=["701","501","120","120","2100"]
		result=self.server.debitnotevoucher.getDebitNote(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	def test_type_getDebitNote(self):
		self.quereyParams_details=67
		result=self.server.debitnotevoucher.getDebitNote(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	def test_wrongdata_getDebitNote(self):
		self.queryParams_details=["700","501","120","120","2100"]
		result=self.server.debitnotevoucher.getDebitNote(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	def test_multiple_getDebitNote(self):
		self.queryParams_details=["702","501","120","120","2100"]
		i=0
		while i<2:
			result=self.server.debitnotevoucher.getDebitNote(self.queryParams_master,self.queryParams_details,self.client_id)
			assert result
			i=i+1
	def test_right_editDebitNote(self):
		self.queryParams_master=["701","501",self.today_date,self.today_date,"","400","SBI","this is debit narration"]
		self.queryParams_details=["701","501","120","120","2600"]
		result=self.server.debitnotevoucher.editDebitNote(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	def test_type_editDebitNote(self):
		self.queryParams_master=5335
		self.queryParams_details=437
		result=self.server.debitnotevoucher.editDebitNote(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	def test_wrongdata_editDebitNote(self):
		self.queryParams_master=["701","501","",self.today_date,"","400","SBI",""]
		self.queryParams_details=["701","501","2147483649","120","2600"]
		result=self.server.debitnotevoucher.editDebitNote(self.queryParams_master,self.queryParams_details,self.client_id)
		assert result
	def test_multiple_editDebitNote(self):
		self.queryParams_master=["701","501",self.today_date,self.today_date,"","40090","RBI","this is debit narration"]
		self.queryParams_details=["701","501","120","120","2600"]
		i=0
		while i<2:
			result=self.server.debitnotevoucher.editDebitNote(self.queryParams_master,self.queryParams_details,self.client_id)
			assert result
			i=i+1
	'''tearDown closes the connection.'''	
	def tearDown(self):
		print "cleaning up test_debitnotevoucher"

if __name__ == '__main__':
	import unittest
	unittest.main()	
