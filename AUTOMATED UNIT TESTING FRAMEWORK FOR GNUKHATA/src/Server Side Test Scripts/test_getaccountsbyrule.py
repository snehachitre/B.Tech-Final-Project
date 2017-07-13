import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
import xmlrpclib,datetime

class test_getaccountsbyrule(unittest.TestCase):

    def setUp(self):        
        print "setup"
        self.server = xmlrpclib.Server("http://localhost:7081");
        self.dbname = ["testdb3","2003-04"]
        self.client_id = self.server.getConnection(self.dbname)
        self.today_date = datetime.date.today().strftime('%Y-%m-%d')


    def test_right_getContraAccounts(self):        
        result=self.server.getaccountsbyrule.getContraAccounts(self.client_id)
        assert result
        
    def test_type_getContraAccounts(self):
        result=self.server.getaccountsbyrule.getContraAccounts(self.client_id)
        self.failIf(type(result)!=list)
        
    def test_wrongdata_getContraAccounts(self):
        self.client_id=[-56,"dhgdhy"]
        for index in self.client_id
            result=self.server.getaccountsbyrule.getContraAccounts(index)
            assert result
            index=index+1
        
    def test_multiple_getContraAccounts(self):
        i=0
        while i<2:
            result=self.server.getaccountsbyrule.getContraAccounts(self.client_id)
            assert result
            i=i+1
        
    def test_right_getReceivableAccounts(self):
        self.queryParams=["cr"]
        result=self.server.getaccountsbyrule.getReceivableAccounts(self.queryParams,self.client_id)
        assert result

    def test_type_getReceivableAccounts(self):
        self.queryParams=["cr"]
        result=self.server.getaccountsbyrule.getReceivableAccounts(self.queryParams,self.client_id)
        self.failIf(type(result)!=list)

    def test_wrongdata_getReceivableAccounts(self):
        self.queryParams=[""]
        result=self.server.getaccountsbyrule.getReceivableAccounts(self.queryParams,self.client_id)
        assert result

    def test_multiple_getReceivableAccounts(self):
        self.queryParams=["cr"]
        i=0
        while i<2:
            result=self.server.getaccountsbyrule.getReceivableAccounts(self.queryParams,self.client_id)
            assert result
            i=i+1
    
    def test_right_getPaymentAccounts(self):
        self.queryParams=["dr"]
        result=self.server.getaccountsbyrule.getPaymentAccounts(self.queryParams,self.client_id)
        assert result
        
    def test_type_getPaymentAccounts(self):
        self.queryParams=["dr"]
        result=self.server.getaccountsbyrule.getPaymentAccounts(self.queryParams,self.client_id)
        self.failIf(type(result)!=list))
        
    def test_wrongdata_getPaymentAccounts(self):
        self.queryParams=[""]
        result=self.server.getaccountsbyrule.getPaymentAccounts(self.queryParams,self.client_id)
        assert result
        
    def test_multiple_getPaymentAccounts(self):
        self.queryParams=["dr"]
        i=0
        while i<2:
            result=self.server.getaccountsbyrule.getPaymentAccounts(self.queryParams,self.client_id)
            assert result
            i=i+1
            
    def test_right_getJournalAccounts(self):
        result=self.server.getaccountsbyrule.getJournalAccounts(self.client_id)
        assert result

    def test_type_getJournalAccounts(self):
        result=self.server.getaccountsbyrule.getJournalAccounts(self.client_id)
        self.failIf(type(result)!=list)
        
    def test_wrongdata_getJournalAccounts(self):
        self.client_id=[-56,"dhgdhy"]
        for index in self.client_id
            result=self.server.getaccountsbyrule.getJournalAccounts(self.client_id)
            assert result
            index=index+1
            
    def test_multiple_getJournalAccounts(self):
        i=0
        while i<2:
            result=self.server.getaccountsbyrule.getJournalAccounts(self.client_id)
            assert result
            i=i+1
            
    def tearDown(self):
        print "cleaning up test_salesreturn"
        self.server.closeConnection(self.client_id)

if __name__ == '__main__':
    import unittest
    unittest.main() 
