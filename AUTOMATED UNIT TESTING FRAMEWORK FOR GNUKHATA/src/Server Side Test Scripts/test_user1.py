'''Contributors: "Sonal Dolas"<ssonaldd@gmail.com>
	      "Sneha Chitre"<csadhana27@gmail.com>
	      "Nupura Walawalkar"<greatnups@gmail.com>'''
	
import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase


class test_user(unittest.TestCase):
	
	'''SetUp method makes connection to server'''
	def setUp(self):
		
		self.server = xmlrpclib.Server("http://localhost:7081");
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		
	def test_type_changepassword(self):
		self.queryparams=['sonal','abc123','accountant']
		result= self.server.user.changepassword(self.queryparams,self.client_id)
		self.failIf(type(result)!=bool)
				
	
	def test_right_changepassword(self):
		self.queryparams=['sonal','abc123','accountant']
		result= self.server.user.changepassword(self.queryparams,self.client_id)
		assert result
		
	def test_wrongdata_changepassword(self):
		self.queryparams=['','','ggg']
		result= self.server.user.changepassword(self.queryparams,self.client_id)
		assert result
		
	def test_null_changepassword(self):
		self.queryparams=['','','']
		result= self.server.user.changepassword(self.queryparams,self.client_id)
		assert result
		
	def test_type_getUser(self):
		self.queryparams=78
		result= self.server.user.getUser(self.queryparams,self.client_id)
		self.failIf(type(result)!=str)
		
		
			
	def test_right_getUser(self):
		self.queryparams=['sonal','abc123','accountant']
		result= self.server.user.getUser(self.queryparams,self.client_id)
		assert result
		
	def test_wrongdata_getUser(self):
		self.queryparams=['','','ggg']
		result= self.server.user.getUser(self.queryparams,self.client_id)
		assert result
		
	def test_null_getUser(self):
		self.queryparams=['','','']
		result= self.server.user.getUser(self.queryparams,self.client_id)
		assert result
		
		
	def test_type_setUser(self):
		self.queryparams=['sonal','abc123','accountant']
		result = self.server.user.setUser(self.queryparams,self.client_id)
		self.failIf(type(result)!=bool)
		
			
	def test_right_setUser(self):
		self.queryparams=['sonal','abc123','accountant']
		result = self.server.user.setUser(self.queryparams,self.client_id)
		assert result
		
	def test_wrongdata_setUser(self):
		self.queryparams=['','','ggg']
		result = self.server.user.setUser(self.queryparams,self.client_id)
		self.failIf(result==True)
		
		
	def test_null_setUser(self):
		self.queryparams=['','','']
		result = self.server.user.setUser(self.queryparams,self.client_id)
		self.failIf(result==True)
		
	'''tearDown closes the connection.'''	
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)


if __name__ == '__main__':
		import unittest
		unittest.main()
		
		
		
		
