import json
import random
import string
import Product as test



'''
READ DATA FROM JSON FILE
'''

def readEntireInventoryData():
    #open Json File
    fileName = "./Data/inventory.json"

    #reads entire data in JSON
    with open(fileName, 'r') as file:
      data = json.load(file)

    
    return data

'''
CREATE DATA FOR Products class and update JSON FILE
'''

def createInventoryData(productName, dateCreated, inventoryAvailable, price, warehouseLocation):

    #Local method to generate random SKU for product
    sku = generateSKU()
    #create object of Product class
    product1 = test.Product(sku, productName, dateCreated, inventoryAvailable, price, warehouseLocation)

    #convert Product Object into json
    x = {
            "sku": product1.getSku(),
            "productName": product1.getProductName(),
            "dateCreated": product1.getDateCreated(),
            "inventoryAvailable": product1.getInventoryAvailable(),
            "price": product1.getPrice(),
            "warehouseLocation": product1.getWarehouseLocation()
            }
 
    #readCurrentInventoryData
    data = readEntireInventoryData()

    #appendNewDataInJSON
    data.append(x)

    fileName1 = "./Data/inventory.json"
    #Save new Product Data to inventory.json file
    with open(fileName1, 'w') as file1:
      json.dump(data, file1, indent=4)

    print(data)
    return data


'''
UPDATE DATA FOR Products in JSON FILE
'''
def updateInventoryData(sku,productName, dateCreated, inventoryAvailable, price, warehouseLocation):
    data = readEntireInventoryData()
    skuHashmap = {}

    for i in data:
        if i["sku"] not in skuHashmap:
            skuHashmap[i["sku"]] = 1

    if sku not in skuHashmap:
        return "Invalid Entry: sku is not in inventory"
    else:
        position = list(skuHashmap).index(sku)
        print(position)
    
        data[position]['productName'] = productName
        data[position]['dateCreated'] = dateCreated
        data[position]['inventoryAvailable'] = inventoryAvailable
        data[position]['price'] = price
        data[position]['warehouseLocation'] = warehouseLocation

        fileName1 = "./Data/inventory.json"
        #Save new Product Data to inventory.json file
        with open(fileName1, 'w') as file1:
          json.dump(data, file1, indent=4)
          
    print(data)
    return data


'''
REMOVE DATA FOR Products in JSON FILE
'''
def removeInventoryData(sku):
    data = readEntireInventoryData()
    skuHashmap = {}

    for i in data:
        if i["sku"] not in skuHashmap:
            skuHashmap[i["sku"]] = 1

    if sku not in skuHashmap:
        return "Invalid Entry: sku is not in inventory"
    else:
        position = list(skuHashmap).index(sku)
        print(position)

        
        data.pop(position)

        fileName1 = "./Data/inventory.json"
        #Save new Product Data to inventory.json file
        with open(fileName1, 'w') as file1:
          json.dump(data, file1, indent=4)
          
    print(data) 
    return data   
def generateSKU():
    skuHashmap = {}
    
    #read Json File
    data = readEntireInventoryData()

    #Iterate the JSON data and saves SKU data in a Hashmap
    for i in data:
        if i["sku"] not in skuHashmap:
            skuHashmap[i["sku"]] = 1


    #Generating a SKU ID and ensuring no duplicates are in JSON File
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(6)))
    
    if result_str not in skuHashmap:
        return result_str

    else:
        while result_str in skuHashmap:
            result_str = ''.join((random.choice(source) for i in range(6)))
            
        return result_str

            


            
    
