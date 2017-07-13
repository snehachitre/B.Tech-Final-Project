'''
Contributors: Sneha S. Chitre <csadhana27@gmail.com>
		Sonal D. Dolas <ssonaldd@gmail.com>
		Nupura S. Walawalkar <greatnups@gmail.com>	
'''
import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
import xmlrpclib,datetime

class test_customer(unittest.TestCase):
	
	def setUp(self):
		print "setup"
		self.server = xmlrpclib.Server("http://localhost:7081");
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.queryParams=["33","amey","kailas complex,m g road,borivali","Mumbai","400091","Maharashtra","India","6348262823","34245287","1245","3","www.gmail.com","abc@gmail.com","suhdg"]
	
	def test_right_getCustomer(self):		
		result=self.server.customer.getCustomer(self.client_id)
		assert result
			
	def test_type_getCustomer(self):
		result=self.server.customer.getCustomer(self.client_id)
		print result
		self.failIf(type(result!=list))
		
	def test_wrongdata_getCustomer(self):
		self.queryParams=["1234","nupura","borivali","lakshdwip","400091","india","maharashtra","6348262823","34245287","","3 months","","",""]
		result=self.server.customer.getCustomer(self.client_id)
		assert result
		
	def test_multiple_getCustomer(self):
		i=0
		while i<2:
			result=self.server.customer.getCustomer(self.client_id)
			assert result
			i=i+1
			
	def test_right_setCustomer(self):		
		result=self.server.customer.setCustomer(self.queryParams,self.client_id)
		assert result
		
	def test_type_setCustomer(self):
		result=self.server.customer.setCustomer(self.queryParams,self.client_id)
		print result
		if type(result==bool):
			pass 
		#self.failIf(type(result!=str))
		
	def test_wrongdata_setCustomer(self):
		self.queryParams=["2147483649","","borivali","mumbai","400091","maharashtra","india","6348262823","34245287","","","","",""]
		result=self.server.customer.setCustomer(self.queryParams,self.client_id)
		assert result
	
	def test_right_editCustomer(self):	
		self.queryParams=["33","amey","abc complex,m g road","Mumbai","400091","Maharashtra","India","6348262823","34245287","1245","9","www.gmail.com","abc@gmail.com","suhdg"]
		result=self.server.customer.editCustomer(self.queryParams,self.client_id)
		assert result
		
	def test_type_editCustomer(self):
		self.queryParams=["33","amey","abc complex,m g road","Mumbai","400091","Maharashtra","India","6348262823","34245287","1245","9","www.gmail.com","abc@gmail.com","suhdg"]
		result=self.server.customer.editCustomer(self.queryParams,self.client_id)
		self.failIf(type(result!=bool))
		
	def test_wrongdata_editCustomer(self):
		self.queryParams=["1234","def","dadar","mumbai","400050","maharashtra","india","6348262823","34245287","","","","",""]
		result=self.server.customer.editCustomer(self.queryParams,self.client_id)
		assert result
		
	def test_multiple_editCustomer(self):
		self.queryParams=["23","amey","abc complex,m g road","Mumbai","400091","Maharashtra","India","6348262823","34245287","1245","9","www.gmail.com","abc@gmail.com","suhdg"]
		i=0
		while i<2:
			result=self.server.customer.editCustomer(self.queryParams,self.client_id)
			assert result
			i=i+1
			
	def test_right_getAllCustomerNames(self):		
		result=self.server.customer.getAllCustomerNames(self.client_id)
		assert result
		
		
	def test_type_getAllCustomerNames(self):
		result=self.server.customer.getAllCustomerNames(self.client_id)
		print result
		
	
	def test_wrongdata_getAllCustomerNames(self):
		self.client_id=["-78","dfgi"]
		for index in self.client_id:
			result=self.server.customer.getAllCustomerNames(index)
			assert result
			index=index+1
			
	def test_multiple_getAllCustomerNames(self):
		i=0
		while i<2:
			result=self.server.customer.getAllCustomerNames(self.client_id)
			assert result
			i=i+1
			
	def test_right_getAllCustomer(self):		
		result=self.server.customer.getAllCustomer(self.client_id)
		assert result
		
	
	def test_type_getAllCustomer(self):		
		result=self.server.customer.getAllCustomer(self.client_id)
		self.failIf(type(result!=list))	
		
	
		
	

if __name__ == '__main__':
	import unittest
	unittest.main()	
