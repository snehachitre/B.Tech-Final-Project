import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
from time import strftime
import xmlrpclib,datetime

class test_groups(unittest.TestCase):
	
	#This fuction connects to the xmlrpclib server and sets up a testdatabase.
	def setUp(self):
	
		print "setup"
		self.server = xmlrpclib.Server("http://localhost:7081",allow_none=True);
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
	
	def test_right_setGroups(self):
		
		self.queryParams=["1010","Asset","Sundry Debtors","2000.50"]
		result=self.server.groups.setGroups(self.queryParams,self.client_id)
		assert result
		
	def test_type_setGroups(self):

		self.queryParams=["1010","Asset","Sundry Debtors","2000.50"]
		result=self.server.groups.setGroups(self.queryParams,self.client_id)
		if type(result)==bool:
			print "ok"
		else 
			print "incorrect output"
		assert result
		
	def test_wrongdata_setGroups(self):
		
		self.queryParams=["246876438438","Direct Income","Other Charges Received","7800.507"]
		'''if(self.queryParams[0]>2147483647 or type(self.queryParams[0])!='int' or self.queryParams[0]<0):
			print "invalid group code"
		else:'''
		result=self.server.groups.setGroups(self.queryParams,self.client_id)
		assert result
	
	def test_multiple_setGroups(self):
		self.queryParams=["1020","Liability","Sundry Creditors","2000.50"]
		i=0
		while i<3:
			result=self.server.groups.setGroups(self.queryParams,self.client_id)
			assert result
			i=i+1
			
	def test_right_getGroupByCode(self):
		
		self.queryParams=["1010","Asset","Sundry Debtors","2000.50"]
		result=self.server.groups.getGroupByCode(self.queryParams,self.client_id)
		assert result
	
	def test_type_getGroupByCode(self):
		
		self.queryParams=["1010","Asset","Sundry Debtors","2000.50"]
		result=self.server.groups.getGroupByCode(self.queryParams,self.client_id)
		assert result
		if(type(result)!='str'):
			print "incorrect group"
		else:
			print "ok"
		assert result
	
	def test_wrongdata_getGroupByCode(self):
		
		self.queryParams=["246876438438","","Other Charges Received","2000.50"]
		'''if(self.queryParams[0]>2147483647 or type(self.queryParams[0])!='int'):
			print "invalid group code"
		else:'''
		result=self.server.groups.getGroupByCode(self.queryParams,self.client_id)
		assert result
	
	def test_multiple_getGroupByCode(self):
		
		self.queryParams=["1020","Liability","Sundry Creditors","4000"]
		i=0
		while i<2:
			result=self.server.groups.getGroupByCode(self.queryParams,self.client_id)
			assert result
			i=i+1
			
	def test_right_getAllGroups(self):
		
		result=self.server.groups.getAllGroup(self.client_id)
		assert result
	
	def test_type_getAllGroups(self):
		
		result=self.server.groups.getAllGroups(self.client_id)
		if type(result)==list:
			print "ok"
		else:
			print "incorrect list"
			assert result
		
	def test_wrongdata_getAllGroups(self):
		
		self.client_id=["-987432","sdfg",""]
		for index in self.client_id:
			result=self.server.groups.getAllGroups(index)
			assert result
			index=index+1
	def test_multiple_getAllGroups(self):
		
		i=0
		while i<2:
			result=self.server.groups.getAllGroups(self.client_id)
			assert result
			i=i+1
			
	def test_right_updatGroupBalance(self):
		
		self.queryParams=["105","Direct Income","Other Charges Received","2000.50"]
		result=self.server.groups.updateGroupBalance(self.queryParams,self.client_id)
		assert result
		
	def test_type_updateGroupBalance(self):
		
		self.queryParams=["105","Direct Income","Discount Received","3000"]
		result=self.server.groups.updateGroupBalance(self.queryParams,self.client_id)
		if type(result)==bool
			print "ok"
		else:
			print "incorrect output"
		assert result
		
	def test_wrongdata_updateGroupBalance(self):
		
		self.queryParams=["abc","Direct Income","Other Charges Received","2000.50"]
		result=self.server.groups.updateGroupBalance(self.queryParams,self.client_id)
		assert result
	
	def test_multiple_updateGroupBalance(self):
	    
		self.queryParams=["1020","Liability","Sundry Creditors","4500"]
		i=0
		while i<2:
			result=self.server.groups.updateGroupBalance(self.queryParams,self.client_id)
			assert result
			i=i+1
		
	def test_right_getGroupByName(self):
		
		self.queryParams=["134","Direct Income","Other Charges Received","2000.50"]
		result=self.server.groups.getGroupByName(self.queryParams,self.client_id)
		assert result
		
	def test_type_getGroupByName(self):
	
		self.queryParams=["1020","Liability","Sundry Creditors","4000"]
		result=self.server.groups.getGroupByName(self.queryParams,self.client_id)
		if type(result)=='list':
			print "ok"
		else:
			print "incorrect list"
		assert result
		
	def test_wrongdata_getGroupByName(self):
	
		self.queryParams=["346.34","abc","dfg","3543"]
		result=self.server.groups.getGroupByName(self.queryParams,self.client_id)
		assert result
		
	def test_multiple_getGroupByName(self):
		
		self.queryParams=["1020","Liability","Sundry Creditors","4000"]
		i=0
		while i<2:
			result=self.server.groups.getGroupByName(self.queryParams,self.client_id)
			assert result
			i=i+1
	
	def test_right_editGroups(self):
		
		self.queryParams=["1020","Liability","Sundry Creditors","2890"]
		result=self.server.groups.editGroups(self.queryParams,self.client_id)
		assert result
	
	def test_type_editGroups(self):
	
		self.queryParams=["1020","Liability","Sundry Creditors","4000"]
		result=self.server.groups.editGroups(self.queryParams,self.client_id)
		if type(result)==bool:
			print "ok"
		else:
			print "incorrect output"
		assert result
		
	def test_wrongdata_editGroups(self):
	
		self.queryParams=["610","abc","Other Charges Received","2000.50"]
		result=self.server.groups.editGroups(self.queryParams,self.client_id)
		assert result
	
	def test_multiple_editGroups(self):
		
		self.queryParams=["1020","Liability","Sundry Creditors","4000"]
		i=0
		while i<2:
			result=self.server.groups.editGroups(self.queryParams,self.client_id)
			assert result
			i=i+1
			
	def test_right_getGroupNames(self):
		
		result=self.server.groups.getGroupNames(self.client_id)
		assert result
	
	def test_type_getGroupNames(self):
		
		result=self.server.groups.getGroupNames(self.client_id)
		if type(result)==list:
			print "ok"
		else:
			print "incorrect list"
		assert result
	
	def test_wrongdata_getGroupNames(self):
		
		self.client_id=["-987432","sdfg",""]
		for index in self.client_id:
			result=self.server.groups.getGroupNames(self.client_id)
			assert result
	
	def test_multiple_getGroupNames(self):
	
		self.queryParams=["23","Direct Income","Other Charges Received","2000.50"]
		i=0
		while i<2:
			result=self.server.groups.getGroupNames(self.client_id)
			assert result
			i=i+1
		
	def test_right_getGroupNameByAccountName(self):
		
		self.queryParams=["1020","Liability","Sundry Creditors","4000"]
		result=self.server.groups.getGroupNames(self.client_id)
		assert result
	
	def test_type_getGroupNameByAccountName(self):
	
		self.queryParams=abcd
		result=self.server.groups.getGroupNameByAccountName(self.queryParams,self.client_id)
		assert result
		
	def test_wrongdata_getGroupNameByAccountName(self):
	
		self.queryParams=["nups"]
		result=self.server.groups.getGroupNameByAccountName(self.queryParams,self.client_id)
		assert result
		
	def test_multiple_getGroupNameByAccountName(self):
	
		self.queryParams=["1020","Liability","Sundry Creditors","4000"]
		i=0
		while i<2:
			result=self.server.groups.getGroupNames(self.client_id)
			assert result
			i=i+1
	def tearDown(self):
		print "cleaning up test_groups"

if __name__ == '__main__':
	import unittest
	unittest.main()	