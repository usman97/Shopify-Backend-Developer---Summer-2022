from flask import Flask, render_template, request, send_file
import CURD
import json
import jsonToCsv
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html")

'''
@app.route("/result", methods = ['POST', "GET"])
def result():
	output = request.form.to_dict()
	name = output["name"]

	return render_template("result.html", name = name)
'''
@app.route("/displayData")
def displayData():
	data = CURD.readEntireInventoryData()

	return render_template("displayData.html", data = json.dumps(data, indent = 4))

@app.route("/addInventory")
def addInventory():
	return render_template("addInventory.html")

@app.route("/newInventory", methods = ['POST', "GET"])
def newInventory():
	output = request.form.to_dict()
	print(output)
	productName = output["productName"]
	dateCreated = output["dateCreated"]
	inventoryAvailable = output["inventoryAvailable"]
	price = output["price"]
	warehouseLocation = output["warehouseLocation"]
	
	data = CURD.createInventoryData(productName, dateCreated, inventoryAvailable, price, warehouseLocation)
	
	return render_template("newInventory.html", data1 = json.dumps(data, indent = 4))

@app.route("/removeInventory")
def removeInventory():
	return render_template("removeInventory.html")

@app.route("/dataAfterRemoval", methods = ['POST', "GET"])
def displayInventoryAfterRemoval():
	output = request.form.to_dict()
	print(output)
	sku = output["sku"]
	
	
	data = CURD.removeInventoryData(sku)
	
	return render_template("dataAfterRemoval.html", data = json.dumps(data, indent = 4))

@app.route("/updateInventoryDetails")
def updatedInventoryDetails():
	return render_template("updateInventoryDetails.html")

@app.route("/updatedInventory", methods = ['POST', "GET"])
def updatedInventory():
	output = request.form.to_dict()
	print(output)
	sku = output["sku"]
	productName = output["productName"]
	dateCreated = output["dateCreated"]
	inventoryAvailable = output["inventoryAvailable"]
	price = output["price"]
	warehouseLocation = output["warehouseLocation"]
	
	data = CURD.updateInventoryData(sku, productName, dateCreated, inventoryAvailable, price, warehouseLocation)
	
	return render_template("updatedInventory.html", data = json.dumps(data, indent = 4))

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "./Data/productsInventory.csv"
    return send_file(path, as_attachment=True)
if __name__ == '__main__':
	app.run(debug= True, port=5001)

