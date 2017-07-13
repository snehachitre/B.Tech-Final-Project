import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
from time import strftime
import xmlrpclib,datetime

class test_reports(unittest.TestCase):
	
	'''SetUp method makes connection to server'''
	def setUp(self):
	
		print "setup"
		self.server = xmlrpclib.Server("http://localhost:7081", allow_none=True);
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
	
	def test_right_getTrialBalance(self):
		
		result=self.server.reports.getTrialBalance(self.client_id)
		assert result
		
	def test_multiple_getTrialBalance(self):
	
		i=0
		while i<2:
			result=self.server.reports.getTrialBalance(self.client_id)
			assert result
			i=i+1
	'''tearDown closes the connection.'''	
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)
if __name__ == '__main__':
	import unittest
	unittest.main()	
