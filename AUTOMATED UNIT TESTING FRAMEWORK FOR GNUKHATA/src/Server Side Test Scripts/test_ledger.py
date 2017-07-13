'''Contributors: "Sonal Dolas"<ssonaldd@gmail.com>
	      "Sneha Chitre"<csadhana27@gmail.com>
	      "Nupura Walawalkar"<greatnups@gmail.com>'''
	
import xmlrpclib
import unittest             
from unittest import TestCase

		
class test_ledger(unittest.TestCase):

	'''SetUp method makes connection to server'''
	def setUp(self):
		self.server = xmlrpclib.Server("http://localhost:7081")
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.queryParams_ledger=['2006-12-18','12','12','200000.50']
		self.vouchertype=['Purchase Bill']
		self.vouchercode=['12']
		
	def test_right_setLedger(self):
		result=self.server.ledger.setLedger(self.queryParams_ledger, self.vouchertype, self.client_id)
		assert result
		
	def test_type_setLedger(self):
		result=self.server.ledger.setLedger(self.queryParams_ledger, self.vouchertype, self.client_id)
		self.failIf(type(result)!=bool)	
		
	def test_multi_setLedger(self):
		i=0
		while i<2:
			result=self.server.ledger.setLedger(self.queryParams_ledger, self.vouchertype, self.client_id)
			assert result
			i=i+1

	def test_wrongdata_setLedger(self):
		self.queryParams_ledger=['','','','']
		self.vouchertype=['']
		result=self.server.ledger.setLedger(self.queryParams_ledger, self.vouchertype, self.client_id)
		assert result
			
	def test_right_getDetailsByLedger(self):
		result=self.server.ledger.getDetailsByLedger(self.queryParams_ledger,self.client_id)
		assert result
		
	def test_type_getDetailsByLedger(self):
		result=self.server.ledger.getDetailsByLedger(self.queryParams_ledger,self.client_id)	
		self.failIf(type(result)!=list)
		
	def test_multi_getDetailsByLedger(self):
		i=0
		while i<2:
			result=self.server.ledger.getDetailsByLedger(self.queryParams_ledger,self.client_id)
			assert result	
			i=i+1

	def test_wrong_getDetailsByLedger(self):
		self.queryParams_ledger=['','','','']
		result=self.server.ledger.getDetailsByLedger(self.queryParams_ledger,self.client_id)
		assert result
		
		
	def test_right_getDetailsOfSundryDebtors(self):
		self.queryParams=['Sales']
		result=self.server.ledger.getDetailsOfSundryDebtors(self.queryParams,self.client_id)
		assert result
		
	def test_type_getDetailsOfSundryDebtors(self):
		self.queryParams=['Sales']
		result=self.server.ledger.getDetailsOfSundryDebtors(self.queryParams,self.client_id)
		self.failIf(type(result)!=list)
		
	def test_multi_getDetailsOfSundryDebtors(self):
		self.queryParams=['Sales']
		i=0
		while i<0:
			result=self.server.ledger.getDetailsOfSundryDebtors(self.queryParams,self.client_id)
			assert result
			i=i+1
		
	def test_wrongdata_getDetailsOfSundryDebtors(self):
		self.queryParams=['']
		result=self.server.ledger.getDetailsOfSundryDebtors(self.queryParams,self.client_id)
		assert result

	def test_right_getDetailsOfSundryCreditors(self):
		self.queryParams=['Sales']
		result=self.server.ledger.getDetailsOfSundryCreditors(self.queryParams,self.client_id)
		assert result	
		
	def test_type_getDetailsOfSundryCreditors(self):
		self.queryParams=['Sales']
		result=self.server.ledger.getDetailsOfSundryCreditors(self.queryParams,self.client_id)
		self.failIf(type(result)!=list)
		
	def test_multi_getDetailsOfSundryCreditors(self):
		self.queryParams=['Sales']
		i=0
		while i<0:
			result=self.server.ledger.getDetailsOfSundryCreditors(self.queryParams,self.client_id)
			assert result	
			i=i+1
			
	def test_wrongdata_getDetailsOfSundryCreditors(self):
		self.queryParams=['']
		result=self.server.ledger.getDetailsOfSundryCreditors(self.queryParams,self.client_id)
		assert result

	def test_right_getDetailsByLedgerInDate(self):
		self.queryParams=['Sales','2011-01-25']
		result=self.server.ledger.getDetailsByLedgerInDate(self.queryParams,self.client_id)
		assert result	
		
	def test_type_getDetailsByLedgerInDate(self):
		self.queryParams=['Sales','2011-01-25']
		result=self.server.ledger.getDetailsByLedgerInDate(self.queryParams,self.client_id)	
		self.failIf(type(result)!=list)
		
	def test_multi_getDetailsByLedgerInDate(self):
		self.queryParams=['Sales','2011-01-25']
		i=0
		while i<2:
			result=self.server.ledger.getDetailsByLedgerInDate(self.queryParams,self.client_id)
			assert result	
			i=i+1
	
	def test_wrongdata_getDetailsByLedgerInDate(self):
		self.queryParams=['','']
		result=self.server.ledger.getDetailsByLedgerInDate(self.queryParams,self.client_id)
		assert result	

	def test_right_getGeneralLedger(self):
		self.queryParams=[]
		result=self.server.ledger.getGeneralLedger(self.queryParams,self.client_id)
		assert result	
		
	def test_type_getGeneralLedger(self):
		self.queryParams=[]
		result=self.server.ledger.getGeneralLedger(self.queryParams,self.client_id)
		self.failIf(type(result)!=list)
		
	def test_multi_getGeneralLedger(self):
		self.queryParams=[]
		i=0
		while i<2:
			result=self.server.ledger.getGeneralLedger(self.queryParams,self.client_id)
			assert result	
			i=i+1
	
	def test_wrongdata_getGeneralLedger(self):
		self.queryParams=[]
		result=self.server.ledger.getGeneralLedger(self.queryParams,self.client_id)
		assert result	
	
	def test_right_getGeneralReportIncome(self):
		self.queryParams=[]
		result=self.server.ledger.getGeneralReportIncome(self.queryParams,self.client_id)
		assert result		
		
	def test_type_getGeneralReportIncome(self):
		self.queryParams=[]
		result=self.server.ledger.getGeneralReportIncome(self.queryParams,self.client_id)
		self.failIf(type(result)!=list)
		
	def test_multi_getGeneralReportIncome(self):
		self.queryParams=[]
		i=0
		while i<2:
			result=self.server.ledger.getGeneralReportIncome(self.queryParams,self.client_id)
			assert result		
			i=i+1
		
	def test_wrongdata_getGeneralReportIncome(self):
		self.queryParams=[]
		result=self.server.ledger.getGeneralReportIncome(self.queryParams,self.client_id)
		assert result	

	def test_right_getGeneralReportExpense(self):
		self.queryParams=[]
		result=self.server.ledger.getGeneralReportExpense(self.queryParams,self.client_id)
		assert result		
			
	def test_type_getGeneralReportExpense(self):
		self.queryParams=[]
		result=self.server.ledger.getGeneralReportExpense(self.queryParams,self.client_id)
		self.failIf(type(result)!=list)
		
	def test_multi_getGeneralReportExpense(self):
		self.queryParams=[]
		i=0
		while i<2:
			result=self.server.ledger.getGeneralReportExpense(self.queryParams,self.client_id)
			assert result	
			i=i+1	
		
	def test_wrongdata_getGeneralReportExpense(self):
		self.queryParams=[]
		result=self.server.ledger.getGeneralReportExpense(self.queryParams,self.client_id)
		assert result

	def test_right_getGeneralReport(self):
		self.queryParams=[]
		result=self.server.ledger.getGeneralReport(self.queryParams,self.client_id)
		assert result	
		
	def test_type_getGeneralReport(self):
		self.queryParams=[]
		result=self.server.ledger.getGeneralReport(self.queryParams,self.client_id)	
		self.failIf(type(result)!=list)
		
	def test_multi_getGeneralReport(self):
		self.queryParams=[]
		i=0
		while i<2:
			result=self.server.ledger.getGeneralReport(self.queryParams,self.client_id)
			assert result	
			i=i+1
	
	def test_wrong_getGeneralReport(self):
		self.queryParams=[]
		result=self.server.ledger.getGeneralReport(self.queryParams,self.client_id)
		assert result

	def test_right_editLedger(self):
		self.queryParams_ledger=['2006-12-18' ,'12','12','50000']
		self.vouchertype=['Purchase Bill']
		result=self.server.ledger.editLedger(self.queryParams_ledger,self.vouchertype,self.client_id)
		assert result	
		
	def test_type_editLedger(self):
		self.queryParams_ledger=['2006-12-18' ,'12','12','50000']
		self.vouchertype=['Purchase Bill']
		result=self.server.ledger.editLedger(self.queryParams_ledger,self.vouchertype,self.client_id)
		self.failIf(type(result)!=bool)		
		
	def test_multi_editLedger(self):
		self.queryParams_ledger=['2006-12-18' ,'12','12','50000']
		self.vouchertype=['Purchase Bill']
		i=0
		while i<2:
			result=self.server.ledger.editLedger(self.queryParams_ledger,self.vouchertype,self.client_id)
			assert result	
			i=i+1


	def test_wrong_editLedger(self):
		self.queryParams_ledger=['2006-12-18' ,'12','12','50000']
		self.vouchertype=['Purchase Bill']
		result=self.server.ledger.editLedger(self.queryParams_ledger,self.vouchertype,self.client_id)
		assert result	

'''tearDown closes the connection.'''	
	def tearDown(self):
		print "cleaning up test_debitnotevoucher"

if __name__ == '__main__':
	import unittest
	unittest.main()	
