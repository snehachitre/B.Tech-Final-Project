'''
Contributors: Sneha S. Chitre <csadhana27@gmail.com>
		Sonal D. Dolas <ssonaldd@gmail.com>
		Nupura S. Walawalkar <greatnups@gmail.com>	
'''

import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
 


class test_main(unittest.TestCase): 
	
	'''SetUp method makes connection to server'''
	def setUp(self):
		print "setUp method of test_main"
		self.server = xmlrpclib.Server("http://localhost:7081", allow_none=True)
		self.queryParams=['amol','1985-86']
	        
               

	#This function tests if the xmlrpc_getOrganisationNames function. It checks whether the output of the function is list of organisation names.
	
	def test_type_getOrganisationNames(self):

		print "We are in test_type_getOrganisationNames"
		result = self.server.getOrganisationNames()
		if type(result)==list:
			print "organisation names list is proper"
		else:
			print "organisation names list is improper" 
		assert result
		print result
		
			
	def test_conn_getOrganisationNames(self):
		result = self.server.getOrganisationNames()
		assert result
	
	def test_wrongdata_getOrganisationNames(self):
		self.client_id=[-89, 'ss', 78.25, '']
		for index in self.client_id:
			result = self.server.getOrganisationNames(index)
			assert result
	
				
	def test_multi_getOrganisationNames(self):
		i=0
		while i<5:
			result = self.server.getOrganisationNames()
			assert result
			i=i+1

	#This function tests if the xmlrpc_getFinancialYear function. It checks whether the years are properly added in the list everytime and also checks the returntype of the function is list.
	def test_type_getFinancialYear(self):

		print "we are in test_type_getFinancialYear"
		res1=self.server.getFinancialYear(self.queryParams[0])	
		if type(res1)==list:
			
			print "financial year list is proper"
			print res1
		else:
			print "financial year list is not proper"
			
		
			
	def test_conn_getFinancialYear(self):
		result = self.server.getFinancialYear(self.queryParams[0])
		assert result

	def test_wrongdata_getFinancialYear(self):
		self.sampleOrgname=['','_#$%%^','987t534gnh','..33....78yuh.']
		index=0
		for index in self.sampleOrgname:
			self.queryParams[0]= index
			result = self.server.getFinancialYear(self.queryParams[0])
			index= index + 1
			assert result

	#This function tests if the function returns the list of databases starting with "gk".
	'''def test_type_getDatabase(self):

		print "we are in test_type_getDatabase"
		res2=self.server.getDatabase()
		if type(res2)==list:
			print "database list is proper"
		else: 
			print "database list is not proper"			
		print res2
		assert res2

	def test_conn_getDatabase(self):
		result = self.server.getDatabase()
		assert result

	def test_wrongdata_getDatabase(self):
		self.client_id=[-89, 'ss', 78.25, '']
		for index in self.client_id:
			result = self.server.getDatabase(index)
			assert result
	
				
	def test_multi_getDatabase(self):
		i=0
		while i<5:
			result = self.server.getDatabase()
			assert result
			i=i+1
'''

		# Test for function xmlrpc_getconnection is commented here because if the xmlrpc_Deploy function is working properly then automatically xmlrpc_getConnection is working properly. this is because in xmlrpc_deploy function is calling this function to get the client_id.
	'''def test_getConnection(self):

		print "we are in test_getConnection"
		res2=self.server.getConnection(self.queryParams)
		if type(res2).__name__=='int':
			print "connection successful"
			print "client_id is", res2'''
			
	
	#This function tests the functionality of xmlrpc_Deploy function. xmlrpc_Deploy function returns a list, boolean character "True" and client_id if the parameters passed are correct. test_deploy1 function checks if the function is returning a list as intended. xmlrpc_Deploy should not work for the same financial year under one organisation and should only return positive integer greater than 0 as client_id.
	def test_right_Deploy(self):

		print "we are in test_right_Deploy"

		# we check that the financial year should not be repeated under the same organization name in the following condition.
		if self.queryParams[1] not in self.server.getFinancialYear(self.queryParams[0]):
			
			result=self.server.Deploy(self.queryParams)
			print result
			assert result
				
			if (result <0):
				self.assertRaises(gnukhata.OutOfRangeError, gnukhata.xmlrpc_Deploy, -1)
				print "client id is negative. test fail"
	
		else:
			print "Same financial year under one organisation name is not allowed"

	'''tearDown closes the connection.'''	
	def tearDown(self):
		print "cleaning up test_debitnotevoucher"


if __name__=='__main__'	:
	import unittest
	unittest.main()

