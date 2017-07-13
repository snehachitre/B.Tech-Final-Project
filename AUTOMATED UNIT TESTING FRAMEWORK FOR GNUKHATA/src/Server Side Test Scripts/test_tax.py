import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
from time import strftime
import xmlrpclib,datetime

class test_tax(unittest.TestCase):
	
	'''SetUp method makes connection to server'''
	def setUp(self):
	
		print "setup"
		self.server = xmlrpclib.Server("http://localhost:7081",allow_none=True);
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
				
	def test_right_setTax(self):
		self.queryParams=["tax105","50","this is tax"]
		result=self.server.tax.setTax(self.queryParams,self.client_id)
		assert result
	
	def test_type_setTax(self):
		self.queryParams=["tax305","50","this is tax"]
		result=self.server.tax.setTax(self.queryParams,self.client_id)
		if type(result)==bool:
			print "ok"
		else:
			print "incorrect output"
		assert result
	
	def test_wrongdata_setTax(self):
		self.queryParams=["","1234567890112.789","THIS IS TAX"]
		result=self.server.tax.setTax(self.queryParams,self.client_id)
		assert result
	
	def test_multiple_setTax(self):
		self.queryParams=["tax1089","55","this is tax"]
		i=0
		while i<2:
			result=self.server.tax.setTax(self.queryParams,self.client_id)
			assert result
			i=i+1
	def test_right_getTax(self):
		self.queryParams=["tax1010","55","this is tax"]
		result=self.server.tax.getTax(self.queryParams,self.client_id)
		assert result
		
			
	def test_type_getTax(self):
		self.queryParams=["tax1010","55","this is tax"]
		result=self.server.tax.getTax(self.queryParams,self.client_id)
		if type(result)==list:
			print "ok"
		else:
			print "incorrect list"
		assert result
	
	def test_wrongdata_getTax(self):
		self.queryParams=["","55","this is tax"]
		result=self.server.tax.getTax(self.queryParams,self.client_id)
		assert result
	
	def test_multiple_getTax(self):
		self.queryParams=["tax1010","40","this is tax"]
		i=0
		while i<2:
			result=self.server.tax.getTax(self.queryParams,self.client_id)
			assert result
			i=i+1
	def test_right_editTax(self):
		self.queryParams=["tax1010","40","this is tax2"]
		result=self.server.tax.editTax(self.client_id)
		assert result
		
	def test_type_editTax(self):
		self.queryParams=["tax1010","55","this is tax"]
		result=self.server.tax.editTax(self.client_id)
		if type(result)==bool:
			print "ok"
		assert result
	
	def test_wrongdata_editTax(self):
		self.queryParams=["ab","","this is tax"]
		result=self.server.tax.editTax(self.queryParams,self.client_id)
		assert result
	
	def test_multiple_editTax(self):
		self.queryParams=["tax1010","40","this is nottax"]
		i=0
		while i<2:
			result=self.server.tax.getTax(self.queryParams,self.client_id)
			assert result
			i=i+1
		
	def test_right_getTaxNames(self):
		result=self.server.tax.getTaxNames(self.client_id)
		assert result
		
	def test_type_getTaxNames(self):

		result=self.server.tax.getTaxNames(self.client_id)
		if type(result)==list:
			print "ok"
		else:
			print "incorrect list"
		assert result
	
	def test_wrongdata_getTaxNames(self):
		self.client_id=["-99","","gfdjh"]
		result=self.server.tax.getTaxNames(self.client_id)
		assert result
	def test_multiple_getTaxNames(self):
		i=0
		while i<2:
			result=self.server.tax.getTaxNames(self.client_id)
			assert result
			i=i+1
	def test_right_getAllTaxes(self):
		result=self.server.tax.getAllTaxes(self.client_id)
		assert result
		
	def test_type_getAllTaxes(self):
		
		result=self.server.tax.getAllTaxes(self.client_id)
		if type(result)==list:
			print "ok"
		else:
			print "incorrect list"
		assert result
	
	def test_wrongdata_getAllTaxes(self):
		self.client_id=["-89","","jghy"]
		result=self.server.tax.getAllTaxes(self.client_id)
		assert result
	
	def test_multiple_getAllTaxes(self):
		i=0
		while i<2:
			result=self.server.tax.getAllTaxes(self.client_id)
			assert result
			i=i+1

	'''tearDown closes the connection.'''	
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)

if __name__ == '__main__':
	import unittest
	unittest.main()	
