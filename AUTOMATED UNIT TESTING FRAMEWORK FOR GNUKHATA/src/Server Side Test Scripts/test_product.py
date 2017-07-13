import xmlrpclib
from twisted.trial import unittest             
from unittest import TestCase
from time import strftime
import xmlrpclib,datetime

class test_product(unittest.TestCase):
	
	'''SetUp method makes connection to server'''
	def setUp(self):
	
		print "setup"
		self.server = xmlrpclib.Server("http://localhost:7081", allow_none=True);
		self.dbname = ["testdb3","2003-04"]
		self.client_id = self.server.getConnection(self.dbname)
		self.queryParams1=['12','hat','12','hat hat','20','30','25','25']
		self.queryParams2=[]
		
		
	def test_right_setProduct(self):
		result = self.server.product.setProduct(self.queryParams1,self.queryParams2,self.client_id)
		assert result
		
	def test_type_setProduct(self):
		result = self.server.product.setProduct(self.queryParams1,self.queryParams2,self.client_id)
		self.failIf(type(result)!=bool)
		
	def test_wrongdata_setProduct(self):
		self.queryParams1=['','','','','','','','']
		self.queryParams2=[]
		result = self.server.product.setProduct(self.queryParams1,self.queryParams2,self.client_id)
		assert result

	def test_multi_setProduct(self):
		i=0
		while i<2:
			result = self.server.product.setProduct(self.queryParams1,self.queryParams2,self.client_id)
			assert result
			i=i+1

	def test_right_getAllProductName(self):
		result = self.server.product.getAllProductName(self.client_id)
		assert result
			
	def test_type_getAllProductName(self):
		result = self.server.product.getAllProductName(self.client_id)
		print result
		self.failIf(type(result)!=list)
		
	def test_multi_getAllProductName(self):
		i=0
		while i<2:
			result = self.server.product.getAllProductName(self.client_id)
			assert result
			i=i+1
			
	def test_wrongdata_getAllProductName(self):
		self.client_id=[]
		result = self.server.product.getAllProductName(self.client_id)
		assert result
	
	def test_right_getProductByCode(self):
		result = self.server.product.getProductByCode(self.queryParams1,self.client_id)
		assert result
		
	def test_type_getProductByCode(self):
		result = self.server.product.getProductByCode(self.queryParams1,self.client_id)
		self.failIf(type(result)!=list)
		
	def test_right_getProductByCode(self):
		i=0
		while i<2:
			result = self.server.product.getProductByCode(self.queryParams1,self.client_id)
			assert result
			i=i+1
			
	def test_wrongdata_getProductByCode(self):
		self.queryParams1=['','','','','','','','']
		result = self.server.product.getProductByCode(self.queryParams1,self.client_id)
		assert result
	
	def test_right_getProductByName(self):
		result = self.server.product.getProductByName(self.queryParams1,self.client_id)
		assert result
		
	def test_type_getProductByName(self):
		result = self.server.product.getProductByName(self.queryParams1,self.client_id)
		self.failIf(type(result)!=list)
		
	def test_multi_getProductByName(self):
		i=0
		while i<2:
			result = self.server.product.getProductByName(self.queryParams1,self.client_id)
			assert result
			i=i+1

	def test_wrongdata_getProductByName(self):
		self.queryParams1=['','','','','','','','']
		result = self.server.product.getProductByName(self.queryParams1,self.client_id)
		assert result
		
	def test_right_editProduct(self):
		self.queryParams1=['12','hat','12','hat hat','20','25','25','25']
		self.queryParams2=[]
		result = self.server.product.editProduct(self.queryParams1,self.queryParams2,self.client_id)
		assert result
		
	def test_type_editProduct(self):
		self.queryParams1=['12','hat','12','hat hat','20','25','25','25']
		self.queryParams2=[]
		result = self.server.product.editProduct(self.queryParams1,self.queryParams2,self.client_id)
		self.failIf(type(result)!=bool)
		
	def test_multi_editProduct(self):
		self.queryParams1=['12','hat','12','hat hat','20','25','25','25']
		self.queryParams2=[]
		i=0
		while i<2:
			result = self.server.product.editProduct(self.queryParams1,self.queryParams2,self.client_id)
			assert result	
			i=i+1
			
	def test_wrongdata_editProductByName(self):	
		self.queryParams1=['','','','','','','','']
		self.queryParams2=[]
		result = self.server.product.editProduct(self.queryParams1,self.queryParams2,self.client_id)
		assert result	
	
	def test_right_getPurchaseProductDetails(self):
		result = self.server.product.getPurchaseProductDetails(self.queryParams1,self.client_id)
		assert result
		
	def test_type_getPurchaseProductDetails(self):
		result = self.server.product.getPurchaseProductDetails(self.queryParams1,self.client_id)
		self.failIf(type(result)!=list)
		
	def test_multi_getPurchaseProductDetails(self):
		i=0
		while i<2:
			result = self.server.product.getPurchaseProductDetails(self.queryParams1,self.client_id)
			assert result
			i=i+1
			
	def test_wrongdata_getPurchaseProductDetails(self):
		self.queryParams1=['','','','','','','','']
		result = self.server.product.getPurchaseProductDetails(self.queryParams1,self.client_id)
		assert result
	

	def test_right_getSaleProductDetails(self):
		result = self.server.product.getSaleProductDetails(self.queryParams1,self.client_id)
		assert result
		
	def test_type_getSaleProductDetails(self):
		result = self.server.product.getSaleProductDetails(self.queryParams1,self.client_id)
		self.failIf(type(result)!=list)
		
	def test_multi_getSaleProductDetails(self):
		i=0
		while i<2:
			result = self.server.product.getSaleProductDetails(self.queryParams1,self.client_id)
			assert result	
			i=i+1
	
	def test_wrongdata_getSaleProductDetails(self):
		self.queryParams1=['','','','','','','','']
		result = self.server.product.getSaleProductDetails(self.queryParams1,self.client_id)
		assert result

	def test_right_getAllProductCode(self):
		result = self.server.product.getAllProductCode(self.client_id)
		assert result
		
	def test_type_getAllProductCode(self):
		result = self.server.product.getAllProductCode(self.client_id)
		self.failIf(type(result)!=list)
	
	def test_multi_getAllProductCode(self):
		i=0
		while i<2:
			result = self.server.product.getAllProductCode(self.client_id)
			assert result	
			i=i+1
			
	def test_wrongdata_getAllProductCode(self):
		self.client_id=[]
		result = self.server.product.getAllProductCode(self.client_id)
		assert result

	def test_right_getOpeningQuantity(self):
		result = self.server.product.getOpeningQuantity(self.client_id)
		assert result
		
	def test_type_getOpeningQuantity(self):
		result = self.server.product.getOpeningQuantity(self.client_id)
		self.failIf(type(result)!=list)
		
	def test_multi_getOpeningQuantity(self):
		i=0
		while i<2:
			result = self.server.product.getOpeningQuantity(self.client_id)
			assert result
			i=i+1

	def test_wrongdata_getOpeningQuantity(self):
		self.client_id=[]s
		result = self.server.product.getOpeningQuantity(self.client_id)
		assert result
		
	def test_right_getOpeningQuantityByProduct(self):
		result = self.server.product.getOpeningQuantityByProduct(self.queryParams1,self.client_id)
		assert result
		
	def test_type_getOpeningQuantityByProduct(self):
		result = self.server.product.getOpeningQuantityByProduct(self.queryParams1,self.client_id)
		self.failIf(type(result)!=list)
		
	def test_multi_getOpeningQuantityByProduct(self):
		i=0
		while i<2:
			result = self.server.product.getOpeningQuantityByProduct(self.queryParams1,self.client_id)
			assert result
			i=i+1
	def test_wrongdata_getOpeningQuantityByProduct(self):
		self.queryParams1=['','','','','','','','']
		result = self.server.product.getOpeningQuantityByProduct(self.queryParams1,self.client_id)
		assert result

		
	def test_right_getStockByProduct(self):
		result = self.server.product.getStockByProduct(self.queryParams1,self.client_id)
		assert result	
		
	def test_type_getStockByProduct(self):
		result = self.server.product.getStockByProduct(self.queryParams1,self.client_id)
		self.failIf(type(result)!=list)
		
	def test_multi_getStockByProduct(self):
		i=0
		while i<2:
			result = self.server.product.getStockByProduct(self.queryParams1,self.client_id)
			assert result
			i=i+1
			
	def test_wrongdata_getStockByProduct(self):
		self.queryParams1=['','','','','','','','']
		result = self.server.product.getStockByProduct(self.queryParams1,self.client_id)
		assert result	

	def test_right_getOpeningStock(self):
		result = self.server.product.getOpeningStock(self.client_id)
		assert result	
		
	def test_type_getOpeningStock(self):
		result = self.server.product.getOpeningStock(self.client_id)
		self.failIf(type(result)!=list)
		
	def test_multi_getOpeningStock(self):
		i=0
		while i<2:
			result = self.server.product.getOpeningStock(self.client_id)
			assert result	
			i=i+1
			
	def test_wrongdata_getOpeningStock(self):
		self.client_id=[]
		result = self.server.product.getOpeningStock(self.client_id)
		assert result	

	def test_right_getAllStock(self):
		result = self.server.product.getAllStock(self.client_id)
		assert result		
		
	def test_type_getAllStock(self):
		result = self.server.product.getAllStock(self.client_id)
		self.failIf(type(result)!=list)
		
	def test_multi_getAllStock(self):
		i=0
		while i<2:
			result = self.server.product.getAllStock(self.client_id)
			assert result			
			i=i+1

	def test_wrongdata_getAllStock(self):
		self.client_id=[]
		result = self.server.product.getAllStock(self.client_id)
		assert result	
			
	def test_right_getSaledProductByDate(self):
		result = self.server.product.getSaledProductByDate(self.queryParams1,self.client_id)
		assert result
			
	def test_type_getSaledProductByDate(self):
		result = self.server.product.getSaledProductByDate(self.queryParams1,self.client_id)
		self.failIf(type(result)!=list)		
			
	def test_multi_getSaledProductByDate(self):
		i=0
		while i<2:
			result = self.server.product.getSaledProductByDate(self.queryParams1,self.client_id)
			assert result	
			i=i+1
			
	def test_wrongdata_getSaledProductByDate(self):
		self.queryParams1=[]
		result = self.server.product.getSaledProductByDate(self.queryParams1,self.client_id)
		assert result

	def test_right_getAllSaledProducts(self):
		result = self.server.product.getAllSaledProducts(self.queryParams1,self.client_id)
		assert result
		
	def test_type_getAllSaledProducts(self):
		result = self.server.product.getAllSaledProducts(self.queryParams1,self.client_id)
		self.failIf(type(result)!=list)	
		
	def test_multi_getAllSaledProducts(self):
		i=0
		while i<2:
			result = self.server.product.getAllSaledProducts(self.queryParams1,self.client_id)
			assert result	
			i=i+1
		
	def test_wrongdata_getAllSaledProducts(self):
		self.queryParams1=[]
		result = self.server.product.getAllSaledProducts(self.queryParams1,self.client_id)
		assert result	
			
	'''tearDown closes the connection.'''	
	def tearDown(self):
		print "We are in tearDown"
		self.server.closeConnection(self.client_id)
			
if __name__ == '__main__':
		import unittest
		unittest.main()
