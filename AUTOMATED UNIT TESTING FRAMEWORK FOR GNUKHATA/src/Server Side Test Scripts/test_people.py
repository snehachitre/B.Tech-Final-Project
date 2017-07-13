import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
from time import strftime
import xmlrpclib,datetime

class test_people(unittest.TestCase):

	def setUp(self):
		print "setup"
		self.server = xmlrpclib.Server("http://localhost:7081",allow_none=True);
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
	
	def test_right_setPeopleDetails(self):
		self.queryParams=["200","nupura","Vendor/Supplier","borivali","mumbai","400078","maharashtra","india","26354262","348912736","","1000","","",""]
		result=self.server.people.setPeopleDetails(self.querParams,self.client_id)
		assert result
	
	def test_type_setPeopleDetails(self):
		self.queryParams=0
		result=self.server.people.setPeopleDetails(self.queryParams,self.client_id)
		assert result
	
	def test_wrongdata_setPeopleDetails(self):
	    self.queryParams=["3573945793475","nupura","Vendor/Supplier","abhaurgfwAIEF","asuherguierhg","iuervgfiuaer","india","","26354262","348912736","","1000","","",""]
	    if(self.queryParams[0]>2147483647 or type(self.queryParams[0])!='int' or self.queryParams[0]<0):
			print "invalid people code"
	    else:
			result=self.server.people.setPeopleDetails(self.queryParams,self.client_id)
			assert result		
	
	def test_multiple_setPeopleDetails(self):
		self.queryParams=["201","sss","Vendor/Supplier","borivali","mumbai","400078","maharashtra","india","26354262","348912736","","1000","","",""]
		i=0
		while i<5:
			result=self.server.people.setPeopleDetails(self.querParams,self.client_id)
			assert result
			i=i+1
	
	def test_right_setPeopleMaster(self):
		self.queryParams=["202","nupura","abc","abhaurgfwAIEF","asuherguierhg","iuervgfiuaer","india","","26354262","348912736","","1000","","",""]
		result=self.server.people.setPeopleMaster(self.queryParams,self.client_id)
		assert result
		
	def test_type_setPeopleMaster(self):
		self.queryParams=213
		result=self.server.people.setPeopleMaster(self.queryParams,self.client_id)
		assert result
	
	def test_wrongdata_setPeopleMaster(self):
		self.queryParams=["2147483648","nupura","abc","abhaurgfwAIEF","asuherguierhg","iuervgfiuaer","india","","26354262","348912736","","1000","","",""]
		if(self.queryParams[0]>2147483647 or type(self.queryParams[0])!='int' or self.queryParams[0]<0):
			print "invalid people code"
		else:
			result=self.server.people.setPeopleMaster(self.queryParams,self.client_id)
			assert result
	
	def test_multiple_setPeopleMaster(self):
	        self.queryParams=["203","nupura","abc","abhaurgfwAIEF","asuherguierhg","iuervgfiuaer","india","","26354262","348912736","","1000","","",""]
		i=0
		while i<2:
			result=self.server.people.setPeopleMaster(self.queryParams,self.client_id)
			assert result
			i=i+1
	
	def test_right_editPeopleMaster(self):
		self.queryParams=["204","nupura","abc","abhaurgfwAIEF","asuherguierhg","iuervgfiuaer","india","","26354262","348912736","","1000","","",""]
		result=self.server.people.editPeopleMaster(self.queryParams,self.client_id)
		assert result
		
	def test_type_editPeople(self):
		self.queryParams=346
		result=self.server.people.editPeopleMaster(self.queryParams,self.client_id)
		assert result
	
	def test_wrongdata_editPeople(self):
		self.queryParams=["2147483648","nupura","abc","abhaurgfwAIEF","asuherguierhg","iuervgfiuaer","india","","26354262","348912736","","1000","","",""]
		'''if(self.queryParams[0]>2147483647 or type(self.queryParams[0])!='int' or self.queryParams[0]<0):
			print "invalid people code"
		else:'''
		result=self.server.people.editPeopleMaster(self.queryParams,self.client_id)
		assert result
	
	def test_multiple_editPeople(self):
		self.queryParams=["205","nupura","abc","abhaurgfwAIEF","asuherguierhg","iuervgfiuaer","india","","26354262","348912736","","1000","","",""]
	        i=0
		while i<2:
			result=self.server.people.editPeopleMaster(self.queryParams,self.client_id)
			assert result
			i=i+1
	
	def test_right_getPeopleDetails(self):
		self.queryParams=["206","nupuraw","Vendor/Supplier","malad","mumbai","400078","maharashtra","india","26354262","348912736","","1000","","",""]
		result=self.server.people.getPeopleMaster(self.queryParams,self.client_id)
		assert result
	
	def test_type_getPeopleDetails(self):
		self.queryParams=7654
		result=self.server.people.getPeopleMaster(self.queryParams,self.client_id)
		assert result
		
	def test_wrongdata_getPeopleDetails(self):
		self.queryParams=["2147483648","nupura","abc","abhaurgfwAIEF","asuherguierhg","iuervgfiuaer","india","","26354262","348912736","","1000","","",""]
		'''if(self.queryParams[0]>2147483647 or type(self.queryParams[0])!='int' or self.queryParams[0]<0):
			print "invalid people code"
		else:'''
		result=self.server.people.getPeopleMaster(self.queryParams,self.client_id)
		assert result
	def test_multiple_getPeopleDetails(self):
		self.queryParams=["207","abcd","Vendor/Supplier","malad","mumbai","400078","maharashtra","india","26354262","348912736","","1000","","",""]
		i=0
		while i<2:
			result=self.server.people.getPeopleMaster(self.queryParams,self.client_id)
			assert result
			i=i+1
	
	def test_right_getAllPeople(self):
		result=self.server.people.getAllPeople(self.client_id)
		assert result
		
	def test_type_getAllPeople(self):
		self.client=gfdg
		result=self.server.people.getAllPeople(self.client_id)
		assert result
	
	def test_wrongdata_getAllPeople(self):
		self.client_id=["-90","fdj"]
		for index in self.client_id:
			result=self.server.people.getAllPeople(index)
			assert result
			index=index+1
	
	def test_multiple_getAllPeople(self):
		i=0
		while i<2:
			result=self.server.people.getAllPeople(self.client_id)
			assert result
			i=i+1
	
	def test_right_getPeopleMaster(self):
		result=self.server.people.getPeopleMaster(self.client_id)
		assert result
		
	def test_type_getPeopleMaster(self):
		self.client_id=jhf
		result=self.server.people.getPeopleMaster(self.client_id)
		assert result
	
	def test_wrongdata_getPeopleMaster(self):
		self.client_id=["-75676","ytu"]
		for index in self.client_id:
			result=self.server.people.getPeopleMaster(index)
			assert result
			index=index+1
	def test_multiple_getPeopleMaster(self):
		i=0
		while i<2:
			result=self.server.people.getPeopleMaster(self.client_id)
			assert result
			i=i+1
	def test_right_getCountMaster(self):
		result=self.server.people.getCountMaster(self.client_id)
		assert result
	
	def test_type_getCountMaster(self):
		self.client_id=hgdhg
		result=self.server.people.getCountMaster(self.client_id)
		assert result
	
	def test_wrongdata_getCountMaster(self):
		self.client_id=["0","ytu"]
		for index in self.client_id:
			result=self.server.people.getCountMaster(index)
			assert result
			index=index+1
	
	def test_multiple_getCountMaster(self):
		i=0
		while i<2:
			result=self.server.people.getCountMaster(self.client_id)
			assert result
			i=i+1
	def test_right_getPeopleMasterById(self):
		self.queryParams=["209","nupura","abc","abhaurgfwAIEF","asuherguierhg","iuervgfiuaer","india","","26354262","348912736","","1000","","",""]
		result=self.server.people.getPeopleMasterById(self.queryParams,self.client_id)
		assert result
	
	def test_type_getPeopleMasterById(self):
		self.queryParams=6756
		result=self.server.people.getPeopleMasterById(self.queryParams,self.client_id)
		assert result
	
	def test_wrongdata_getPeopleMasterById(self):
		self.queryParams=["210","nupura","abc","abhaurgfwAIEF","asuherguierhg","iuervgfiuaer","india","","26354262","348912736","","1000","","",""]
		result=self.server.people.getPeopleMasterById(self.queryParams,self.client_id)
		assert result
	
	def test_multiple_getPeopleMasterId(self):
		self.queryParams=["210","nupura","abc","abhaurgfwAIEF","asuherguierhg","iuervgfiuaer","india","","26354262","348912736","","1000","","",""]
		i=0
		while i<2:
			result=self.server.people.getPeopleMasterById(self.queryParams,self.client_id)
			assert result
			i=i+1
	def tearDown(self):
		print "cleaning up test_people"

if __name__ == '__main__':
	import unittest
	unittest.main()	
