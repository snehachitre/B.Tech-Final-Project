'''
Contributors: Sneha S. Chitre <csadhana27@gmail.com>
		Sonal D. Dolas <ssonaldd@gmail.com>
		Nupura S. Walawalkar <greatnups@gmail.com>	
'''

import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase


class test_main(unittest.TestCase): 
	
	#This fuction connects to the xmlrpclib server and sets up a testdatabase.
	def setUp(self):
		print "setUp method of test_main"
		self.server = xmlrpclib.Server("http://localhost:7081", allow_none=True)
	       	
                self.queryParams=['testdb2','1956-57']
		

	#This function tests if the xmlrpc_getOrganisationNames function. It checks whether the output of the function is list of organisation names.
	def test_getOrganisationNames(self):

		print "we are in test_getOrganisationNames"
		res= self.server.getOrganisationNames()
		if type(res).__name__=='list':

			print "organisation names list is proper"
			print res
		else:
			print "organisation names list is not proper"

	#This function tests if the xmlrpc_getFinancialYear function. It checks whether the years are properly added in the list everytime and also checks the returntype of the function is list.
	def test_getFinancialYear(self):

		print "we are in test_getFinancialYear"
		res1=self.server.getFinancialYear(self.queryParams[0])	
		if type(res1).__name__=='list':
			
			print "financial year list is proper"
			print res1
		else:
			print "financial year list is not proper"
			
		

	#This function tests if the function returns the list of databases starting with "gk".
	def test_getDatabase(self):

		print "we are in test_getDatabase"
		res2=self.server.getDatabase()
		if type(res2).__name__=='list':
			print "database list is proper"
			print res2
		else: 
			print "database list is not proper"			
	
	# Test for function xmlrpc_getconnection is commented here because if the xmlrpc_Deploy function is working properly then automatically xmlrpc_getConnection is working properly. this is because in xmlrpc_deploy function is calling this function to get the client_id.
	def test_getConnection(self):

		print "we are in test_getConnection"
		res2=self.server.getConnection(self.queryParams)
		if type(res2).__name__=='int':
			print "connection successful"
			print "client_id is", res2
			
	
	#This function tests the functionality of xmlrpc_Deploy function. xmlrpc_Deploy function returns a list, boolean character "True" and client_id if the parameters passed are correct. test_deploy1 function checks if the function is returning a list as intended. xmlrpc_Deploy should not work for the same financial year under one organisation and should only return positive integer greater than 0 as client_id.
	def test_Deploy(self):

		print "we are in test_Deploy"

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

if __name__=='__main__'	:
	import unittest
	unittest.main()

