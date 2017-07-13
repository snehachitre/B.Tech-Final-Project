'''Contributors: "Sonal Dolas"<ssonaldd@gmail.com>
	      "Sneha Chitre"<csadhana27@gmail.com>
	      "Nupura Walawalkar"<greatnups@gmail.com>'''
	
import xmlrpclib
import unittest
from unittest import TestCase

class test_organisation(unittest.TestCase):

#setUp fuction connects to the xmlrpclib server and sets up a testdatabase.	
	def setUp(self):
		print "setUp method of test_organisation"
		self.server = xmlrpclib.Server("http://localhost:7081");
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.count=str(self.server.people.getCountMaster(self.client_id))
		self.queryParams=['ooo','NGO','H582','Sonal','Corner View, Bhandup','Mumbai','400042','Maharastra','India','22558899','3123213213','www.abcd.com','xyz@abc.com']
		print "setUp method of test_organisation."

#test_editOrganisation method checks whether result is list and list is returning proper queryParams or not.		
	def test_editOrganisation(self):
		print "We are in test_editOrganisation"
		result = self.server.organisation.editOrganisation(self.queryParams,self.client_id)
		if type(result)!=list:
			print "improper list"
			
		try:
			assert result
		except AssertionError:
			print "Assertion Error in test_editOrganisation"

#test_getOrganisationNames method checks whether result is list and list is returning Organisation names or not.		
	def test_getOrganisationNames(self):
		print "We are in test_getOrganisationNames"
		result = self.server.organisation.getOrganisationNames(self.client_id)
		if type(result)!=list:
			print "improper list"
					
		try:
			assert result
			print result
		except AssertionError:
			print "Assertion Error in test_getOrganisationNames...."

#test_getAllOrganisation method checks whether result is list and list is returning all organisation information.	
	def test_getAllOrganisation(self):
		print "We are in test_getAllOrganisation"
		result = self.server.organisation.getAllOrganisation(self.client_id)
		if type(result)!=list:
			print "improper list"
					
		try:
			assert result
			print result
		except AssertionError:
			print "Assertion Error in test_getAllOrganisation...."

#test_setOrganisation method checks whether result is True.
	def test_setOrganisation(self):
		if self.queryParams[0] not in self.server.organisation.getOrganisationNames(self.client_id):
			result = self.server.organisation.setOrganisation(self.queryParams,self.client_id)
						
			try:
				assert result
				print result
			except AssertionError:
				print "Assertion Error...."
				
#tearDown function closing up the connection				
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)

# these lines are neccesary to initiate the test case.
if __name__ == '__main__':
		import unittest
		unittest.main()
		
