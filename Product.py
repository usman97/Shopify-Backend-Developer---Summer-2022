import json
'''
This Python class contains an Object Class to create different products object
and store their inventory information
'''

class Product:
    def __init__(self, sku, productName, dateCreated, inventoryAvailable, price, warehouseLocation):
        self.sku = sku
        self.productName = productName
        self.dateCreated = dateCreated
        self.inventoryAvailable = inventoryAvailable
        self.price = price
        self.warehouseLocation = warehouseLocation


    def getSku(self):
        return self.sku


    def getProductName(self):
        return self.productName


    def getDateCreated(self):
        return self.dateCreated

    def getInventoryAvailable(self):
        return self.inventoryAvailable

    def getPrice(self):
        return self.price

    def getWarehouseLocation(self):
        return self.warehouseLocation
