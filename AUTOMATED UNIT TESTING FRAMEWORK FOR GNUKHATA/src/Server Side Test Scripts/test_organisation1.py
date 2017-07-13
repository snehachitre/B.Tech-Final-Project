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
		self.server = xmlrpclib.Server("http://localhost:7081", allow_none=True);
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.count=str(self.server.people.getCountMaster(self.client_id))
		self.queryParams=['12','NGO','H582','Sonal','Corner View, Bhandup','Mumbai','400042','Maharastra','India','22558899','3123213213','www.abcd.com','xyz@abc.com']
		
	def test_type_getOrganisationNames(self):
		#print "We are in test_getStateNames"
		result = self.server.organisation.getOrganisationNames(self.client_id)
		if type(result)==list:
			print result
		else:
			print "improper list"
		assert result	
	
	def test_conn_getOrganisationNames(self):
		result = self.server.organisation.getOrganisationNames(self.client_id)
		assert result
		
	def test_wrongdata_getOrganisationNames(self):
		self.client_id=[-89, 'ss', 78.25, '']
		for index in self.client_id:
			result = self.server.organisation.getOrganisationNames(self.client_id)
			assert result
		
	def test_multi_getOrganisationNames(self):
		i=0
		while i<2:
			result = self.server.organisation.getOrganisationNames(self.client_id)
			assert result
			i=i+1	
			
	def test_type_getAllOrganisation(self):
		#print "We are in test_getStateNames"
		result = self.server.organisation.getAllOrganisation(self.client_id)
		if type(result)==list:
			print result
		else:
			print "improper list"
		assert result	
		
	def test_conn_getAllOrganisation(self):
		result = self.server.organisation.getAllOrganisation(self.client_id)
		assert result
		
	def test_wrongdata_getAllOrganisation(self):
		self.client_id=[-89, 'ss', 78.25, '']
		for index in self.client_id:
			result = self.server.organisation.getAllOrganisation(self.client_id)
			assert result
		
	def test_multi_getAllOrganisation(self):
		i=0
		while i<2:
			result = self.server.organisation.getAllOrganisation(self.client_id)
			assert result
			i=i+1		
			
	def test_type_setOrganisation(self):
		#print "We are in test_getStateNames"
		result = self.server.organisation.setOrganisation(self.queryParams,self.client_id)
		if type(result)==list:
			print result
		else:
			print "improper list"
		assert result	
		
	def test_conn_setOrganisation(self):
		result = self.server.organisation.setOrganisation(self.queryParams,self.client_id)
		assert result
		
	def test_wrongdata_setOrganisation(self):
		self.client_id=[-89, 'ss', 78.25, '']
		for index in self.client_id:
			result = self.server.organisation.setOrganisation(self.queryParams,self.client_id)
			assert result
		
	def test_multi_setOrganisation(self):
		i=0
		while i<2:
			result = self.server.organisation.setOrganisation(self.queryParams,self.client_id)
			assert result
			i=i+1		
			
	def test_type_editOrganisation(self):
		#print "We are in test_getStateNames"
		result = self.server.organisation.editOrganisation(self.queryParams,self.client_id)
		if type(result)==list:
			print result
		else:
			print "improper list"
		assert result	
		
	def test_conn_editOrganisation(self):
		self.queryParams=['12','NGO','H582','Sagar','Corner View, Bandra','Mumbai','400042','Maharastra','India','22558899','3123213213','www.abcd.com','xyz@abc.com']
		result = self.server.organisation.editOrganisation(self.queryParams,self.client_id)
		assert result
		
	def test_wrongdata_editOrganisation(self):
		self.client_id=[-89, 'ss', 78.25, '']
		self.queryParams=['25','','H582','Sonal','Corner View, Bhandup','Mum','40','Mah','In','22558899','3123213213','www.abcd','.com']
		for index in self.client_id:
			result = self.server.organisation.editOrganisation(self.queryParams,self.client_id)
			assert result
			index=index+1
		
	def test_multi_editOrganisation(self):
		i=0
		while i<2:
			result = self.server.organisation.editOrganisation(self.queryParams,self.client_id)
			assert result
			i=i+1	

#tearDown function closing up the connection				
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)

# these lines are neccesary to initiate the test case.
if __name__ == '__main__':
		import unittest
		unittest.main()
		
