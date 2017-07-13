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
	
	'''SetUp method connects to the server'''
	def setUp(self):
		print "setup"
		self.server = xmlrpclib.Server("http://localhost:7081",allow_none=True);
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		
	
	def test_right_getCustomer(self):		
		self.queryParams=["1234","nupura","borivali","Mumbai","400091","Maharashtra","India","6348262823","34245287","A7584","3 months","www.123engg.com","123user@gmail.com","abc"]
		result=self.server.customer.getCustomer(self.queryParams,self.client_id)
		assert result
		'''if type(result).__name__=='list':
			print result
		else:
			self.failIf(type(result)!=Boolean)
			print result'''
	
	def test_type_getCustomer(self):
		self.queryParams=["1670","sneha","santacruz","Mumbai","400091","Maharashtra","India","6348262823","34245287","A564","3 months","www.123engg.com","123user@gmail.com","abc"]
		result=self.server.customer.getCustomer(self.queryParams,self.client_id)
		if type(result)==list:
			print result
		else:
			assert result
		
	def test_wrongdata_getCustomer(self):
		self.queryParams=["123432525235254","","borivali","Mumbai","400091","Maharashtra","India","6348262823","34245287","A7584","","www.123engg.com","123user@gmail.com","abc"]
		result=self.server.customer.getCustomer(self.queryParams,self.client_id)
		assert result
		
	def test_multiple_getCustomer(self):
		self.queryParams=["300","nupura","borivali","Mumbai","400091","Maharashtra","India","6348262823","34245287","A7584","3 months","www.123engg.com","123user@gmail.com","abc"]
		i=0
		while i<2:
			result=self.server.customer.getCustomer(self.client_id)
			assert result
			i=i+1
	def test_right_setCustomer(self):		
		self.queryParams=["4000","sonal","mulund","Mumbai","400091","Maharashtra","India","439862823","34245287","A7584","10 months","www.123engg.com","123user@gmail.com","abc"]
		result=self.server.customer.setCustomer(self.queryParams,self.client_id)
		assert result
		
	def test_type_setCustomer(self):
		self.queryParams=["124655","nupura","borivali","Pune","400091","Maharashtra","India","6348262823","34245287","A7584","3 months","www.123engg.com","123user@gmail.com","abc"]
		result=self.server.customer.setCustomer(self.queryParams,self.client_id)
		if type(result)==list:
			print result
		else:
			assert result
		
	def test_wrongdata_setCustomer(self):
		self.queryParams=["214748374649","","borivali","mumbai","400091","maharashtra","india","6348262823","34245287","B573","","www.gmail.com","420user@yahoo.com","uawerifuaogsf"]
		result=self.server.customer.setCustomer(self.queryParams,self.client_id)
		assert result
		
	def test_multiple_setCustomer(self):
		self.queryParams=["4060","sonal","mulund","Mumbai","400091","Maharashtra","India","439862823","34245287","A7584","10 months","www.123engg.com","123user@gmail.com","abc"]
		i=0
		while i<2:
			result=self.server.customer.setCustomer(self.queryParams,self.client_id)
			assert result
			i=i+1
			
	def test_right_editCustomer(self):	
		self.queryParams=["1234","nupura","borivali","Nagpur","400066","Maharashtra","India","6348262823","34245287","A7584","6 months","www.123engg.com","123user@gmail.com","abc"]
		result=self.server.customer.editCustomer(self.queryParams,self.client_id)
		assert result
		
	def test_type_editCustomer(self):
		self.queryParams=["4000","sonal","mulund","Pune","400091","Maharashtra","India","439862823","45900034","A7584","10 months","www.123engg.com","123user@gmail.com","abc"]
		result=self.server.customer.editCustomer(self.queryParams,self.client_id)
		if type(result)==bool:
			print result
		else:
			assert result
		
	def test_wrongdata_editCustomer(self):
		self.queryParams=["1234","def","dadar","mumbai","400050","maharashtra","india","6348262823","34245287","","","","",""]
		result=self.server.customer.editCustomer(self.queryParams,self.client_id)
		assert result
		
	def test_multiple_editCustomer(self):
		self.queryParams=["1234","nupura","dadar","mumbai","400050","goa","india","64876823","74837958","","2 months","","",""]
		i=0
		while i<2:
			result=self.server.customer.editCustomer(self.queryParams,self.client_id)
			assert result
			i=i+1
	def test_right_getAllCustomerNames(self):		
		result=self.server.customer.getAllCustomerNames(self.client_id)
		assert result
		'''if type(result).__name__=='list':
				print result
				print "check"'''
		
	def test_type_getAllCustomerNames(self):
		result=self.server.customer.getAllCustomerNames(self.client_id)
		if type(result)==list
			print result
		else:
			assert result
	
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
		
	'''tearDown closes the connection.'''
	def tearDown(self):
		print "cleaning up test_customer"

if __name__ == '__main__':
	import unittest
	unittest.main()	
