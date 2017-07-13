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
        self.queryParams=["1","Corpus","Reserve","2000.50"]
        result=self.server.groups.setGroups(self.queryParams,self.client_id)
        assert result
        
    def test_type_setGroups(self):
        self.queryParams=["2","Current Asset","Bank","2000"]
        result=self.server.groups.setGroups(self.queryParams,self.client_id)
        self.failIf(type(result)!=bool)
        
    def test_wrongdata_setGroups(self):     
        self.queryParams=["12","Direct Income","","7800.507"]
        result=self.server.groups.setGroups(self.queryParams,self.client_id)
        assert result
    
    def test_multiple_setGroups(self):
        self.queryParams=["3","Current Asset","Cash","4000"]
        i=0
        while i<3:
            result=self.server.groups.setGroups(self.queryParams,self.client_id)
            assert result
            i=i+1

'''---------------------------------------------------------------------------------------'''

    def test_right_getGroupByCode(self):        
        self.queryParams=["2","Current Asset","Bank","2000"]
        result=self.server.groups.getGroupByCode(self.queryParams,self.client_id)
        assert result
    
    def test_type_getGroupByCode(self):     
        self.queryParams=["3","Current Asset","Cash","4000"]
        result=self.server.groups.getGroupByCode(self.queryParams,self.client_id)
        self.failIf(type(result)!=list)
    
    def test_wrongdata_getGroupByCode(self):        
        self.queryParams=["0","Current Asset","Cash","4000"]
        result=self.server.groups.getGroupByCode(self.queryParams,self.client_id)
        assert result
    
    def test_multiple_getGroupByCode(self):     
        self.queryParams=["3","Current Asset","Cash","4000"]
        i=0
        while i<2:
            result=self.server.groups.getGroupByCode(self.queryParams,self.client_id)
            assert result
            i=i+1
            
'''---------------------------------------------------------------------------------------'''            

    def test_right_getAllGroups(self):      
        result=self.server.groups.getAllGroup(self.client_id)
        assert result
    
    def test_type_getAllGroups(self):       
        result=self.server.groups.getAllGroups(self.client_id)
        self.failIf(type(result)!=list)
        
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
            
'''---------------------------------------------------------------------------------------'''            

    def test_right_updatGroupBalance(self):     
        self.queryParams=["3","Current Asset","Inventory","2000"]
        result=self.server.groups.updateGroupBalance(self.queryParams,self.client_id)
        assert result
        
    def test_type_updateGroupBalance(self):     
        self.queryParams=["3","Current Asset","Loans & Advance","3000"]
        result=self.server.groups.updateGroupBalance(self.queryParams,self.client_id)
        self.failIf(type(result)!=bool)
        
        
    def test_wrongdata_updateGroupBalance(self):        
        self.queryParams=["","Indirect Expense","","2000.50"]
        result=self.server.groups.updateGroupBalance(self.queryParams,self.client_id)
        assert result
    
    def test_multiple_updateGroupBalance(self):     
        self.queryParams=["3","Current Asset","Sundry Debtors","3000"]
        i=0
        while i<2:
            result=self.server.groups.updateGroupBalance(self.queryParams,self.client_id)
            assert result
            i=i+1
            
'''---------------------------------------------------------------------------------------'''            

    def test_right_getCrOpeningBalance(self):
        result=self.server.groups.getCrOpeningBalance(self.client_id)
        assert result

    def test_type_getCrOpeningBalance(self):
        result=self.server.groups.getCrOpeningBalance(self.client_id)
        self.failIf(type(result)!=list)

    def test_wrongdata_getCrOpeningBalance(self):
        self.client_id=[-6,0,"abc"]
        for index in self.queryParams
                result=self.server.groups.getCrOpeningBalance(index)
                assert result
                index=index+1

    def test_multiple_getCrOpeningBalance(self):
        i=0
        while i<2:
                result=self.server.groups.getCrOpeningBalance(index)
                assert result
                i=i+1
                
'''---------------------------------------------------------------------------------------'''                        

    def test_right_getDrOpeningBalance(self):
        result=self.server.groups.getDrOpeningBalance(index)
        assert result
                
    def test_type_getDrOpeningBalance(self):
        result=self.server.groups.getDrOpeningBalance(self.client_id)
        self.failIf(type(result)!=list)

    def test_wrongdata_getDrOpeningBalance(self):
        self.client_id=[-6,0,"abc"]
        for index in self.queryParams
                result=self.server.groups.getDrOpeningBalance(index)
                assert result
                index=index+1

    def test_multiple_getDrOpeningBalance(self):
        i=0
        while i<2:
                result=self.server.groups.getDrOpeningBalance(index)
                assert result
                i=i+1
'''---------------------------------------------------------------------------------------'''

    def test_right_getGroupByName(self):        
        self.queryParams=["2","Current Asset","Bank","2000.50"]
        result=self.server.groups.getGroupByName(self.queryParams,self.client_id)
        assert result
        
    def test_type_getGroupByName(self):    
        self.queryParams=["2","Current Asset","Bank","2000.50"]
        result=self.server.groups.getGroupByName(self.queryParams,self.client_id)
        self.failIf(type(result)!=bool)
        
    def test_wrongdata_getGroupByName(self):    
        self.queryParams=["20","Current Asset","Bank","2000.50"]
        result=self.server.groups.getGroupByName(self.queryParams,self.client_id)
        assert result
        
    def test_multiple_getGroupByName(self):        
        self.queryParams=["2","Current Asset","Bank","2000.50"]
        i=0
        while i<2:
            result=self.server.groups.getGroupByName(self.queryParams,self.client_id)
            assert result
            i=i+1
            
'''---------------------------------------------------------------------------------------'''            

    def test_right_getGroupCodeByName(self):
        self.queryParams=["Current Asset"]
        result=self.server.groups.getGroupCodeByName(self.queryParams,self.client_id)       
        assert result
        
    def test_type_getGroupCodeByName(self):
        self.queryParams=["Current Asset"]
        result=self.server.groups.getGroupCodeByName(self.queryParams,self.client_id)       
        self.failIf(type(result)!=int)
        
    def test_wrongdata_getGroupCodeByName(self):
        result=self.server.groups.getGroupCodeByName(self.queryParams,self.client_id)       
        assert result

    def test_multiple_getGroupCodeByName(self):
        self.queryParams=["Current Asset"]
        i=0
        while i<2:
                result=self.server.groups.getGroupCodeByName(self.queryParams,self.client_id)       
                assert result
                i=i+1
        
'''---------------------------------------------------------------------------------------'''                

    def test_right_editGroups(self):        
        self.queryParams=["2","Current Asset","Sundry Debtors","1000"]
        result=self.server.groups.editGroups(self.queryParams,self.client_id)
        assert result
    
    def test_type_editGroups(self):
    
        self.queryParams=["2","Current Asset","Sundry Debtors","800"]
        result=self.server.groups.editGroups(self.queryParams,self.client_id)
        self.failIf(type(result)!=bool) 
        
    def test_wrongdata_editGroups(self):
    
        self.queryParams=["20","Current Asset","Sundry Debtors",""]
        result=self.server.groups.editGroups(self.queryParams,self.client_id)
        assert result
    
    def test_multiple_editGroups(self):
        
        self.queryParams=["2","Current Asset","Sundry Debtors","700"]
        i=0
        while i<2:
            result=self.server.groups.editGroups(self.queryParams,self.client_id)
            assert result
            i=i+1
            
'''---------------------------------------------------------------------------------------'''            

    def test_right_getGroupNames(self):        
        result=self.server.groups.getGroupNames(self.client_id)
        assert result
    
    def test_type_getGroupNames(self):        
        result=self.server.groups.getGroupNames(self.client_id)
        self.failIf(type(result)!=list)
    
    def test_wrongdata_getGroupNames(self):        
        self.client_id=["-987432","sdfg",""]
        for index in self.client_id:
            result=self.server.groups.getGroupNames(self.client_id)
            assert result
    
    def test_multiple_getGroupNames(self):
        i=0
        while i<2:
            result=self.server.groups.getGroupNames(self.client_id)
            assert result
            i=i+1

'''---------------------------------------------------------------------------------------'''        

    def test_right_getGroupNameByAccountName(self):        
        self.queryParams=["gnukhata"]
        result=self.server.groups.getGroupNames(self.client_id)
        assert result
    
    def test_type_getGroupNameByAccountName(self):    
        self.queryParams=["gnukhata"]
        result=self.server.groups.getGroupNameByAccountName(self.queryParams,self.client_id)
        self.failIf(type(result)!=str)
        
    def test_wrongdata_getGroupNameByAccountName(self):    
        self.queryParams=["xyz"]
        result=self.server.groups.getGroupNameByAccountName(self.queryParams,self.client_id)
        assert result
        
    def test_multiple_getGroupNameByAccountName(self):    
        self.queryParams=["gnukhata"]
        i=0
        while i<2:
            result=self.server.groups.getGroupNames(self.client_id)
            assert result
            i=i+1

'''---------------------------------------------------------------------------------------'''

    def test_right_getSubGroupByGroup(self):
        self.queryParams=["Fixed Asset"]
        result=self.server.groups.getSubGroupByGroup(self.queryParams,self.client_id)
        assert result
        
    def test_type_getSubGroupByGroup(self):
        self.queryParams=["Fixed Asset"]
        result=self.server.groups.getSubGroupByGroup(self.queryParams,self.client_id)
        self.failIf(type(result)!=str)

    def test_wrongdata_getSubGroupByGroup(self):
        self.queryParams=[""]
        result=self.server.groups.getSubGroupByGroup(self.queryParams,self.client_id)
        assert result

    def test_multiple_getSubGroupByGroup(self):
        self.queryParams=["Investment in Bank Deposits"]
        result=self.server.groups.getSubGroupByGroup(self.queryParams,self.client_id)
        assert result

'''---------------------------------------------------------------------------------------'''

    def test_right_getSubGroupByName(self):
        self.queryParams=["Inventory"]
        result=self.server.groups.getSubGroupByName(self.queryParams,self.client_id)
        assert result
        
    def test_type_getSubGroupByName(self):
        self.queryParams=["Inventory"]    
        result=self.server.groups.getSubGroupByName(self.queryParams,self.client_id)
        self.failIf(type(result)!=list)
        
    def test_wrongdata_getSubGroupByName(self):
        self.queryParams=[""]
        result=self.server.groups.getSubGroupByName(self.queryParams,self.client_id)
        assert result
        
    def test_multiple_getSubGroupByName(self):
        self.queryParams=["Building"]
        i=0
        while i<2:
                result=self.server.groups.getSubGroupByName(self.queryParams,self.client_id)
                assert result
                i=i+1
                
'''---------------------------------------------------------------------------------------'''

    def test_right_getSubGroupsByGroup(self):
        self.queryParams=["Current Liability"]
        result=self.server.groups.getSubGroupByName(self.queryParams,self.client_id)
        assert result
        
    def test_type_getSubGroupsByGroup(self):
        self.queryParams=["Investment"]
        result=self.server.groups.getSubGroupByName(self.queryParams,self.client_id)
        self.failIf(type(result)!=list)
        
    def test_wrongdata_getSubGroupsByGroup(self):
        self.queryParams=[""]
        result=self.server.groups.getSubGroupByName(self.queryParams,self.client_id)
        assert result
        
    def test_multiple_getSubGroupsByGroup(self):
        self.queryParams=["Fixed Asset"]
        result=self.server.groups.getSubGroupByName(self.queryParams,self.client_id)
        assert result
        
    def tearDown(self):
        print "cleaning up test_groups"

if __name__ == '__main__':
    import unittest
    unittest.main() 
